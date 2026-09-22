from pathlib import Path
import numpy as np

OUT=Path('outputs'); OUT.mkdir(parents=True,exist_ok=True)

# Checkpoint 93: exact viscous Kelvin law + natural-time amplification implies
# a much smaller vorticity-gradient ruler.
# For a material loop C_t,
#   dGamma/dt = nu int_C Delta u . dx = -nu int_C curl omega . dx.
# If length(C)<=c_L delta and Gamma changes by an O(1) fraction in one nonlinear
# time tau~delta^2/Gamma, then somewhere on the loop
#   |grad omega| >= const Gamma^2/(nu delta^3).
# Relative to Omega~Gamma/delta^2 this yields
#   ell_grad/delta <= const/Re_Gamma.
# At inherited parent amplitude, the circulation Reynolds number at ell_grad is
#   Re_ell ~ 1/Re_parent.
# To make that subscale itself a next high-Re vortex with Re_next=m Re_parent,
# vorticity amplitude must be boosted by ~m Re_parent^2.

Res=np.logspace(0,6,121)
ms=[1.0,2.0,4.0]
rows=[]
for Re in Res:
    ell_over_delta=1.0/Re
    diffusion_time_over_nonlinear=1.0/Re
    inherited_Re_sub=1.0/Re
    for m in ms:
        target_Re=m*Re
        amplitude_boost=target_Re/inherited_Re_sub # m Re^2
        min_log_stretch=np.log(amplitude_boost)
        rows.append((Re,m,ell_over_delta,diffusion_time_over_nonlinear,
                     inherited_Re_sub,target_Re,amplitude_boost,min_log_stretch))
arr=np.array(rows,float)
np.savetxt(OUT/'checkpoint_93_kelvin_gradient_trap.csv',arr,delimiter=',',
           header='Re_parent,m,ell_grad_over_delta,tau_diff_ell_over_tau_nl,Re_sub_if_parent_amplitude,Re_target_next,required_vorticity_amplitude_boost,log_boost',comments='')

lines=[]
lines.append('Checkpoint 93 - Kelvin gradient trap for circulation amplification')
lines.append('')
lines.append('Exact viscous Kelvin law for a material loop:')
lines.append('  dGamma/dt = nu integral_C Delta u . dx = -nu integral_C curl(omega) . dx.')
lines.append('If an O(1) fractional circulation increase occurs in tau_nl~delta^2/Gamma while loop length is O(delta), then')
lines.append('  ||grad omega||_loop >= O(Gamma^2/(nu delta^3)).')
lines.append('With Omega~Gamma/delta^2, the corresponding gradient length obeys')
lines.append('  ell_grad/delta <= O(1/Re_Gamma).')
lines.append('Its diffusion time is shorter than the parent nonlinear time by the same factor:')
lines.append('  tau_nu(ell_grad)/tau_nl <= O(1/Re_Gamma).')
lines.append('At the parent vorticity amplitude, that subscale has')
lines.append('  Re_ell ~ O(1/Re_parent),')
lines.append('so it is strongly diffusive, not a new high-Re vortex.')
lines.append('To turn it into a next-generation vortex with Re_next=m Re_parent requires an amplitude multiplication O(m Re_parent^2).')
lines.append('')
for Re in [10,100,1000,10000]:
    for m in [2]:
        boost=m*Re*Re
        lines.append(f'Re={Re:g}, m={m:g}: ell/delta~{1/Re:.3g}, inherited Re_ell~{1/Re:.3g}, required omega boost~{boost:.3g}, log boost~{np.log(boost):.3g}')
lines.append('')
lines.append('Interpretation: the formal m>1 cascade cannot amplify circulation on the parent nonlinear clock without first generating an even thinner, faster-diffusing gradient layer. If that layer is promoted to the next high-Re generation, its vorticity amplitude must jump by ~Re^2. This does not prove impossibility, but it converts circulation amplification into an explicit nested-scale/strain escalation rather than a free cascade parameter.')
(OUT/'checkpoint_93_kelvin_gradient_trap.txt').write_text('\n'.join(lines))
print('\n'.join(lines))
