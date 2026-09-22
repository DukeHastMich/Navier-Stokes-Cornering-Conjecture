import numpy as np, time
rng=np.random.default_rng(123456)
M=4; CORE=.05
Pbase=np.array([-0.39152222,0.46783813,0.38618739,-0.26343015,0.22127862,-0.06004850,-0.33713882,0.51200028,-0.33031461,0.14111113,-0.08935009,-0.35328273])

def evaluate(P,N=96):
 h=2*np.pi/N
 def dtheta(X): return (np.roll(X,-1,0)-np.roll(X,1,0))/(2*h)
 th=2*np.pi*np.arange(N)/N; c=P.reshape((2,3,2)); X=np.c_[np.cos(th),np.sin(th),np.zeros(N)]
 for idx,k in enumerate((2,3)):
  X += c[idx,:,0][None,:]*np.cos(k*th)[:,None]+c[idx,:,1][None,:]*np.sin(k*th)[:,None]
 X-=X.mean(0); X/=np.sqrt(np.mean(np.sum(X*X,1)))
 Xt=dtheta(X); sp=np.linalg.norm(Xt,axis=1); tang=Xt/(sp[:,None]+1e-15)
 r=X[:,None,:]-X[None,:,:]; den=(np.sum(r*r,2)+CORE**2)**1.5
 K=np.cross(Xt[None,:,:],r)/den[:,:,None]*h/(4*np.pi); arc=np.floor(np.arange(N)*M/N).astype(int)
 parts=np.zeros((M,N,3))
 for m in range(M): parts[m]=K[:,arc==m].sum(1)
 U=parts.sum(0); Urel=U-U.mean(0); rho=np.mean(np.sum(X*Urel,1))
 cyc=[]
 for target in range(M):
  src=(target-1)%M; dU=dtheta(parts[src]); alpha=np.sum(tang*dU,1)/(sp+1e-15); mask=arc==target
  cyc.append(np.sum(alpha[mask]*sp[mask])/np.sum(sp[mask]))
 # curvature reach + nonlocal sep (exclude fixed arclength fraction ~.08 of N each side)
 dt=(np.roll(tang,-1,0)-np.roll(tang,1,0))/(2*h); kap=np.linalg.norm(dt,axis=1)/(sp+1e-15); rc=1/(kap.max()+1e-15)
 D=np.linalg.norm(r,axis=2); mask=np.ones((N,N),bool); ex=max(3,int(round(.04*N)))
 ii=np.arange(N)
 for off in range(-ex,ex+1): mask[ii,(ii+off)%N]=False
 hs=.5*D[mask].min(); reach=min(rc,hs)
 return rho,np.array(cyc),reach,rc,hs

def score(P):
 rho,cyc,reach,rc,hs=evaluate(P)
 # reward simultaneous relay/contraction, strongly reward usable reach
 margin=min(-rho,cyc.min())
 # feasible positive margin gets priority; reach penalty if <.08
 return margin + .20*min(reach,.15), (rho,cyc,reach,rc,hs)

best=[]; tic=time.time()
# candidates: scaled base, noisy base, and random low-mode perturbations
Ps=[]
for f in np.linspace(.4,1.0,13): Ps.append(Pbase*f)
for _ in range(1800):
 f=rng.uniform(.3,1.0); P=f*Pbase + rng.normal(0,.12,size=12)
 Ps.append(np.clip(P,-.8,.8))
for _ in range(1000): Ps.append(rng.uniform(-.45,.45,size=12))
for i,P in enumerate(Ps):
 sc,m=score(P); rho,cyc,reach,rc,hs=m
 if rho<0 and cyc.min()>0:
  best.append((reach,min(-rho,cyc.min()),-rho,cyc.min(),sc,P.copy(),cyc.copy(),rc,hs))
best.sort(key=lambda x:(x[0],x[1]),reverse=True)
with open('/mnt/data/checkpoint_80_geometry_search.txt','w') as f:
 f.write(f'evals={len(Ps)} elapsed={time.time()-tic:.3f}s feasible={len(best)}\n')
 for j,b in enumerate(best[:20]):
  reach,margin,contr,mincyc,sc,P,cyc,rc,hs=b
  f.write(f'#{j} reach={reach:.6g} margin={margin:.6g} contraction={contr:.6g} mincyc={mincyc:.6g} rc={rc:.6g} hs={hs:.6g}\n')
  f.write(' P='+np.array2string(P,precision=8,separator=',')+'\n cyc='+np.array2string(cyc,precision=8)+'\n')
 if best:
  np.save('/mnt/data/checkpoint_80_bestP.npy',best[0][5])
print(open('/mnt/data/checkpoint_80_geometry_search.txt').read()[:6000])
