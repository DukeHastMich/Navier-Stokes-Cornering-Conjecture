import numpy as np
from scipy.interpolate import CubicSpline

N=80
M=4
EPS=0.15
DS=0.005
SMAX=30.0
SAVE_EVERY=10
REPARAM_EVERY=5
P=np.array([
    -0.39152222,  0.46783813,
     0.38618739, -0.26343015,
     0.22127862, -0.06004850,
    -0.33713882,  0.51200028,
    -0.33031461,  0.14111113,
    -0.08935009, -0.35328273,
])

def dtheta(X):
    h=2*np.pi/len(X)
    return (np.roll(X,-1,axis=0)-np.roll(X,1,axis=0))/(2*h)

def normalize(X):
    X=X-X.mean(axis=0)
    R=np.sqrt(np.mean(np.sum(X*X,axis=1)))
    return X/R

def reparam(X):
    # periodic cubic interpolation to uniform arclength, then renormalize
    Xc=np.vstack([X,X[0]])
    seg=np.linalg.norm(np.diff(Xc,axis=0),axis=1)
    s=np.concatenate([[0.0],np.cumsum(seg)])
    L=s[-1]
    if L<=0: return normalize(X)
    su=np.linspace(0,L,N+1)[:-1]
    out=np.empty((N,3))
    for j in range(3):
        cs=CubicSpline(s,Xc[:,j],bc_type='periodic')
        out[:,j]=cs(su)
    return normalize(out)

def make_curve():
    th=2*np.pi*np.arange(N)/N
    coeff=P.reshape((2,3,2))
    X=np.column_stack((np.cos(th),np.sin(th),np.zeros(N)))
    for idx,k in enumerate((2,3)):
        X += coeff[idx,:,0][None,:]*np.cos(k*th)[:,None]
        X += coeff[idx,:,1][None,:]*np.sin(k*th)[:,None]
    return normalize(X)

def velocity_and_parts(Y):
    n=len(Y); h=2*np.pi/n
    Xt=dtheta(Y)
    r=Y[:,None,:]-Y[None,:,:]
    den=(np.sum(r*r,axis=2)+EPS**2)**1.5
    K=np.cross(Xt[None,:,:],r)/den[:,:,None]*h/(4*np.pi)
    arc=np.floor(np.arange(n)*M/n).astype(int)
    parts=np.zeros((M,n,3))
    for m in range(M): parts[m]=K[:,arc==m,:].sum(axis=1)
    return parts.sum(axis=0),parts,arc

def zfield(Y):
    U,_,_=velocity_and_parts(Y)
    Uc=U.mean(axis=0)
    Yc=Y-Y.mean(axis=0)
    Urel=U-Uc
    rho=np.mean(np.sum(Yc*Urel,axis=1)) # R dR/dt when R=1
    return Urel-rho*Yc, rho

def metrics(Y):
    n=len(Y); h=2*np.pi/n
    Xt=dtheta(Y); sp=np.linalg.norm(Xt,axis=1); tang=Xt/(sp[:,None]+1e-15)
    U,parts,arc=velocity_and_parts(Y)
    Uc=U.mean(axis=0); rho=np.mean(np.sum(Y*(U-Uc),axis=1))
    alpha=np.zeros((M,n))
    for src in range(M):
        dU=dtheta(parts[src])
        alpha[src]=np.sum(tang*dU,axis=1)/(sp+1e-15)
    cyc=[]
    for target in range(M):
        mask=arc==target; w=sp[mask]; src=(target-1)%M
        cyc.append(np.sum(alpha[src,mask]*w)/np.sum(w))
    cyc=np.array(cyc)
    L=np.sum(sp)*h
    # shape descriptors: eigenvalues of covariance; chirality; Fourier energies 1..8
    C=(Y.T@Y)/n
    ev=np.linalg.eigvalsh(C)[::-1]
    # curvature rms approximated in theta coordinates
    t=tang
    dt=dtheta(t)
    kappa=np.linalg.norm(dt,axis=1)/(sp+1e-15)
    krms=np.sqrt(np.sum((kappa**2)*sp)/np.sum(sp))
    kmax=np.max(kappa)
    # normalized mode powers invariant to rotations only partly; pairwise distance spectrum gives rotation invariant summary
    D=np.linalg.norm(Y[:,None,:]-Y[None,:,:],axis=2)
    # sample sorted upper triangle quantiles
    vals=D[np.triu_indices(n,1)]
    qs=np.quantile(vals,[.1,.25,.5,.75,.9])
    return rho,L,*cyc,*ev,krms,kmax,*qs

def rk4(Y):
    k1,_=zfield(Y)
    k2,_=zfield(normalize(Y+0.5*DS*k1))
    k3,_=zfield(normalize(Y+0.5*DS*k2))
    k4,_=zfield(normalize(Y+DS*k3))
    Z=Y+(DS/6)*(k1+2*k2+2*k3+k4)
    return normalize(Z)

Y=make_curve(); rows=[]; shapes=[]
nsteps=int(round(SMAX/DS))
for step in range(nsteps+1):
    if step%SAVE_EVERY==0:
        s=step*DS; rows.append((s,*metrics(Y))); shapes.append(Y.copy())
    if step<nsteps:
        Y=rk4(Y)
        if (step+1)%REPARAM_EVERY==0: Y=reparam(Y)

rows=np.asarray(rows); shapes=np.asarray(shapes)
header='s,rho,L,cyc0,cyc1,cyc2,cyc3,cov1,cov2,cov3,krms,kmax,dq10,dq25,dq50,dq75,dq90'
np.savetxt('/mnt/data/checkpoint_71_zspace_trace.csv',rows,delimiter=',',header=header,comments='')
np.save('/mnt/data/checkpoint_71_zspace_shapes.npy',shapes)
# analyze recurrence in rotation-invariant descriptor vector excluding s and rho maybe include L/cov/kappa/quantiles/cyc
feat=rows[:,2:] # all shape-ish incl cyc
# standardize by robust overall scale
mu=feat.mean(0); sd=feat.std(0)+1e-12; F=(feat-mu)/sd
# nearest recurrence for each late point excluding temporal neighbors +/- 20 saved frames (=1 s)
best=[]
for i in range(len(F)):
    candidates=np.r_[0:max(0,i-20), min(len(F),i+21):len(F)]
    if len(candidates)==0: continue
    d=np.linalg.norm(F[candidates]-F[i],axis=1)
    j=candidates[np.argmin(d)]
    best.append((d.min(),i,j,abs(rows[i,0]-rows[j,0])))
best=sorted(best)[:20]
# fixed-point drift: Euclidean descriptor speed late
Df=np.linalg.norm(np.diff(F,axis=0),axis=1)/(SAVE_EVERY*DS)
# test autocorrelation / candidate period from descriptor scalar projection PC1
X=F-F.mean(0)
u,svals,vt=np.linalg.svd(X,full_matrices=False)
pc1=u[:,0]*svals[0]
pc1=pc1-pc1.mean()
ac=np.correlate(pc1,pc1,mode='full')[len(pc1)-1:]
ac/=np.arange(len(pc1),0,-1)
ac/=ac[0]
# candidate local maxima lag > 20
peaks=[]
for k in range(21,len(ac)-1):
    if ac[k]>ac[k-1] and ac[k]>=ac[k+1]: peaks.append((ac[k],k,k*SAVE_EVERY*DS))
peaks=sorted(peaks,reverse=True)[:10]
# contraction average rho; physical scale would obey dR^2/dt=2rho at R=1, in s d log R /ds = rho
# cumulative log scale change under renormalized trajectory = integral rho ds
logR=np.concatenate([[0],np.cumsum(0.5*(rows[1:,1]+rows[:-1,1])*np.diff(rows[:,0]))])
np.savetxt('/mnt/data/checkpoint_71_zspace_logR.csv',np.column_stack([rows[:,0],logR]),delimiter=',',header='s,logR_cumulative',comments='')
with open('/mnt/data/checkpoint_71_zspace_results.txt','w') as f:
    f.write('Checkpoint 71: renormalized Z-space closed-filament relay\n')
    f.write('Toy regularized Biot-Savart filament model; NOT full Navier-Stokes.\n')
    f.write(f'N={N}, eps=a/R={EPS}, ds={DS}, smax={SMAX}, reparam_every={REPARAM_EVERY}\n\n')
    f.write(f'initial rho={rows[0,1]:.9g}; final rho={rows[-1,1]:.9g}\n')
    f.write(f'mean rho all={rows[:,1].mean():.9g}; mean rho last half={rows[len(rows)//2:,1].mean():.9g}\n')
    f.write(f'fraction rho<0 all={(rows[:,1]<0).mean():.4f}; last half={(rows[len(rows)//2:,1]<0).mean():.4f}\n')
    f.write(f'cumulative int rho ds to smax={logR[-1]:.9g} (negative would indicate net scale contraction in this gauge)\n')
    f.write(f'L initial={rows[0,2]:.9g}; final={rows[-1,2]:.9g}\n')
    f.write('cyc initial='+np.array2string(rows[0,3:7],precision=6)+'\n')
    f.write('cyc final='+np.array2string(rows[-1,3:7],precision=6)+'\n')
    f.write(f'late descriptor speed mean={Df[len(Df)//2:].mean():.9g}; min={Df[len(Df)//2:].min():.9g}\n\n')
    f.write('Best nontrivial descriptor recurrences (standardized distance, s_i, s_j, |ds|):\n')
    for d,i,j,sep in best[:10]: f.write(f'{d:.6g}, {rows[i,0]:.6g}, {rows[j,0]:.6g}, {sep:.6g}\n')
    f.write('\nStrongest PC1 autocorrelation peaks (corr, lag frames, period s):\n')
    for a,k,p in peaks: f.write(f'{a:.6g}, {k}, {p:.6g}\n')
print(open('/mnt/data/checkpoint_71_zspace_results.txt').read())
