from pathlib import Path
import numpy as np

OUT=Path('outputs')
OUT.mkdir(parents=True,exist_ok=True)
CNU=4.0
CGEOM=1.0

yvals=np.logspace(-1,-6,6)
rows=[]
for y in yvals:
    rows.append((y,CNU/y))
arr=np.array(rows)
np.savetxt(OUT/'checkpoint_85_escape_scaling.csv',arr,delimiter=',',header='y_core_over_scale_sq,min_ARe_for_nonincrease',comments='')

ratios=np.array([1,2,4,8,16,32,64],dtype=float)
# If strain from a source a distance d away satisfies sigma <= C Gamma_s/d^2,
# while relative core thinning requires sigma a^2/nu >= c_nu,
# then Re_s >= (c_nu/C)(d/a)^2.
remote=np.column_stack([ratios,(CNU/CGEOM)*ratios**2])
np.savetxt(OUT/'checkpoint_85_remote_pusher.csv',remote,delimiter=',',header='d_over_a,min_Re_source_scaling_Cgeom1',comments='')

lines=[]
lines.append('Checkpoint 85 - escape-variable collapse and remote-pusher scaling')
lines.append('Conditional coherent-core algebra; NOT a full Navier-Stokes theorem.')
lines.append('')
lines.append('Start from the comparison inequality')
lines.append("    dy/ds >= c_nu/Re_delta - A_delta y,")
lines.append('where y=a^2/delta^2.')
lines.append('Whenever y is nonincreasing, y_s <= 0, so necessarily')
lines.append('    A_delta Re_delta y >= c_nu.')
lines.append('Equivalently')
lines.append('    A_delta Re_delta >= c_nu/y')
lines.append('and, because A_delta Re_delta y = (sigma-2 gamma) a^2/nu,')
lines.append('    (sigma-2 gamma) a^2/nu >= c_nu.')
lines.append('Thus the two apparent escape variables are not independent: their product must diverge at least like 1/y if a/delta -> 0 while y keeps decreasing.')
lines.append('')
lines.append('Required A_delta*Re_delta versus y:')
for y,q in rows:
    lines.append(f'  y={y:.1e}: A*Re >= {q:.6g}')
lines.append('')
lines.append('Remote-pusher scaling:')
lines.append('If a source at distance d supplies sigma <= C Gamma_s/d^2, then the same core-thinning gate requires')
lines.append('    Re_s = Gamma_s/nu >= (c_nu/C) (d/a)^2.')
for r,req in remote:
    lines.append(f'  d/a={r:5.1f}: Re_s >= {req:.6g}  (illustrative C=1)')
lines.append('')
lines.append('If the pusher remains at the outer geometric scale d~delta, then d/a~1/sqrt(y), so Re_s must grow like 1/y.')
lines.append('If instead d collapses to O(a), the source has entered the core scale and a is the new ruler; this is a renormalization escape, not an independent large-A mechanism.')
lines.append('')
lines.append('Critical-norm interpretation (coherent single-scale heuristic):')
lines.append('For U_delta ~ Gamma_delta/delta in a blob occupying O(delta^3), the local L3 size scales like U_delta*delta ~ Gamma_delta.')
lines.append('Hence Re_delta=Gamma_delta/nu is the dimensionless critical-amplitude variable. Re_delta -> infinity is the model analogue of escaping every bounded-L3 rescaling.')
lines.append('This is consistent with, but does not prove, the known theorem that any genuine finite-time 3D Navier-Stokes blowup must have ||u(t)||_L3 -> infinity (Seregin 2012).')

(OUT/'checkpoint_85_escape_scaling.txt').write_text('\n'.join(lines))
print('\n'.join(lines))
