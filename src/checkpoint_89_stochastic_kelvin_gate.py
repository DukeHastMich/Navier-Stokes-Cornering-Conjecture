from pathlib import Path
import numpy as np

OUT = Path('outputs')
OUT.mkdir(parents=True, exist_ok=True)

# Constantin-Iyer statistical Kelvin theorem motivates the following necessary
# geometric bookkeeping.  For a current loop C_delta spanning area ~pi delta^2,
#   Gamma_t(C_delta) = E Gamma_0(A_t(C_delta)).
# If ||omega_0||_infty=M0, Stokes + area formula give schematically
#   |Gamma_t| <= M0*pi*delta^2 * E[K2],
# where K2 is the 2-area stretch of the stochastic back-to-label map.
# Hence E[K2] >= Gamma_t/(M0*pi*delta^2).
# If a deterministic uniform strain integral J bounds each path's area stretch by
# K2 <= exp(2J), then J >= .5 log(K2_required).  For random J this translates to
# a required exponential moment, not a pointwise bound.

M0=1.0
nu=1.0
ps=[0.0,0.1,0.25,0.5]
deltas=np.logspace(-1,-8,57)
rows=[]
for p in ps:
    for d in deltas:
        Gamma=d**(-p)  # illustrative critical-amplitude growth law
        Kreq=Gamma/(np.pi*M0*d*d)
        Juniform=max(0.0,0.5*np.log(Kreq))
        rows.append((p,d,Gamma,Kreq,Juniform))
arr=np.array(rows,float)
np.savetxt(OUT/'checkpoint_89_stochastic_kelvin_gate.csv',arr,delimiter=',',
           header='p,delta,Gamma_delta_eq_delta_minus_p,min_expected_area_stretch_K2,min_uniform_integrated_strain_J',comments='')

# Compare the gate with the abstract merger cascade of checkpoint 88.
cases=[(2,.20),(2,.10),(3,.08),(4,.04)]
mr=[]
for m,q in cases:
    required_area_factor=m/(q*q) # K_{n+1}/K_n needed by Gamma/area scaling
    Jreq=.5*np.log(required_area_factor)
    collapse_impulse=-np.log(q)
    extra=Jreq-collapse_impulse # = .5 log m
    mr.append((m,q,required_area_factor,Jreq,collapse_impulse,extra))
mr=np.array(mr,float)
np.savetxt(OUT/'checkpoint_89_merger_area_gate.csv',mr,delimiter=',',
           header='m,q,required_back_area_factor_per_generation,J_required_half_log_factor,log_scale_contraction,extra_J_over_contraction',comments='')

lines=[]
lines.append('Checkpoint 89 - walking the small-circulation loop backward (stochastic Kelvin gate)')
lines.append('Necessary bookkeeping derived from the Constantin-Iyer statistical Kelvin representation; NOT a new regularity theorem.')
lines.append('')
lines.append('For a current loop C_delta spanning O(delta^2), statistical Kelvin gives')
lines.append('  Gamma_t(C_delta) = E[ Gamma_0(A_t(C_delta)) ].')
lines.append('If M0=||omega_0||_infty, Stokes plus the area formula give schematically')
lines.append('  |Gamma_t| <= M0*pi*delta^2 E[K2],')
lines.append('so')
lines.append('  E[K2] >= |Gamma_t|/(M0*pi*delta^2),')
lines.append('where K2 is the two-dimensional area distortion of the stochastic back-to-label map.')
lines.append('')
lines.append('Thus a current small-scale loop with growing circulation cannot appear from a bounded backward geometry: its stochastic preimages must, on average, span rapidly growing area. In an incompressible flow this is the backward-area / forward-stretch version of the same strain mechanism.')
lines.append('If a deterministic pathwise bound K2<=exp(2J) is available, J must satisfy J >= (1/2)log K2_required. In the genuinely stochastic formula only an exponential-moment requirement follows without further assumptions.')
lines.append('')
lines.append('For Gamma_delta ~ delta^{-p}, the required area stretch scales as delta^{-(2+p)}.')
for p in ps:
    lines.append(f'  p={p:.2f}: K2_required ~ delta^(-{2+p:.2f})')
lines.append('')
lines.append('For an m-fold aggregation with scale ratio q, each generation needs backward area amplification at least m/q^2. The corresponding uniform-strain impulse floor is')
lines.append('  J_generation >= 0.5 log(m/q^2) = -log q + 0.5 log m.')
for m,q,k,j,c,e in mr:
    lines.append(f'  m={m:.0f}, q={q:.3f}: area factor={k:.6g}, J>={j:.6g}, pure contraction log(1/q)={c:.6g}, extra={e:.6g}')
lines.append('')
lines.append('Crucially, this still does not kill the Type-II cascade: one-scale strain sigma~Gamma/delta^2 acting for tau~delta^2/Gamma already supplies O(1) strain impulse per generation, and a geometry coefficient large enough could meet the logarithmic gate. The backward calculation therefore identifies what must diverge/deform, but does not close the theorem.')
(OUT/'checkpoint_89_stochastic_kelvin_gate.txt').write_text('\n'.join(lines))
print('\n'.join(lines))
