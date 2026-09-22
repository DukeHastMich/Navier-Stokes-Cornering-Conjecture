from pathlib import Path
import numpy as np

OUT=Path('outputs'); OUT.mkdir(parents=True,exist_ok=True)

# Checkpoint 97: audit whether the square-root ladder conflicts with the basic critical budgets.
# Normalize nu=delta0=1. The proxies are deliberately simple scale estimates:
#   E_j ~ Gamma_j^2 delta_j
#   dissipation-per-nonlinear-time ~ nu Gamma_j delta_j
#   impulse scale ~ Gamma_j delta_j^2
#   L3-critical single-scale amplitude ~ Gamma_j/nu = Re_j.
# None is a theorem for a dense cluster; the point is to see whether the reduced budgets themselves diverge.

def ladder(R0, stop=1.5, max_levels=64):
    R=float(R0); d=1.0
    out=[]
    for j in range(max_levels):
        G=R
        E=G*G*d
        D=G*d
        I=G*d*d
        tau=d*d/G
        out.append((j,R,d,E,D,I,tau))
        if R<=stop: break
        d/=np.sqrt(R); R=np.sqrt(R)
    return np.array(out,float)

rows=[]
lines=['Checkpoint 97 - critical cost audit of nested helper ladder','']
for R0 in [1e4,1e8,1e16,1e32]:
    a=ladder(R0)
    sums=a[:,3:].sum(axis=0)
    for r in a: rows.append((R0,*r))
    lines.append(f'R0={R0:.0e}: levels={len(a)}, sum(Eproxy)={sums[0]:.6g}, sum(Dproxy)={sums[1]:.6g}, sum(Iproxy)={sums[2]:.6g}, sum(tau)={sums[3]:.6g}')
    lines.append(f'  ratios to first level: E={sums[0]/a[0,3]:.6g}, D={sums[1]/a[0,4]:.6g}, I={sums[2]/a[0,5]:.6g}, time={sums[3]/a[0,6]:.6g}')

arr=np.array(rows,float)
np.savetxt(OUT/'checkpoint_97_critical_cost_audit.csv',arr,delimiter=',',
           header='R0,level,Re,delta,Eproxy,Dproxy,ImpulseProxy,tau',comments='')
lines += [
    '',
    'Result: the nested ladder is dominated by its outer level in these standard scale proxies. The helper hierarchy does not create a new divergent energy, impulse, dissipation-per-stage, or time series by itself.',
    'This is exactly what critical scaling allows. It is a failed-obstruction result, not evidence that a true Navier-Stokes cascade exists.',
    '',
    'Important consequence: checkpoint 93 remains a valid conditional statement at fixed inherited amplitude, but its interpretation as a likely fatal Re^2 promotion cost is too strong. A dense Type-II mechanism can interpose diffusion-compatible intermediate layers and use them as transient transfer machinery rather than demanding that the thinnest Kelvin layer immediately become the next high-Re primary vortex.'
]
(OUT/'checkpoint_97_critical_cost_audit.txt').write_text('\n'.join(lines))
print('\n'.join(lines))
