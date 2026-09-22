import numpy as np
from scipy.interpolate import CubicSpline

N=80; M=4; DS=0.0015; SMAX=1.2; REPARAM_EVERY=5
P=np.array([-0.39152222,0.46783813,0.38618739,-0.26343015,0.22127862,-0.06004850,-0.33713882,0.51200028,-0.33031461,0.14111113,-0.08935009,-0.35328273])
EPSLIST=[0.01,0.02,0.03,0.035]

def dtheta(X):
 h=2*np.pi/len(X); return (np.roll(X,-1,0)-np.roll(X,1,0))/(2*h)
def normalize(X):
 X=X-X.mean(0); return X/np.sqrt(np.mean(np.sum(X*X,axis=1)))
def reparam(X):
 Xc=np.vstack([X,X[0]]); seg=np.linalg.norm(np.diff(Xc,axis=0),axis=1); s=np.r_[0,np.cumsum(seg)]; L=s[-1]; su=np.linspace(0,L,N+1)[:-1]
 out=np.column_stack([CubicSpline(s,Xc[:,j],bc_type='periodic')(su) for j in range(3)]); return normalize(out)
def make_curve():
 th=2*np.pi*np.arange(N)/N; c=P.reshape((2,3,2)); X=np.c_[np.cos(th),np.sin(th),np.zeros(N)]
 for idx,k in enumerate((2,3)):
  X += c[idx,:,0][None,:]*np.cos(k*th)[:,None] + c[idx,:,1][None,:]*np.sin(k*th)[:,None]
 return normalize(X)
def velocity(Y,eps):
 h=2*np.pi/N; Xt=dtheta(Y); r=Y[:,None,:]-Y[None,:,:]; den=(np.sum(r*r,axis=2)+eps**2)**1.5
 return (np.cross(Xt[None,:,:],r)/den[:,:,None]*h/(4*np.pi)).sum(axis=1)
def zfield(Y,eps):
 U=velocity(Y,eps); Urel=U-U.mean(0); rho=np.mean(np.sum(Y*Urel,axis=1)); return Urel-rho*Y,rho
def rk4(Y,eps):
 k1,_=zfield(Y,eps); k2,_=zfield(normalize(Y+.5*DS*k1),eps); k3,_=zfield(normalize(Y+.5*DS*k2),eps); k4,_=zfield(normalize(Y+DS*k3),eps)
 return normalize(Y+DS*(k1+2*k2+2*k3+k4)/6)
def reach(Y,ex=3):
 Xt=dtheta(Y); sp=np.linalg.norm(Xt,axis=1); t=Xt/(sp[:,None]+1e-15); dt=dtheta(t); kap=np.linalg.norm(dt,axis=1)/(sp+1e-15); rc=1/(kap.max()+1e-15)
 D=np.linalg.norm(Y[:,None,:]-Y[None,:,:],axis=2); mask=np.ones((N,N),bool)
 for i in range(N):
  for off in range(-ex,ex+1): mask[i,(i+off)%N]=False
 hs=.5*D[mask].min(); return min(rc,hs),rc,hs

rows=[]
for eps in EPSLIST:
 Y=make_curve(); first_expand=None; first_overlap=None; min_rho=1e9; min_reach=1e9; rho0=None
 nsteps=int(round(SMAX/DS))
 for step in range(nsteps+1):
  s=step*DS; _,rho=zfield(Y,eps)
  if rho0 is None: rho0=rho
  min_rho=min(min_rho,rho)
  if first_expand is None and rho>=0: first_expand=s
  if step%5==0:
   rr,rc,hs=reach(Y); min_reach=min(min_reach,rr)
   if first_overlap is None and eps>=rr: first_overlap=s
  if step<nsteps:
   Y=rk4(Y,eps)
   if (step+1)%REPARAM_EVERY==0: Y=reparam(Y)
 rows.append([eps,rho0,first_expand if first_expand is not None else np.nan,first_overlap if first_overlap is not None else np.nan,min_rho,min_reach])
arr=np.array(rows,float)
np.savetxt('/mnt/data/checkpoint_73_zspace_core_sweep.csv',arr,delimiter=',',header='eps,rho0,first_rho_nonnegative_s,first_eps_ge_reach_s,min_rho,min_reach',comments='')
with open('/mnt/data/checkpoint_73_zspace_core_sweep.txt','w') as f:
 f.write('Checkpoint 73: Z-space coherent-core sweep\nToy regularized Biot-Savart filament, normalized Rg=1. NOT Navier-Stokes.\n')
 f.write(f'N={N}, ds={DS}, smax={SMAX}\n\n')
 f.write('eps      rho0       first expand    first core>=reach   min rho      min reach\n')
 for row in arr:
  f.write(f'{row[0]:.3f}  {row[1]: .6f}   {row[2]:10.5f}      {row[3]:10.5f}       {row[4]: .6f}   {row[5]:.6f}\n')
print(open('/mnt/data/checkpoint_73_zspace_core_sweep.txt').read())
