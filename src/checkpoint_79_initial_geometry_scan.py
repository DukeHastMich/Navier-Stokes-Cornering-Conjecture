import numpy as np
from pathlib import Path
Path("outputs").mkdir(parents=True, exist_ok=True)

P0=np.array([-0.39152222,0.46783813,0.38618739,-0.26343015,0.22127862,-0.06004850,-0.33713882,0.51200028,-0.33031461,0.14111113,-0.08935009,-0.35328273])
N=256; M=4; EPS=0.03

def dtheta(X):
 h=2*np.pi/N; return (np.roll(X,-1,0)-np.roll(X,1,0))/(2*h)
def normalize(X):
 X=X-X.mean(0); return X/np.sqrt(np.mean(np.sum(X*X,axis=1)))
def make_curve(f):
 th=2*np.pi*np.arange(N)/N; c=(f*P0).reshape((2,3,2)); X=np.c_[np.cos(th),np.sin(th),np.zeros(N)]
 for idx,k in enumerate((2,3)):
  X += c[idx,:,0][None,:]*np.cos(k*th)[:,None]+c[idx,:,1][None,:]*np.sin(k*th)[:,None]
 return normalize(X)
def velocity_parts(Y):
 h=2*np.pi/N; Xt=dtheta(Y); r=Y[:,None,:]-Y[None,:,:]; den=(np.sum(r*r,2)+EPS**2)**1.5
 K=np.cross(Xt[None,:,:],r)/den[:,:,None]*h/(4*np.pi); arc=np.floor(np.arange(N)*M/N).astype(int)
 parts=np.zeros((M,N,3))
 for m in range(M): parts[m]=K[:,arc==m].sum(1)
 return parts.sum(0),parts,arc
def metrics(Y):
 h=2*np.pi/N; Xt=dtheta(Y); sp=np.linalg.norm(Xt,axis=1); tang=Xt/(sp[:,None]+1e-15)
 U,parts,arc=velocity_parts(Y); Urel=U-U.mean(0); rho=np.mean(np.sum(Y*Urel,axis=1))
 cyc=[]
 for target in range(M):
  src=(target-1)%M; dU=dtheta(parts[src]); alpha=np.sum(tang*dU,axis=1)/(sp+1e-15); mask=arc==target; cyc.append(np.sum(alpha[mask]*sp[mask])/np.sum(sp[mask]))
 # reach: curvature radius and nonlocal half-distance; exclude +/- ~5% curve indices
 dt=dtheta(tang); kap=np.linalg.norm(dt,axis=1)/(sp+1e-15); rc=1/(kap.max()+1e-15)
 D=np.linalg.norm(Y[:,None,:]-Y[None,:,:],axis=2); mask=np.ones((N,N),bool); ex=8
 idx=np.arange(N)
 for off in range(-ex,ex+1): mask[idx,(idx+off)%N]=False
 hs=.5*D[mask].min(); reach=min(rc,hs)
 L=np.sum(sp)*h; spacing=L/N
 return rho,np.array(cyc),reach,rc,hs,L,spacing

rows=[]
for f in np.linspace(.05,1.0,20):
 Y=make_curve(f); rho,cyc,reach,rc,hs,L,spacing=metrics(Y)
 rows.append([f,rho,*cyc,reach,rc,hs,L,spacing,EPS/reach,spacing/EPS])
arr=np.array(rows)
np.savetxt('outputs/checkpoint_79_initial_geometry_scan.csv',arr,delimiter=',',header='f,rho,cyc0,cyc1,cyc2,cyc3,reach,curv_radius,half_nonlocal_sep,L,spacing,eps_over_reach,spacing_over_eps',comments='')
print('f rho mincyc reach eps/reach spacing/eps')
for r in arr:
 print(f'{r[0]:.2f} {r[1]: .5f} {r[2:6].min(): .5f} {r[6]:.5f} {r[11]:.3f} {r[12]:.3f}')
