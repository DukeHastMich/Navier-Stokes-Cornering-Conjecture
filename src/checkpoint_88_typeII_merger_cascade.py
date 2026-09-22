from pathlib import Path
import numpy as np

OUT = Path('outputs')
OUT.mkdir(parents=True, exist_ok=True)

# Abstract adversarial scale cascade. This is deliberately NOT claimed as an NSE solution.
# Generation n:
#   Gamma_n = Gamma0 * m^n          (same-signed circulation aggregation)
#   delta_n = delta0 * q^n         (active ruler)
#   Re_n ~ Gamma_n/nu
#   y_n=a_n^2/delta_n^2 ~ const/Re_n  (best-case bounded-geometry core floor)
# Standard one-scale proxies:
#   U_n ~ Gamma_n/delta_n
#   tau_n ~ delta_n^2/Gamma_n
#   E_n ~ Gamma_n^2 delta_n
#   dissipation per generation ~ E_n when y_n ~ nu/Gamma_n
# The question is whether there is a nonempty parameter region where Gamma->inf,
# core ratio->0, total time finite, AND sum of stage dissipation finite.

ms = [2,3,4,5]
qs = np.geomspace(0.005, 0.8, 300)
rows=[]
for m in ms:
    for q in qs:
        time_ratio = q*q/m
        energy_ratio = m*m*q
        l3_ratio = m
        core_ratio = m**-0.5  # (a/delta)_{n+1}/(a/delta)_n if y~1/Re
        feasible = (energy_ratio < 1.0) and (time_ratio < 1.0)
        rows.append((m,q,time_ratio,energy_ratio,l3_ratio,core_ratio,float(feasible)))
arr=np.array(rows,float)
np.savetxt(OUT/'checkpoint_88_typeII_merger_phase.csv',arr,delimiter=',',
           header='m,q,time_ratio_q2_over_m,stage_energy_ratio_m2q,L3_or_Gamma_ratio_m,relative_core_ratio_m_minus_half,finite_budget_window',comments='')

# Representative feasible and boundary trajectories.
def trajectory(m,q,N=14):
    n=np.arange(N+1,dtype=float)
    Gamma=m**n
    delta=q**n
    Re=Gamma
    y=1/Gamma
    relcore=np.sqrt(y)
    a=delta*relcore
    U=Gamma/delta
    tau=delta**2/Gamma
    E=Gamma**2*delta
    Omega=Gamma/(a*a)
    return np.column_stack([n,Gamma,delta,Re,relcore,a,U,tau,E,Omega])

cases=[(2,0.20,'feasible_m2_q020'),(2,0.25,'boundary_m2_q025'),(3,0.08,'feasible_m3_q008')]
for m,q,name in cases:
    tr=trajectory(m,q)
    np.savetxt(OUT/f'checkpoint_88_{name}.csv',tr,delimiter=',',
               header='n,Gamma,delta,Re,core_over_delta,a,U,tau,stage_energy_proxy,omega_proxy',comments='')

lines=[]
lines.append('Checkpoint 88 - abstract circulation-aggregation / Type-II cascade stress test')
lines.append('Algebraic adversary only; NOT a constructed Navier-Stokes solution.')
lines.append('')
lines.append('Assume Gamma_n=m^n Gamma_0 and delta_n=q^n delta_0 with m>1, 0<q<1.')
lines.append('Using the bounded-geometry core floor y_n=(a_n/delta_n)^2 ~ 1/Re_n gives a_n/delta_n ~ m^{-n/2}.')
lines.append('One-scale proxies then obey:')
lines.append('  tau_{n+1}/tau_n = q^2/m')
lines.append('  E_{n+1}/E_n ~ D_{n+1}/D_n = m^2 q')
lines.append('  critical L3/circulation amplitude Gamma_{n+1}/Gamma_n = m')
lines.append('')
lines.append('Therefore there is a NONEMPTY formal finite-budget window')
lines.append('  q < 1/m^2,')
lines.append('in which Gamma_n -> infinity and a_n/delta_n -> 0, while both total Zeno time and the sum of the model stage-dissipation costs converge.')
lines.append('This means the present energy + finite-core gates alone do NOT rule out a Type-II cascade that aggregates circulation while shrinking the active ruler faster than Gamma^{-2}.')
lines.append('')
for m in ms:
    lines.append(f'm={m}: formal finite-budget window q < {1/(m*m):.8f}')
lines.append('')
lines.append('Representative m=2,q=0.20: energy/dissipation ratio per generation = 0.8, time ratio = 0.02, while Gamma doubles and relative core thickness falls by sqrt(2) each generation.')
lines.append('At the boundary q=1/4, the per-generation energy proxy is constant, so an infinite sequence with a comparable dissipation toll would exhaust finite energy; strict q<1/4 is needed in this model.')
lines.append('')
lines.append('Interpretation: the surviving algebraic monster is unambiguously Type II. It must increase a critical amplitude while making each new ruler dramatically smaller. This is consistent with Seregin\'s theorem that true finite-time blowup requires ||u||_L3 -> infinity; it does not provide such a blowup construction.')
(OUT/'checkpoint_88_typeII_merger_cascade.txt').write_text('\n'.join(lines))
print('\n'.join(lines))
