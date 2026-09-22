import numpy as np
from scipy.interpolate import CubicSpline
N=256; M=4; CORE=0.05; DS=0.0015; SMAX=2.0; REPARAM_EVERY=5; SAVE_EVERY=10
P=np.array([-0.35689105,0.49044896,0.11072659,-0.103841,0.11431879,-0.21819872,-0.32107964,0.25192189,-0.51089946,0.16385267,-0.25518278,-0.33879372])

def dtheta(X):
 h=2*np.pi/N; return (np.roll(X,-1,0)-np.roll(X,1,0))/(2*h)
def normalize(X):
 X=X-X.mean(0); return X/np.sqrt(np.mean(np.sum(X*X,axis=1)))
def reparam(X):
 Xc=np.vstack([X,X[0]]); seg=np.linalg.norm(np.diff(Xc,axis=0),axis=1); s=np.r_[0,np.cumsum(seg)]; L=s[-1]; su=np.linspace(0,L,N+1)[:-1]
 out=np.column_stack([CubicSpline(s,Xc[:,j],bc_type='periodic')(su) for j in range(3)]); return normalize(out)
def make_curve():
 th=2*np.pi*np.arange(N)/N; c=P.reshape((2,3,2)); X=np.c_[np.cos(th),np.sin(th),np.zeros(N)]
 for idx,k in enumerate((2,3)):
  X += c[idx,:,0][None,:]*np.cos(k*th)[:,None]+c[idx,:,1][None,:]*np.sin(k*th)[:,None]
 return normalize(X)
def velocity_parts(Y):
 h=2*np.pi/N; Xt=dtheta(Y); r=Y[:,None,:]-Y[None,:,:]; den=(np.sum(r*r,2)+CORE**2)**1.5
 K=np.cross(Xt[None,:,:],r)/den[:,:,None]*h/(4*np.pi); arc=np.floor(np.arange(N)*M/N).astype(int)
 parts=np.zeros((M,N,3))
 for m in range(M): parts[m]=K[:,arc==m].sum(1)
 return parts.sum(0),parts,arc
def zfield(Y):
 U,_,_=velocity_parts(Y); Urel=U-U.mean(0); rho=np.mean(np.sum(Y*Urel,axis=1)); return Urel-rho*Y,rho
def rk4(Y):
 k1,_=zfield(Y); k2,_=zfield(normalize(Y+.5*DS*k1)); k3,_=zfield(normalize(Y+.5*DS*k2)); k4,_=zfield(normalize(Y+DS*k3)); return normalize(Y+DS*(k1+2*k2+2*k3+k4)/6)
def metrics(Y):
 h=2*np.pi/N; Xt=dtheta(Y); sp=np.linalg.norm(Xt,axis=1); tang=Xt/(sp[:,None]+1e-15)
 U,parts,arc=velocity_parts(Y); Urel=U-U.mean(0); rho=np.mean(np.sum(Y*Urel,axis=1))
 cyc=[]
 for target in range(M):
  src=(target-1)%M; dU=dtheta(parts[src]); alpha=np.sum(tang*dU,axis=1)/(sp+1e-15); mask=arc==target; cyc.append(np.sum(alpha[mask]*sp[mask])/np.sum(sp[mask]))
 dt=dtheta(tang); kap=np.linalg.norm(dt,axis=1)/(sp+1e-15); rc=1/(kap.max()+1e-15)
 D=np.linalg.norm(Y[:,None,:]-Y[None,:,:],axis=2); mask=np.ones((N,N),bool); ex=max(3,int(round(.04*N))); ii=np.arange(N)
 for off in range(-ex,ex+1): mask[ii,(ii+off)%N]=False
 hs=.5*D[mask].min(); reach=min(rc,hs)
 L=np.sum(sp)*h; spacing=L/N
 return rho,*cyc,reach,rc,hs,L,spacing,CORE/reach,spacing/CORE
Y=make_curve(); rows=[]; first_expand=None; first_relay_fail=None; first_overlap=None
steps=int(round(SMAX/DS))
for step in range(steps+1):
 if step%SAVE_EVERY==0:
  s=step*DS; m=metrics(Y); rows.append((s,*m)); rho=m[0]; cyc=np.array(m[1:5]); cr=m[-2]
  if first_expand is None and rho>=0: first_expand=s
  if first_relay_fail is None and (rho>=0 or cyc.min()<=0): first_relay_fail=s
  if first_overlap is None and cr>=1: first_overlap=s
 if step<steps:
  Y=rk4(Y)
  if (step+1)%REPARAM_EVERY==0: Y=reparam(Y)
arr=np.array(rows)
np.savetxt('/mnt/data/checkpoint_81_resolved_zrelay.csv',arr,delimiter=',',header='s,rho,cyc0,cyc1,cyc2,cyc3,reach,curv_radius,half_nonlocal_sep,L,spacing,core_over_reach,spacing_over_core',comments='')
with open('/mnt/data/checkpoint_81_resolved_zrelay.txt','w') as f:
 f.write('Checkpoint 81 - better-resolved Z-space closed relay\nToy regularized Biot-Savart filament; NOT Navier-Stokes.\n')
 f.write(f'N={N}, core={CORE}, ds={DS}, smax={SMAX}\n')
 f.write(f'initial row={arr[0]}\n')
 f.write(f'first global expansion s={first_expand}\nfirst relay/contraction fail s={first_relay_fail}\nfirst core>=reach s={first_overlap}\n')
 i=np.argmin(arr[:,6]); f.write(f'min reach={arr[i,6]:.9g} at s={arr[i,0]:.6g}; core/reach={arr[i,11]:.6g}; rho={arr[i,1]:.6g}\n')
 f.write(f'final row={arr[-1]}\n')
print(open('/mnt/data/checkpoint_81_resolved_zrelay.txt').read())
