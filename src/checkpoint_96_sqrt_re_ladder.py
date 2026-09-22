from pathlib import Path
import numpy as np

OUT = Path('outputs'); OUT.mkdir(parents=True, exist_ok=True)

# Checkpoint 96: recursively apply the diffusion-compatible scaling from checkpoint 95.
# R_{j+1}=sqrt(R_j), delta_{j+1}=delta_j/sqrt(R_j).
# Then Omega_{j+1}/Omega_j=sqrt(R_j), and delta_j tends to delta_0/R_0.
# This is only a consistency ladder, not a constructed NS solution.

def ladder(R0, delta0=1.0, nu=1.0, stop=2.0, max_levels=32):
    R = float(R0)
    delta = float(delta0)
    rows=[]
    for j in range(max_levels):
        Gamma = nu*R
        Omega = Gamma/delta**2
        tau_nl = delta**2/Gamma
        Eproxy = Gamma**2*delta
        Dproxy = nu*Gamma*delta  # nu*Omega^2*delta^3*tau_nl
        rows.append((j,R,delta,Gamma,Omega,tau_nl,Eproxy,Dproxy))
        if R <= stop:
            break
        delta = delta/np.sqrt(R)
        R = np.sqrt(R)
    return np.array(rows,float)

R0s=[1e2,1e4,1e8,1e16]
all_rows=[]
lines=['Checkpoint 96 - nested square-root Reynolds ladder','']
for R0 in R0s:
    a=ladder(R0)
    for row in a:
        all_rows.append((R0,*row))
    lines.append(f'R0={R0:.0e}: levels_to_Re<=2 = {len(a)-1}, final Re={a[-1,1]:.6g}, final delta/delta0={a[-1,2]:.6g}, asymptotic delta0/R0={1/R0:.6g}')
    lines.append('  ' + ' -> '.join(f'{x:.4g}' for x in a[:,1]))

arr=np.array(all_rows,float)
np.savetxt(OUT/'checkpoint_96_sqrt_re_ladder.csv',arr,delimiter=',',
           header='R0,level,Re,delta,Gamma,Omega,tau_nl,Eproxy,Dproxy',comments='')

lines += [
    '',
    'Exact recursion identities:',
    '  Re_{j+1}=sqrt(Re_j)',
    '  delta_{j+1}=delta_j/sqrt(Re_j)',
    '  Omega_{j+1}/Omega_j=sqrt(Re_j)=Re_{j+1}',
    '  tau_{j+1}/tau_j=1/sqrt(Re_j)',
    '  Eproxy_{j+1}/Eproxy_j=Re_j^{-3/2}',
    '  Dproxy_{j+1}/Dproxy_j=Re_j^{-1}.',
    '',
    'As j increases, delta_j -> delta0/Re0 while Re_j -> 1. The direct delta/Re gradient ruler can therefore be resolved into only O(log log Re) diffusion-compatible intermediate layers.',
    'This does not construct the geometry or prove that the layers can self-organize. It shows that a one-step low-Re objection is not a contradiction: there is a formally consistent multiscale bridge with rapidly decreasing time/energy proxies.',
]
(OUT/'checkpoint_96_sqrt_re_ladder.txt').write_text('\n'.join(lines))
print('\n'.join(lines))
