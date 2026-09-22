import numpy as np
from scipy.interpolate import CubicSpline
import time
M=4; DS=.0015; SMAX=1.2; REPARAM_EVERY=5; SAVE_EVERY=10
P=np.array([-0.35689105,0.49044896,0.11072659,-0.103841,0.11431879,-0.21819872,-0.32107964,0.25192189,-0.51089946,0.16385267,-0.25518278,-0.33879372])

def run(N,CORE):
 h=2*np.pi/N
 def dtheta(X): return (np.roll(X,-1,0)-np.roll(X,1,0))/(2*h)
 def normalize(X): X=X-X.mean(0); return X/np.sqrt(np.mean(np.sum(X*X,1)))
 def reparam(X):
  Xc=np.vstack([X,X[0]]); seg=np.linalg.norm(np.diff(Xc,axis=0),axis=1); s=np.r_[0,np.cumsum(seg)]; su=np.linspace(0,s[-1],N+1)[:-1]
  return normalize(np.column_stack([CubicSpline(s,Xc[:,j],bc_type='periodic')(su) for j in range(3)]))
 def make_curve():
  th=2*np.pi*np.arange(N)/N; c=P.reshape((2,3,2)); X=np.c_[np.cos(th),np.sin(th),np.zeros(N)]
  for idx,k in enumerate((2,3)): X += c[idx,:,0][None,:]*np.cos(k*th)[:,None]+c[idx,:,1][None,:]*np.sin(k*th)[:,None]
  return normalize(X)
 arc=np.floor(np.arange(N)*M/N).astype(int)
 def vparts(Y):
  Xt=dtheta(Y); r=Y[:,None,:]-Y[None,:,:]; den=(np.sum(r*r,2)+CORE**2)**1.5
  K=np.cross(Xt[None,:,:],r)/den[:,:,None]*h/(4*np.pi); parts=np.zeros((M,N,3))
  for m in range(M): parts[m]=K[:,arc==m].sum(1)
  return parts.sum(0),parts
 def zfield(Y):
  U,_=vparts(Y); Urel=U-U.mean(0); rho=np.mean(np.sum(Y*Urel,1)); return Urel-rho*Y,rho
 def rk4(Y):
  k1,_=zfield(Y); k2,_=zfield(normalize(Y+.5*DS*k1)); k3,_=zfield(normalize(Y+.5*DS*k2)); k4,_=zfield(normalize(Y+DS*k3)); return normalize(Y+DS*(k1+2*k2+2*k3+k4)/6)
 def metrics(Y):
  Xt=dtheta(Y); sp=np.linalg.norm(Xt,axis=1); tang=Xt/(sp[:,None]+1e-15); U,parts=vparts(Y); Urel=U-U.mean(0); rho=np.mean(np.sum(Y*Urel,1)); cyc=[]
  for target in range(M):
   src=(target-1)%M; dU=dtheta(parts[src]); al=np.sum(tang*dU,1)/(sp+1e-15); mask=arc==target; cyc.append(np.sum(al[mask]*sp[mask])/np.sum(sp[mask]))
  dt=dtheta(tang); kap=np.linalg.norm(dt,axis=1)/(sp+1e-15); rc=1/(kap.max()+1e-15)
  D=np.linalg.norm(Y[:,None,:]-Y[None,:,:],axis=2); mask=np.ones((N,N),bool); ex=max(3,int(round(.04*N))); ii=np.arange(N)
  for off in range(-ex,ex+1): mask[ii,(ii+off)%N]=False
  hs=.5*D[mask].min(); reach=min(rc,hs); L=np.sum(sp)*h; return rho,np.min(cyc),reach,L/N
 Y=make_curve(); firstfail=None; overlap=None; minreach=1e9; init=None; tic=time.time()
 steps=int(round(SMAX/DS))
 for step in range(steps+1):
  if step%SAVE_EVERY==0:
   s=step*DS; rho,mincyc,reach,spacing=metrics(Y)
   if init is None: init=(rho,mincyc,reach,spacing)
   minreach=min(minreach,reach)
   if firstfail is None and (rho>=0 or mincyc<=0): firstfail=s
   if overlap is None and CORE>=reach: overlap=s
  if step<steps:
   Y=rk4(Y)
   if (step+1)%REPARAM_EVERY==0: Y=reparam(Y)
 return N,CORE,*init,firstfail,overlap,minreach,time.time()-tic
rows=[]
for N,c in [(256,.05),(320,.04),(384,.03)]:
 r=run(N,c); rows.append(r); print(r,flush=True)
arr=np.array([[np.nan if x is None else x for x in r] for r in rows],float)
np.savetxt('/mnt/data/checkpoint_82_resolved_core_sweep.csv',arr,delimiter=',',header='N,core,rho0,mincyc0,reach0,spacing0,first_fail_s,first_overlap_s,min_reach,elapsed',comments='')
with open('/mnt/data/checkpoint_82_resolved_core_sweep.txt','w') as f:
 f.write('Checkpoint 82 - resolution/core sweep for reach-safe relay candidate\nToy regularized Biot-Savart; NOT Navier-Stokes.\n')
 for r in rows: f.write(str(r)+'\n')
