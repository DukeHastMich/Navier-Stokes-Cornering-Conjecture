from pathlib import Path
import numpy as np

OUT=Path('outputs'); OUT.mkdir(parents=True,exist_ok=True)

# Checkpoint 92: nested one-sign flux monotonicity and the material-core viscous sign gate.
# For an aligned one-sign cross-section zeta(r)>=0,
#   Gamma(R)=2pi int_0^R zeta(r) r dr,
# so Gamma'(R)=2pi R zeta(R)>=0.
# A smaller nested ruler cannot contain more circulation at the same instant.
# In the parallel-tube conservative equation, for a boundary R(t) advected by
# the transverse fluid velocity,
#   d/dt Gamma_{R(t)} = 2 pi nu R partial_r zeta(R,t).
# Thus if zeta decreases outward at the material boundary, viscosity decreases
# enclosed circulation rather than amplifying it.

nu=0.03
Gamma_total=2.0
b=0.7
r=np.linspace(0,4,20001)
zeta=Gamma_total/(np.pi*b)*np.exp(-r*r/b)
# cumulative trapezoid without scipy
integrand=2*np.pi*zeta*r
cum=np.zeros_like(r)
cum[1:]=np.cumsum(0.5*(integrand[1:]+integrand[:-1])*np.diff(r))
dGamma_dr=2*np.pi*r*zeta
partial_r=-2*r*zeta/b
material_rate=2*np.pi*nu*r*partial_r

arr=np.column_stack([r,zeta,cum,dGamma_dr,material_rate])
np.savetxt(OUT/'checkpoint_92_nested_flux_gate.csv',arr[::20],delimiter=',',
           header='R,zeta,Gamma_enclosed,dGamma_dR,material_viscous_dGamma_dt',comments='')

lines=[]
lines.append('Checkpoint 92 - nested one-sign circulation gate')
lines.append('')
lines.append('For zeta>=0, Gamma(R)=2pi int_0^R zeta r dr has Gamma\'(R)=2pi R zeta(R)>=0.')
lines.append('Therefore a smaller nested cross-section cannot have larger same-signed circulation at one instant.')
lines.append('For a boundary advected by the transverse flow in the coherent parallel-tube equation:')
lines.append('  d Gamma_R/dt = 2 pi nu R partial_r zeta(R,t).')
lines.append('For a monotone core partial_r zeta<=0, so viscosity makes the material-core circulation nonincreasing.')
lines.append('')
lines.append(f'Gaussian test: min dGamma/dR={dGamma_dr.min():.6g}, max={dGamma_dr.max():.6g}')
lines.append(f'Gaussian material viscous circulation rate: min={material_rate.min():.6g}, max={material_rate.max():.6g}')
lines.append('')
lines.append('Escape requirement: Gamma growth along a supposed lineage requires flux recruitment from outside the previous core, a non-monotone/sign-changing boundary layer, or reconnection/redefinition of the tube. Pure stretching of the same one-sign coherent core cannot supply m>1.')
(OUT/'checkpoint_92_nested_flux_gate.txt').write_text('\n'.join(lines))
print('\n'.join(lines))
