import numpy as np
from scipy.interpolate import CubicSpline
from pathlib import Path

OUT = Path('outputs')
OUT.mkdir(parents=True, exist_ok=True)

# Better-resolved closed-relay geometry from checkpoints 80-82.
N = 320
M = 4
CORE = 0.04
DS = 0.0015
SMAX = 0.9
REPARAM_EVERY = 5
SAVE_EVERY = 5
CNU = 4.0  # coherent-core second-moment diffusion coefficient used in earlier model
P = np.array([
    -0.35689105, 0.49044896, 0.11072659, -0.103841,
     0.11431879,-0.21819872,-0.32107964, 0.25192189,
    -0.51089946, 0.16385267,-0.25518278,-0.33879372,
])

h = 2*np.pi/N
arc = np.floor(np.arange(N)*M/N).astype(int)

def dtheta(X):
    return (np.roll(X,-1,0)-np.roll(X,1,0))/(2*h)

def normalize(X):
    X = X-X.mean(0)
    return X/np.sqrt(np.mean(np.sum(X*X,axis=1)))

def reparam(X):
    Xc=np.vstack([X,X[0]])
    seg=np.linalg.norm(np.diff(Xc,axis=0),axis=1)
    s=np.r_[0,np.cumsum(seg)]
    su=np.linspace(0,s[-1],N+1)[:-1]
    out=np.column_stack([CubicSpline(s,Xc[:,j],bc_type='periodic')(su) for j in range(3)])
    return normalize(out)

def make_curve():
    th=2*np.pi*np.arange(N)/N
    c=P.reshape((2,3,2))
    X=np.c_[np.cos(th),np.sin(th),np.zeros(N)]
    for idx,k in enumerate((2,3)):
        X += c[idx,:,0][None,:]*np.cos(k*th)[:,None]
        X += c[idx,:,1][None,:]*np.sin(k*th)[:,None]
    return normalize(X)

def velocity_parts(Y):
    Xt=dtheta(Y)
    r=Y[:,None,:]-Y[None,:,:]
    den=(np.sum(r*r,2)+CORE**2)**1.5
    K=np.cross(Xt[None,:,:],r)/den[:,:,None]*h/(4*np.pi)
    parts=np.zeros((M,N,3))
    for m in range(M):
        parts[m]=K[:,arc==m].sum(1)
    return parts.sum(0),parts

def zfield(Y):
    U,_=velocity_parts(Y)
    Urel=U-U.mean(0)
    rho=np.mean(np.sum(Y*Urel,axis=1))
    return Urel-rho*Y,rho

def rk4(Y):
    k1,_=zfield(Y)
    k2,_=zfield(normalize(Y+.5*DS*k1))
    k3,_=zfield(normalize(Y+.5*DS*k2))
    k4,_=zfield(normalize(Y+DS*k3))
    return normalize(Y+DS*(k1+2*k2+2*k3+k4)/6)

def metrics(Y):
    Xt=dtheta(Y)
    sp=np.linalg.norm(Xt,axis=1)
    tang=Xt/(sp[:,None]+1e-15)
    U,parts=velocity_parts(Y)
    Urel=U-U.mean(0)
    rho=np.mean(np.sum(Y*Urel,axis=1))

    # Tangential stretching from the full induced velocity.
    dU=dtheta(U)
    alpha_total=np.sum(tang*dU,axis=1)/(sp+1e-15)

    cyc=[]
    for target in range(M):
        src=(target-1)%M
        dUs=dtheta(parts[src])
        al=np.sum(tang*dUs,axis=1)/(sp+1e-15)
        mask=arc==target
        cyc.append(np.sum(al[mask]*sp[mask])/np.sum(sp[mask]))

    # Reach proxy: min(curvature radius, half non-neighbor separation).
    dt=dtheta(tang)
    kap=np.linalg.norm(dt,axis=1)/(sp+1e-15)
    ik=int(np.argmax(kap))
    rc=1/(kap[ik]+1e-15)

    D=np.linalg.norm(Y[:,None,:]-Y[None,:,:],axis=2)
    mask=np.ones((N,N),bool)
    ex=max(3,int(round(.04*N)))
    ii=np.arange(N)
    for off in range(-ex,ex+1):
        mask[ii,(ii+off)%N]=False
    Dm=np.where(mask,D,np.inf)
    flat=int(np.argmin(Dm))
    ip,jp=np.unravel_index(flat,Dm.shape)
    hs=.5*Dm[ip,jp]

    if rc <= hs:
        reach=rc
        controller=0.0  # curvature
        sigma_local=alpha_total[ik]
        active_i,active_j=ik,ik
    else:
        reach=hs
        controller=1.0  # self-separation
        sigma_local=max(alpha_total[ip],alpha_total[jp])
        active_i,active_j=ip,jp

    # How much positive axial stretching is actually available near the point/pair
    # defining the shrinking ruler?  This distinguishes local support from outsourced
    # stretching elsewhere on the closed filament.
    da=np.minimum(np.linalg.norm(Y-Y[active_i],axis=1),np.linalg.norm(Y-Y[active_j],axis=1))
    near2=da <= 2.0*reach
    near4=da <= 4.0*reach
    sigma_near2=float(np.max(alpha_total[near2])) if np.any(near2) else float(sigma_local)
    sigma_near4=float(np.max(alpha_total[near4])) if np.any(near4) else float(sigma_local)
    imax=int(np.argmax(alpha_total))
    dist_to_alphamax=float(da[imax])

    L=np.sum(sp)*h
    return (rho,*cyc,float(np.max(alpha_total)),float(np.quantile(alpha_total,.95)),
            float(sigma_local),sigma_near2,sigma_near4,dist_to_alphamax,reach,rc,hs,L,L/N,controller,float(active_i),float(active_j),float(imax))

Y=make_curve()
rows=[]
steps=int(round(SMAX/DS))
for step in range(steps+1):
    if step%SAVE_EVERY==0:
        rows.append((step*DS,*metrics(Y)))
    if step<steps:
        Y=rk4(Y)
        if (step+1)%REPARAM_EVERY==0:
            Y=reparam(Y)

arr=np.asarray(rows,float)
s=arr[:,0]
rho=arr[:,1]
reach=arr[:,12]
sigma_local=arr[:,8]
sigma_near2=arr[:,9]
sigma_near4=arr[:,10]
dist_to_alphamax=arr[:,11]

# Physical local scale is delta_phys = R_global * delta_z, and d log R_global / ds = rho.
lnreach=np.log(reach)
dlnreach=np.gradient(lnreach,s,edge_order=2)
gamma_hat=-(rho+dlnreach)  # gamma * R^2/Gamma in the global-R gauge

# A_delta = (sigma - 2 gamma) delta^2 / Gamma; Gamma=1 in this filament normalization.
A=(sigma_local-2*gamma_hat)*reach**2
A_near2=(sigma_near2-2*gamma_hat)*reach**2
A_near4=(sigma_near4-2*gamma_hat)*reach**2
alpha_max=arr[:,6]
alpha_p95=arr[:,7]
A_max=(alpha_max-2*gamma_hat)*reach**2
A_p95=(alpha_p95-2*gamma_hat)*reach**2
# Equivalent form useful for checking signs.
A_alt=(sigma_local+2*(rho+dlnreach))*reach**2
assert np.allclose(A,A_alt,rtol=1e-11,atol=1e-11)

# The coherent-core gate from y' >= cnu/Re - A y.
y=(CORE/reach)**2
# If A<=0, no finite positive Re can make the lower-bound RHS non-positive.
Re_required=np.where(A>0,CNU/(A*y),np.inf)
# A*Re*y = ((sigma-2gamma) a^2/nu), using hypothetical Re values.
Res=(100,1000,4000,10000)
gates=np.column_stack([A*Re*y for Re in Res])

out=np.column_stack([arr,dlnreach,gamma_hat,A,A_near2,A_near4,A_p95,A_max,y,Re_required,gates])
header=(
's,rho,cyc0,cyc1,cyc2,cyc3,alpha_max,alpha_p95,sigma_local,sigma_near2,sigma_near4,dist_active_to_alphamax,reach,curv_radius,'
'half_nonlocal_sep,L,spacing,reach_controller,active_i,active_j,alpha_max_i,dlnreach_ds,gamma_hat,A_local,A_near2,A_near4,A_p95,A_max,'
'y_core_over_reach_sq,Re_required_local,gate_Re100,gate_Re1000,gate_Re4000,gate_Re10000'
)
np.savetxt(OUT/'checkpoint_84_escape_gate.csv',out,delimiter=',',header=header,comments='')

relay_ok=(rho<0)&(np.min(arr[:,2:6],axis=1)>0)
first_fail_idx=np.where(~relay_ok)[0]
first_fail_idx=int(first_fail_idx[0]) if len(first_fail_idx) else len(s)-1
pre=np.arange(0,first_fail_idx+1)
finite_req=np.isfinite(Re_required[pre])

with open(OUT/'checkpoint_84_escape_gate.txt','w') as f:
    f.write('Checkpoint 84 - local-scale escape gate on the resolved closed relay\n')
    f.write('Toy regularized Biot-Savart filament plus an overlaid coherent-core inequality; NOT full Navier-Stokes.\n')
    f.write(f'N={N}, regularization/core={CORE}, ds={DS}, smax={SMAX}, c_nu={CNU}\n\n')
    f.write('Definitions:\n')
    f.write('  delta = reach proxy = min(curvature radius, half non-neighbor separation).\n')
    f.write('  gamma_hat = gamma R^2/Gamma = -(rho + d log(delta_z)/ds).\n')
    f.write('  A_delta = (sigma_local - 2 gamma_hat) delta_z^2 (Gamma=1 normalization).\n')
    f.write('  y = (core/delta_z)^2. Core comparison gives y_s >= c_nu/Re - A_delta y.\n')
    f.write('  Therefore a necessary instantaneous condition for y to be nonincreasing is A_delta*Re*y >= c_nu.\n\n')
    f.write(f'first relay/contraction failure s={s[first_fail_idx]:.6g}\n')
    f.write(f'at failure: rho={rho[first_fail_idx]:.8g}, mincyc={np.min(arr[first_fail_idx,2:6]):.8g}, reach={reach[first_fail_idx]:.8g}, sigma_local={sigma_local[first_fail_idx]:.8g}\n')
    f.write(f'            gamma_hat={gamma_hat[first_fail_idx]:.8g}, A_delta={A[first_fail_idx]:.8g}, y={y[first_fail_idx]:.8g}, Re_required={Re_required[first_fail_idx]:.8g}\n')
    if finite_req.any():
        vals=Re_required[pre][finite_req]
        f.write(f'pre-failure finite Re_required: min={vals.min():.8g}, median={np.median(vals):.8g}, max={vals.max():.8g}\n')
    else:
        f.write('pre-failure A_delta never positive, so the lower-bound core gate cannot be satisfied at any finite Re in this diagnostic.\n')
    for Re,k in zip(Res,range(len(Res))):
        gv=gates[pre,k]
        f.write(f'Re={Re}: pre-failure max(A Re y)={np.nanmax(gv):.8g}; fraction >= c_nu={(gv>=CNU).mean():.4f}\n')
    shrinking=pre[gamma_hat[pre]>0]
    f.write(f'\npre-failure rows with physical local reach shrinking (gamma_hat>0): {len(shrinking)}\n')
    if len(shrinking):
        for label,AA in [('local',A),('near2',A_near2),('near4',A_near4),('p95-global',A_p95),('max-global',A_max)]:
            xx=AA[shrinking]
            f.write(f'  {label}: positive fraction={(xx>0).mean():.4f}; min/median/max={xx.min():.8g}/{np.median(xx):.8g}/{xx.max():.8g}\n')
        rr=dist_to_alphamax[shrinking]/reach[shrinking]
        f.write(f'  distance from active ruler to global alpha_max in reach units: median={np.median(rr):.6g}, min={rr.min():.6g}, max={rr.max():.6g}\n')
    f.write('\nInterpretation:\n')
    f.write('  This does not evolve a Navier-Stokes vortex core. It asks whether the measured local strain/contraction history would even pass the necessary coherent-core gate.\n')
    f.write('  The gate collapses the two apparent escape variables A_delta and Re_delta into their product: if y -> 0 while y is decreasing, A_delta Re_delta must diverge at least like c_nu/y.\n')

print(open(OUT/'checkpoint_84_escape_gate.txt').read())
