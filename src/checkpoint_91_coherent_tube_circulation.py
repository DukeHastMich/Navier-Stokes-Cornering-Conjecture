from pathlib import Path
import numpy as np

OUT = Path('outputs')
OUT.mkdir(parents=True, exist_ok=True)

# Checkpoint 91: exact circulation conservation in the aligned/parallel
# coherent-tube reduction.
#
# Let omega = zeta(x_perp,t) e_z and u=(v_perp, sigma(t) z), with
# div_perp(v_perp)=-sigma. Then
#   zeta_t + v_perp.grad zeta = sigma zeta + nu Delta_perp zeta
# becomes the conservative 2-D Fokker-Planck form
#   zeta_t + div_perp(v_perp zeta) = nu Delta_perp zeta.
# Therefore Gamma = int_R2 zeta dA is exactly constant for decaying fields.
# For the radial linear-strain case v_r=-sigma r/2, a Gaussian remains Gaussian
# with mean-square radius b satisfying b'=-sigma b+4 nu, while Gamma is fixed.

nu = 0.02
Gamma = 3.0
b = 0.8
T = 12.0
dt = 2e-4
sample_dt = 0.05

# Deliberately time-dependent strain, including intervals of weakening and reversal.
def sigma(t):
    return 1.3 + 0.65*np.sin(1.7*t) + 0.30*np.sin(4.1*t + 0.2)

rows=[]
next_sample=0.0
t=0.0
while t <= T + 0.5*dt:
    if t + 1e-12 >= next_sample:
        # Gaussian zeta = Gamma/(pi b) exp(-r^2/b).
        peak = Gamma/(np.pi*b)
        # Numerical quadrature on a radius large relative to sqrt(b).
        rmax = max(12.0*np.sqrt(b), 6.0)
        r = np.linspace(0.0, rmax, 20001)
        zeta = peak*np.exp(-(r*r)/b)
        Gamma_num = 2*np.pi*np.trapezoid(zeta*r, r)
        rows.append((t, sigma(t), b, np.sqrt(b), peak, Gamma_num,
                     (Gamma_num-Gamma)/Gamma))
        next_sample += sample_dt
    # RK4 for b'=-sigma(t)b+4nu
    def f(tt,bb): return -sigma(tt)*bb + 4.0*nu
    k1=f(t,b)
    k2=f(t+dt/2,b+dt*k1/2)
    k3=f(t+dt/2,b+dt*k2/2)
    k4=f(t+dt,b+dt*k3)
    b += dt*(k1+2*k2+2*k3+k4)/6
    t += dt

arr=np.array(rows,float)
np.savetxt(OUT/'checkpoint_91_coherent_tube_circulation.csv',arr,delimiter=',',
           header='t,sigma,b,core_radius_sqrt_b,peak_vorticity,numerical_Gamma,relative_Gamma_error',comments='')

lines=[]
lines.append('Checkpoint 91 - coherent parallel tube: stretching changes peak vorticity, not total circulation')
lines.append('')
lines.append('Exact reduction:')
lines.append('  zeta_t + div_perp(v_perp zeta) = nu Delta_perp zeta')
lines.append('  Gamma(t)=int_R2 zeta dA, hence dGamma/dt=0 under decay at infinity.')
lines.append('For radial linear strain, b\'=-sigma(t)b+4nu and zeta=Gamma/(pi b) exp(-r^2/b).')
lines.append('')
lines.append(f'time-dependent test: nu={nu:g}, Gamma={Gamma:g}, b0=0.8, T={T:g}')
lines.append(f'b range: {arr[:,2].min():.9g} .. {arr[:,2].max():.9g}')
lines.append(f'peak-vorticity range: {arr[:,4].min():.9g} .. {arr[:,4].max():.9g}')
lines.append(f'max numerical circulation relative error: {np.max(np.abs(arr[:,6])):.3e}')
lines.append('')
lines.append('Conclusion: within this exact coherent-tube reduction, axial stretching can make omega arbitrarily larger by shrinking the core, but cannot make Gamma or Re_Gamma grow. The m>1 Type-II corridor therefore cannot be realized by ordinary stretching of one isolated coherent tube.')
(OUT/'checkpoint_91_coherent_tube_circulation.txt').write_text('\n'.join(lines))
print('\n'.join(lines))
