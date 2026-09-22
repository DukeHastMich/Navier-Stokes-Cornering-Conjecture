from pathlib import Path
import numpy as np

OUT=Path('outputs'); OUT.mkdir(parents=True,exist_ok=True)

# Checkpoint 98 is a bookkeeping boundary marker.
# It records which assumptions close which reduced classes and which quantity must escape.
# No numerical PDE claim is made here.
rows = [
    ('bounded coherent Z-state', 1, 0, 0),
    ('fixed/comparable finite-core relay', 1, 0, 0),
    ('single self-closing near-aligned pair', 1, 0, 0),
    ('formal Type-II unbounded critical amplitude', 0, 1, 1),
    ('dense/reconnecting non-isolated cluster', 0, 1, 1),
    ('square-root Kelvin helper hierarchy', 0, 1, 1),
]
# encode strings separately for a plain text table; CSV gets integer class id.
np.savetxt(OUT/'checkpoint_98_route_boundary.csv',
           np.array([[i,r[1],r[2],r[3]] for i,r in enumerate(rows)],float),
           delimiter=',',header='class_id,ruled_out_by_current_reduced_arguments,requires_unbounded_renormalized_quantity,requires_new_full_PDE_estimate',comments='')
lines=['Checkpoint 98 - route boundary / stopping criterion','']
for i,(name,dead,unbounded,newpde) in enumerate(rows):
    lines.append(f'{i}: {name}: ruled_out={bool(dead)}, unbounded_escape={bool(unbounded)}, new_PDE_estimate={bool(newpde)}')
lines += [
    '',
    'Stopping conclusion for this research route:',
    'The cornering/finite-core/Biot-Savart arguments do rule out or strongly obstruct several coherent self-collapse mechanisms, but they do not control the remaining unbounded critical Type-II regime.',
    'Checkpoint 95-97 gives an explicit reduced scaling bridge showing why the Kelvin gradient trap does not close that regime: a delta/Re ruler can be resolved into O(log log Re) diffusion-compatible layers with Re values Re, sqrt(Re), Re^(1/4), ... and no new divergent critical budget.',
    'Any full proof now needs a genuinely new Navier-Stokes estimate controlling a scale-critical quantity (for example the positive middle strain eigenvalue, critical L3 velocity amplitude, or an equivalent circulation/area-distortion functional).',
    'This is a principled stopping point: further rearrangements of the same energy/core/circulation scaling are expected to reproduce the known critical gap rather than prove regularity.'
]
(OUT/'checkpoint_98_route_boundary.txt').write_text('\n'.join(lines))
print('\n'.join(lines))
