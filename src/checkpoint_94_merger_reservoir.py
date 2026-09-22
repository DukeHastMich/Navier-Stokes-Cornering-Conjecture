from pathlib import Path
import numpy as np

OUT=Path('outputs'); OUT.mkdir(parents=True,exist_ok=True)

# Checkpoint 94: if circulation growth is not same-tube viscous amplification,
# it must come from recruitment/merger.  Pure merger conserves signed circulation
# algebraically: child Gamma is the sum of incoming signed fluxes.
# For m-fold growth Gamma_n=m^n Gamma0, cumulative NET recruited circulation is
# Gamma_N-Gamma0.  A merger-only realization therefore needs an unbounded donor
# reservoir if Gamma_N -> infinity.
#
# Conditional smooth-isolated-tube packing model:
# If initial omega is C1 with ||grad omega||_infty=K, and an isolated tube of
# characteristic radius r drops from its core amplitude to ~0 over distance ~r,
# then Omega_peak <= K r.  With bounded cross-section geometry A<=C_A r^2,
# Gamma<=C_A K r^3.  Pairwise-disjoint enlarged tube neighborhoods in bounded
# volume imply sum r^3<infty and hence sum Gamma<infty.
# This is a conditional packing lemma, NOT a general NSE theorem.

Gamma0=1.0
ms=[2,3,4]
Nmax=18
rows=[]
for m in ms:
    for n in range(Nmax+1):
        Gamma=Gamma0*(m**n)
        cumulative_recruited=Gamma-Gamma0
        min_base_donors=m**n
        rows.append((m,n,Gamma,cumulative_recruited,min_base_donors))
arr=np.array(rows,float)
np.savetxt(OUT/'checkpoint_94_merger_recruitment.csv',arr,delimiter=',',
           header='m,n,Gamma_lineage,cumulative_net_recruited_Gamma,min_comparable_base_donor_count',comments='')

# Packing demonstration with geometric radii.
K=5.0; C_A=np.pi
qs=[0.9,0.7,0.5,0.3]
pack=[]
for q in qs:
    r=q**np.arange(200,dtype=float)
    Gamma_bound=C_A*K*r**3
    pack.append((q,Gamma_bound.sum(),(r**3).sum()))
np.savetxt(OUT/'checkpoint_94_isolated_tube_packing.csv',np.array(pack),delimiter=',',
           header='radius_ratio_q,sum_Gamma_upper_bound_CA_K_sum_r3,sum_r3',comments='')

lines=[]
lines.append('Checkpoint 94 - merger/recruitment accounting after same-tube amplification is removed')
lines.append('')
lines.append('If Gamma_{n+1}=m Gamma_n is produced only by merging/recruiting signed vortex flux, then')
lines.append('  Delta Gamma_n=(m-1)Gamma_n,')
lines.append('and the cumulative net recruited circulation telescopes to')
lines.append('  sum Delta Gamma = Gamma_N-Gamma_0.')
lines.append('Thus Gamma_N->infinity requires an unbounded net signed-flux reservoir; splitting and re-merging the same flux cannot multiply it.')
lines.append('')
lines.append('Conditional smooth-isolated donor lemma: if ||grad omega_0||_infty=K and each distinct donor tube of radius r is isolated by a low-vorticity gap of comparable width, then its peak vorticity is O(Kr), and bounded cross-section geometry gives Gamma=O(K r^3). Pairwise-disjoint comparable neighborhoods in bounded volume have sum r^3<infinity, hence finite total recruitable circulation.')
lines.append('This closes an infinite merger tree made of isolated coherent donor tubes under those geometry/isolation assumptions.')
lines.append('')
lines.append('But it is NOT unconditional. The escape is a dense/non-isolated cluster, sheet, sign-changing region, or repeated viscous reconnection where the notion of separate donor tubes breaks down. Rigorous Navier-Stokes reconnection results show that arbitrarily complicated FINITE reconnection cascades can occur in completely smooth solutions, so reconnection itself cannot be assigned a universal fixed energy toll.')
lines.append('')
for m in ms:
    lines.append(f'm={m}: generation {Nmax} needs Gamma/Gamma0={m**Nmax:g} and at least {m**Nmax:g} comparable base donors in a merger-only tree.')
(OUT/'checkpoint_94_merger_reservoir.txt').write_text('\n'.join(lines))
print('\n'.join(lines))
