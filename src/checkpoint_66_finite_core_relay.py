import numpy as np

# Finite-core augmentation of checkpoint 60.
# One smooth closed filament split into four fixed material arcs.
# Source arc j uses its own regularization radius a_j=sqrt(b_j).
# Core second moment obeys b_j' = -sigma_j b_j + 4 nu,
# where sigma_j is the arc-averaged TOTAL longitudinal stretch.
# This is a reduced coherent-core model, NOT a Navier-Stokes DNS or proof.

from pathlib import Path
Path("outputs").mkdir(parents=True, exist_ok=True)

N = 80
M = 4
DT = 0.0025
TMAX = 2.0
A0 = 0.15
B0 = A0*A0

P = np.array([
    -0.39152222,  0.46783813,
     0.38618739, -0.26343015,
     0.22127862, -0.06004850,
    -0.33713882,  0.51200028,
    -0.33031461,  0.14111113,
    -0.08935009, -0.35328273,
])

def dtheta(X):
    h = 2*np.pi/len(X)
    return (np.roll(X, -1, axis=0) - np.roll(X, 1, axis=0))/(2*h)

def make_curve():
    th = 2*np.pi*np.arange(N)/N
    coeff = P.reshape((2,3,2))
    X = np.column_stack((np.cos(th), np.sin(th), np.zeros(N)))
    for idx, k in enumerate((2,3)):
        X += coeff[idx,:,0][None,:]*np.cos(k*th)[:,None]
        X += coeff[idx,:,1][None,:]*np.sin(k*th)[:,None]
    X -= X.mean(axis=0)
    X /= np.sqrt(np.mean(np.sum(X*X, axis=1)))
    return X

arc_global = np.floor(np.arange(N)*M/N).astype(int)

def velocity_and_parts(X,b):
    n = len(X)
    h = 2*np.pi/n
    Xt = dtheta(X)
    r = X[:,None,:] - X[None,:,:]
    r2 = np.sum(r*r,axis=2)
    parts = np.zeros((M,n,3))
    for m in range(M):
        mask = arc_global == m
        den = (r2[:,mask] + max(b[m],1e-12))**1.5
        K = np.cross(Xt[None,mask,:], r[:,mask,:])/den[:,:,None] * h/(4*np.pi)
        parts[m] = K.sum(axis=1)
    return parts.sum(axis=0), parts

def state_derivative(X,b,nu):
    Xt = dtheta(X)
    speed = np.linalg.norm(Xt,axis=1)
    tang = Xt/(speed[:,None]+1e-15)
    U, parts = velocity_and_parts(X,b)
    dU = dtheta(U)
    alpha_total = np.sum(tang*dU,axis=1)/(speed+1e-15)
    sigma = np.zeros(M)
    for m in range(M):
        mask=arc_global==m; w=speed[mask]
        sigma[m]=np.sum(alpha_total[mask]*w)/np.sum(w)
    db = -sigma*b + 4*nu
    return U, db, sigma

def rk4(X,b,nu):
    k1x,k1b,_=state_derivative(X,b,nu)
    k2x,k2b,_=state_derivative(X+0.5*DT*k1x,b+0.5*DT*k1b,nu)
    k3x,k3b,_=state_derivative(X+0.5*DT*k2x,b+0.5*DT*k2b,nu)
    k4x,k4b,_=state_derivative(X+DT*k3x,b+DT*k3b,nu)
    Xn=X+(DT/6)*(k1x+2*k2x+2*k3x+k4x)
    bn=b+(DT/6)*(k1b+2*k2b+2*k3b+k4b)
    return Xn,np.maximum(bn,1e-12)

def metrics(X,b):
    h=2*np.pi/N
    Xt=dtheta(X); speed=np.linalg.norm(Xt,axis=1); tang=Xt/(speed[:,None]+1e-15)
    U,parts=velocity_and_parts(X,b)
    alpha=np.zeros((M,N))
    for src in range(M):
        dU=dtheta(parts[src])
        alpha[src]=np.sum(tang*dU,axis=1)/(speed+1e-15)
    dUt=dtheta(U)
    atot=np.sum(tang*dUt,axis=1)/(speed+1e-15)
    cyc=[]; total=[]
    for target in range(M):
        mask=arc_global==target; w=speed[mask]
        src=(target-1)%M
        cyc.append(np.sum(alpha[src,mask]*w)/np.sum(w))
        total.append(np.sum(atot[mask]*w)/np.sum(w))
    C=X.mean(axis=0); Uc=U.mean(axis=0)
    rg2=np.mean(np.sum((X-C)**2,axis=1))
    rg2dot=2*np.mean(np.sum((X-C)*(U-Uc),axis=1))
    length=np.sum(speed)*h
    ratio=np.sqrt(b/rg2)
    return np.array(cyc),np.array(total),rg2,rg2dot,length,ratio

def run(nu):
    X=make_curve(); b=np.full(M,B0)
    rows=[]; first_relay_fail=None; first_ratio_ge_025=None
    steps=int(round(TMAX/DT))
    for step in range(steps+1):
        t=step*DT
        cyc,total,rg2,rg2dot,L,ratio=metrics(X,b)
        rows.append([t,*cyc,*total,rg2,rg2dot,L,*b,*ratio])
        if first_relay_fail is None and (np.min(cyc)<=0 or rg2dot>=0):
            first_relay_fail=t
        if first_ratio_ge_025 is None and np.max(ratio)>=0.25:
            first_ratio_ge_025=t
        if step<steps:
            X,b=rk4(X,b,nu)
            if not np.all(np.isfinite(X)) or not np.all(np.isfinite(b)):
                break
    arr=np.array(rows)
    return arr,first_relay_fail,first_ratio_ge_025

nus=[0.0,1/10000,1/4000,1/1000,1/100]
summary=[]
for nu in nus:
    arr,fail,t025=run(nu)
    tag='inf' if nu==0 else f'{1/nu:.0f}'
    np.savetxt(f'outputs/checkpoint_66_trace_Re{tag}.csv',arr,delimiter=',',
               header='t,cyc0,cyc1,cyc2,cyc3,total0,total1,total2,total3,rg2,rg2dot,length,b0,b1,b2,b3,a0_over_Rg,a1_over_Rg,a2_over_Rg,a3_over_Rg',comments='')
    start=arr[0]; end=arr[-1]
    min_rg_idx=np.argmin(arr[:,9])
    min_rg=arr[min_rg_idx]
    summary.append({
        'nu':nu,'Re':np.inf if nu==0 else 1/nu,'fail':fail,'t025':t025,
        'min_rg_t':min_rg[0],'min_rg2':min_rg[9],
        'ratio_at_min':min_rg[16:20].copy(),
        'ratio_final':end[16:20].copy(),
        'b_final':end[12:16].copy(),
        'cyc_min_at_min':min_rg[1:5].min(),
        'total_at_min':min_rg[5:9].copy(),
    })

with open('outputs/checkpoint_66_finite_core_relay.txt','w') as f:
    f.write('Checkpoint 66 - finite-core closed-relay augmentation\n')
    f.write('Reduced coherent-core model; NOT Navier-Stokes DNS and NOT a proof.\n')
    f.write("b_j' = -sigma_j b_j + 4 nu; source Biot-Savart regularization radius a_j=sqrt(b_j).\n")
    f.write('Gamma normalized to 1, so Re_Gamma=1/nu. Initial a=0.15, Rg=1.\n\n')
    for s in summary:
        f.write(f"nu={s['nu']:.8g}, Re_Gamma={s['Re']}\n")
        f.write(f"  first relay/contraction failure: {s['fail']}\n")
        f.write(f"  first max(a/Rg)>=0.25: {s['t025']}\n")
        f.write(f"  minimum Rg^2 at t={s['min_rg_t']:.6f}: {s['min_rg2']:.8f}\n")
        f.write('  a/Rg at minimum Rg^2: '+np.array2string(s['ratio_at_min'],precision=6)+'\n')
        f.write('  total axial stretch at min Rg^2: '+np.array2string(s['total_at_min'],precision=6)+'\n')
        f.write(f"  min cyclic link at min Rg^2: {s['cyc_min_at_min']:.8f}\n")
        f.write('  final a/Rg: '+np.array2string(s['ratio_final'],precision=6)+'\n\n')

print(open('outputs/checkpoint_66_finite_core_relay.txt').read())
