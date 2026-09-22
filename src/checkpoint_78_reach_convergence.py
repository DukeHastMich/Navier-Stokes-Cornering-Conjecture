import numpy as np
from scipy.interpolate import CubicSpline
import time, csv
from pathlib import Path
Path("outputs").mkdir(parents=True, exist_ok=True)

P=np.array([-0.39152222,0.46783813,0.38618739,-0.26343015,0.22127862,-0.06004850,-0.33713882,0.51200028,-0.33031461,0.14111113,-0.08935009,-0.35328273])
EPS=0.01; DS=0.0015; SMAX=2.0; REPARAM_EVERY=5

def run(N):
    def dtheta(X):
        h=2*np.pi/N; return (np.roll(X,-1,0)-np.roll(X,1,0))/(2*h)
    def normalize(X):
        X=X-X.mean(0); return X/np.sqrt(np.mean(np.sum(X*X,axis=1)))
    def reparam(X):
        Xc=np.vstack([X,X[0]]); seg=np.linalg.norm(np.diff(Xc,axis=0),axis=1)
        s=np.r_[0,np.cumsum(seg)]; L=s[-1]; su=np.linspace(0,L,N+1)[:-1]
        out=np.column_stack([CubicSpline(s,Xc[:,j],bc_type='periodic')(su) for j in range(3)])
        return normalize(out)
    def make_curve():
        th=2*np.pi*np.arange(N)/N; c=P.reshape((2,3,2)); X=np.c_[np.cos(th),np.sin(th),np.zeros(N)]
        for idx,k in enumerate((2,3)):
            X += c[idx,:,0][None,:]*np.cos(k*th)[:,None] + c[idx,:,1][None,:]*np.sin(k*th)[:,None]
        return normalize(X)
    def velocity(Y):
        h=2*np.pi/N; Xt=dtheta(Y); r=Y[:,None,:]-Y[None,:,:]
        den=(np.sum(r*r,axis=2)+EPS**2)**1.5
        return (np.cross(Xt[None,:,:],r)/den[:,:,None]*h/(4*np.pi)).sum(axis=1)
    def zfield(Y):
        U=velocity(Y); Urel=U-U.mean(0); rho=np.mean(np.sum(Y*Urel,axis=1)); return Urel-rho*Y,rho
    def rk4(Y):
        k1,_=zfield(Y); k2,_=zfield(normalize(Y+.5*DS*k1)); k3,_=zfield(normalize(Y+.5*DS*k2)); k4,_=zfield(normalize(Y+DS*k3))
        return normalize(Y+DS*(k1+2*k2+2*k3+k4)/6)
    ex=max(3,round(3*N/80))
    def reach(Y):
        Xt=dtheta(Y); sp=np.linalg.norm(Xt,axis=1); t=Xt/(sp[:,None]+1e-15); dt=dtheta(t); kap=np.linalg.norm(dt,axis=1)/(sp+1e-15); rc=1/(kap.max()+1e-15)
        D=np.linalg.norm(Y[:,None,:]-Y[None,:,:],axis=2)
        mask=np.ones((N,N),bool)
        for off in range(-ex,ex+1):
            idx=np.arange(N); mask[idx,(idx+off)%N]=False
        hs=.5*D[mask].min(); return min(rc,hs),rc,hs
    Y=make_curve(); first_expand=None; first_overlap=None; minreach=(1e9,None,None,None); samples=[]
    steps=int(round(SMAX/DS)); tic=time.time()
    for step in range(steps+1):
        if step%10==0:
            s=step*DS; _,rho=zfield(Y); rr,rc,hs=reach(Y)
            samples.append((s,rho,rr,rc,hs))
            if first_expand is None and rho>=0: first_expand=s
            if first_overlap is None and EPS>=rr: first_overlap=s
            if rr<minreach[0]: minreach=(rr,s,rc,hs)
        if step<steps:
            Y=rk4(Y)
            if (step+1)%REPARAM_EVERY==0: Y=reparam(Y)
    elapsed=time.time()-tic
    arr=np.array(samples)
    np.savetxt(f'outputs/checkpoint_78_N{N}.csv',arr,delimiter=',',header='s,rho,reach,curv_radius,half_nonlocal_sep',comments='')
    return dict(N=N, ex=ex, first_expand=first_expand, first_overlap=first_overlap,min_reach=minreach[0],min_reach_s=minreach[1],min_rc=minreach[2],min_hs=minreach[3],elapsed=elapsed)

res=[]
for N in [80,120,160]:
    r=run(N); res.append(r); print(r, flush=True)
with open('outputs/checkpoint_78_reach_convergence.txt','w') as f:
    f.write('Checkpoint 78 - reach convergence test\nToy regularized filament; NOT Navier-Stokes. eps=0.01, smax=2.0.\n')
    for r in res: f.write(str(r)+'\n')
