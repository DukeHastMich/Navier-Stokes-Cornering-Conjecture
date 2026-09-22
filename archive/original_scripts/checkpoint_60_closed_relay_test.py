import numpy as np

# Checkpoint 60: closed four-arc vortex-filament relay test.
# This is a regularized Biot-Savart filament model, NOT a Navier-Stokes proof.
# It tests whether a single smooth closed filament can transiently outsource
# stretching around a closed cycle while its overall size contracts.

N = 80
M = 4
CORE = 0.15
DT = 0.01
TMAX = 1.50

# Low-order Fourier shape found by deterministic hill-climb in the research run.
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


def velocity_and_parts(X):
    n = len(X)
    h = 2*np.pi/n
    Xt = dtheta(X)
    r = X[:,None,:] - X[None,:,:]
    den = (np.sum(r*r, axis=2) + CORE**2)**1.5
    K = np.cross(Xt[None,:,:], r)/den[:,:,None] * h/(4*np.pi)
    arc = np.floor(np.arange(n)*M/n).astype(int)
    parts = np.zeros((M,n,3))
    for m in range(M):
        parts[m] = K[:,arc == m,:].sum(axis=1)
    return parts.sum(axis=0), parts, arc


def velocity(X):
    return velocity_and_parts(X)[0]


def metrics(X):
    n = len(X)
    h = 2*np.pi/n
    Xt = dtheta(X)
    speed = np.linalg.norm(Xt, axis=1)
    tang = Xt/(speed[:,None] + 1e-15)
    U, parts, arc = velocity_and_parts(X)

    alpha = np.zeros((M,n))
    for src in range(M):
        dU = dtheta(parts[src])
        alpha[src] = np.sum(tang*dU, axis=1)/(speed + 1e-15)

    cyc = []
    for target in range(M):
        mask = arc == target
        w = speed[mask]
        src = (target - 1) % M
        cyc.append(np.sum(alpha[src,mask]*w)/np.sum(w))
    cyc = np.array(cyc)

    C = X.mean(axis=0)
    Uc = U.mean(axis=0)
    rg2 = np.mean(np.sum((X-C)**2, axis=1))
    rg2dot = 2*np.mean(np.sum((X-C)*(U-Uc), axis=1))
    length = np.sum(speed)*h
    shape_complexity = length/np.sqrt(rg2)
    urms = np.sqrt(np.mean(np.sum(U*U, axis=1)))
    return cyc, rg2dot, length, shape_complexity, urms


def rk4(X):
    k1 = velocity(X)
    k2 = velocity(X + 0.5*DT*k1)
    k3 = velocity(X + 0.5*DT*k2)
    k4 = velocity(X + DT*k3)
    return X + (DT/6)*(k1 + 2*k2 + 2*k3 + k4)


X = make_curve()
rows = []
first_failure = None
for step in range(int(round(TMAX/DT)) + 1):
    t = step*DT
    cyc, rg2dot, length, chi, urms = metrics(X)
    rows.append((t, *cyc, rg2dot, length, chi, urms))
    if first_failure is None and (np.min(cyc) <= 0 or rg2dot >= 0):
        first_failure = (t, cyc.copy(), rg2dot, length, chi, urms)
    if step < int(round(TMAX/DT)):
        X = rk4(X)

rows = np.asarray(rows)
# integrate cyclic logarithmic stretch contributions up to the last strictly valid row
valid = np.where((rows[:,1:5].min(axis=1) > 0) & (rows[:,5] < 0))[0]
last_valid = valid[-1]
t = rows[:last_valid+1,0]
cy = rows[:last_valid+1,1:5]
integ = np.trapezoid(cy, t, axis=0)
gains = np.exp(integ)

np.savetxt(
    '/mnt/data/checkpoint_60_closed_relay_trace.csv', rows, delimiter=',',
    header='t,alpha_3to0,alpha_0to1,alpha_1to2,alpha_2to3,rg2dot,length,L_over_Rg,u_rms',
    comments=''
)

with open('/mnt/data/checkpoint_60_closed_relay_test.txt','w') as f:
    f.write('Closed four-arc regularized Biot-Savart relay test\n')
    f.write('NOT a Navier-Stokes simulation or proof.\n\n')
    f.write(f'N={N}, core={CORE}, dt={DT}, TMAX={TMAX}\n')
    f.write('Initial cyclic stretch rates: ' + np.array2string(rows[0,1:5], precision=8) + '\n')
    f.write(f'Initial d(Rg^2)/dt: {rows[0,5]:.8f}\n')
    f.write(f'Initial L/Rg: {rows[0,7]:.8f}\n')
    f.write(f'Initial u_rms: {rows[0,8]:.8f}\n')
    f.write(f'Initial turnover estimate Rg/u_rms: {1/rows[0,8]:.8f}\n\n')
    if first_failure:
        tt, cc, rr, LL, ch, uu = first_failure
        f.write(f'First failure of [all cyclic alpha>0 AND global contraction]: t={tt:.8f}\n')
        f.write('Cyclic rates at failure: ' + np.array2string(cc, precision=8) + '\n')
        f.write(f'd(Rg^2)/dt at failure: {rr:.8f}\n')
        f.write(f'L/Rg at failure: {ch:.8f}\n')
    f.write('\nIntegrated cyclic log-stretch before failure: ' + np.array2string(integ, precision=8) + '\n')
    f.write('Corresponding multiplicative gains: ' + np.array2string(gains, precision=8) + '\n')
    f.write(f'L/Rg growth before failure: {rows[last_valid,7]/rows[0,7]-1:.8%}\n')
    f.write('\nInterpretation: a single closed filament CAN transiently sustain a four-link internal\n')
    f.write('stretching relay while contracting. In this optimized low-mode example the relay\n')
    f.write('does not remain a collapsing state: shape complexity grows and contraction stalls/\n')
    f.write('reverses before large multiplicative cyclic gain is accumulated.\n')

print(open('/mnt/data/checkpoint_60_closed_relay_test.txt').read())
