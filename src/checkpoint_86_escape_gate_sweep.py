import numpy as np
from scipy.interpolate import CubicSpline
from scipy.signal import savgol_filter
from pathlib import Path
import time

OUT=Path('outputs'); OUT.mkdir(parents=True,exist_ok=True)
M=4; DS=.0015; SMAX=.5; REPARAM_EVERY=5; SAVE_EVERY=5; CNU=4.0
P=np.array([-0.35689105,0.49044896,0.11072659,-0.103841,0.11431879,-0.21819872,-0.32107964,0.25192189,-0.51089946,0.16385267,-0.25518278,-0.33879372])

def run(N,CORE):
    h=2*np.pi/N; arc=np.floor(np.arange(N)*M/N).astype(int)
    def dtheta(X): return (np.roll(X,-1,0)-np.roll(X,1,0))/(2*h)
    def normalize(X):
        X=X-X.mean(0); return X/np.sqrt(np.mean(np.sum(X*X,axis=1)))
    def reparam(X):
        Xc=np.vstack([X,X[0]]); seg=np.linalg.norm(np.diff(Xc,axis=0),axis=1); ss=np.r_[0,np.cumsum(seg)]
        su=np.linspace(0,ss[-1],N+1)[:-1]
        return normalize(np.column_stack([CubicSpline(ss,Xc[:,j],bc_type='periodic')(su) for j in range(3)]))
    def make_curve():
        th=2*np.pi*np.arange(N)/N; c=P.reshape((2,3,2)); X=np.c_[np.cos(th),np.sin(th),np.zeros(N)]
        for idx,k in enumerate((2,3)):
            X += c[idx,:,0][None,:]*np.cos(k*th)[:,None]+c[idx,:,1][None,:]*np.sin(k*th)[:,None]
        return normalize(X)
    def vparts(Y):
        Xt=dtheta(Y); r=Y[:,None,:]-Y[None,:,:]; den=(np.sum(r*r,2)+CORE**2)**1.5
        K=np.cross(Xt[None,:,:],r)/den[:,:,None]*h/(4*np.pi); parts=np.zeros((M,N,3))
        for m in range(M): parts[m]=K[:,arc==m].sum(1)
        return parts.sum(0),parts
    def zfield(Y):
        U,_=vparts(Y); Urel=U-U.mean(0); rho=np.mean(np.sum(Y*Urel,axis=1)); return Urel-rho*Y,rho
    def rk4(Y):
        k1,_=zfield(Y); k2,_=zfield(normalize(Y+.5*DS*k1)); k3,_=zfield(normalize(Y+.5*DS*k2)); k4,_=zfield(normalize(Y+DS*k3))
        return normalize(Y+DS*(k1+2*k2+2*k3+k4)/6)
    def met(Y):
        Xt=dtheta(Y); sp=np.linalg.norm(Xt,axis=1); tang=Xt/(sp[:,None]+1e-15)
        U,parts=vparts(Y); Urel=U-U.mean(0); rho=np.mean(np.sum(Y*Urel,axis=1))
        dU=dtheta(U); alpha=np.sum(tang*dU,axis=1)/(sp+1e-15)
        cyc=[]
        for target in range(M):
            src=(target-1)%M; dUs=dtheta(parts[src]); al=np.sum(tang*dUs,axis=1)/(sp+1e-15); mm=arc==target
            cyc.append(np.sum(al[mm]*sp[mm])/np.sum(sp[mm]))
        dt=dtheta(tang); kap=np.linalg.norm(dt,axis=1)/(sp+1e-15); ik=int(np.argmax(kap)); rc=1/(kap[ik]+1e-15)
        D=np.linalg.norm(Y[:,None,:]-Y[None,:,:],axis=2); mm=np.ones((N,N),bool); ex=max(3,int(round(.04*N))); ii=np.arange(N)
        for off in range(-ex,ex+1): mm[ii,(ii+off)%N]=False
        Dm=np.where(mm,D,np.inf); flat=int(np.argmin(Dm)); ip,jp=np.unravel_index(flat,Dm.shape); hs=.5*Dm[ip,jp]
        if rc<=hs: reach=rc; ai=aj=ik; siglocal=alpha[ik]
        else: reach=hs; ai,aj=ip,jp; siglocal=max(alpha[ip],alpha[jp])
        da=np.minimum(np.linalg.norm(Y-Y[ai],axis=1),np.linalg.norm(Y-Y[aj],axis=1))
        near2=da<=2*reach; sig2=np.max(alpha[near2]); imax=int(np.argmax(alpha)); distmax=da[imax]
        return rho,*cyc,reach,siglocal,sig2,np.max(alpha),distmax
    Y=make_curve(); rr=[]; tic=time.time(); steps=int(round(SMAX/DS))
    for step in range(steps+1):
        if step%SAVE_EVERY==0: rr.append((step*DS,*met(Y)))
        if step<steps:
            Y=rk4(Y)
            if (step+1)%REPARAM_EVERY==0: Y=reparam(Y)
    a=np.asarray(rr,float); s=a[:,0]; rho=a[:,1]; cyc=a[:,2:6]; reach=a[:,6]
    # Smooth only the derivative diagnostic, not the actual reach values.
    w=min(9,len(s) if len(s)%2==1 else len(s)-1)
    if w<5: w=5
    lnr=savgol_filter(np.log(reach),w,3,mode='interp')
    dln=np.gradient(lnr,s,edge_order=2); gamma=-(rho+dln)
    siglocal=a[:,7]; sig2=a[:,8]; sigmax=a[:,9]; distmax=a[:,10]
    Alocal=(siglocal-2*gamma)*reach**2; A2=(sig2-2*gamma)*reach**2; Amax=(sigmax-2*gamma)*reach**2; y=(CORE/reach)**2
    relay=(rho<0)&(np.min(cyc,axis=1)>0); fi=np.where(~relay)[0]; fail=int(fi[0]) if len(fi) else len(s)-1
    pre=np.arange(fail+1); sh=pre[gamma[pre]>0]
    def stats(A):
        if len(sh)==0: return (np.nan,)*5
        x=A[sh]; pos=x>0
        if not np.any(pos): return (float(np.mean(pos)),float(np.min(x)),float(np.median(x)),float(np.max(x)),np.inf)
        req=CNU/(x[pos]*y[sh][pos])
        return (float(np.mean(pos)),float(np.min(x)),float(np.median(x)),float(np.max(x)),float(np.median(req)))
    sl=stats(Alocal); s2=stats(A2); sm=stats(Amax)
    dr=(distmax[sh]/reach[sh]) if len(sh) else np.array([np.nan])
    return (N,CORE,s[fail],reach[fail],len(sh),*sl,*s2,*sm,float(np.nanmedian(dr)),float(np.nanmin(dr)),float(np.nanmax(dr)),time.time()-tic)

rows=[]
for N,c in [(256,.05),(320,.04),(384,.03)]:
    r=run(N,c); rows.append(r); print(r,flush=True)
arr=np.array(rows,float)
header=('N,core,first_fail_s,reach_at_fail,n_local_shrink,'
'local_posfrac,local_min,local_median,local_max,local_median_Re_req,'
'near2_posfrac,near2_min,near2_median,near2_max,near2_median_Re_req,'
'globalmax_posfrac,globalmax_min,globalmax_median,globalmax_max,globalmax_median_Re_req,'
'distmax_over_reach_median,distmax_over_reach_min,distmax_over_reach_max,elapsed_s')
np.savetxt(OUT/'checkpoint_86_escape_gate_sweep.csv',arr,delimiter=',',header=header,comments='')
with open(OUT/'checkpoint_86_escape_gate_sweep.txt','w') as f:
    f.write('Checkpoint 86 - resolution/core sweep of the local escape gate\n')
    f.write('Toy regularized Biot-Savart relay + coherent-core diagnostic; NOT full Navier-Stokes.\n')
    f.write('Derivative of log(reach) is Savitzky-Golay smoothed solely for the gamma diagnostic.\n')
    f.write('Each A statistic is restricted to pre-failure times when the physical local reach is shrinking (gamma_hat>0).\n\n')
    for r in rows:
        f.write(str(r)+'\n')
    f.write('\nColumn interpretation: local uses stretching exactly at the point/pair defining reach; near2 allows any stretching within 2 reach lengths; globalmax allows stretching anywhere on the loop.\n')
print(open(OUT/'checkpoint_86_escape_gate_sweep.txt').read())
