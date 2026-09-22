"""Symbolic verification of the local curvature-producing Navier-Stokes jet.
Generated during the Failure-to-Corner research run.
"""
import sympy as sp

x, y, z, Omega0, s, M = sp.symbols('x y z Omega0 s M', real=True)
u = sp.Matrix([
    -s*x/2 - Omega0*y/2 + M*z**2/2,
     Omega0*x/2 - s*y/2 - M*x*y,
     s*z + M*x*z,
])
vars_ = (x, y, z)
J = u.jacobian(vars_)
S = sp.simplify((J + J.T)/2)
div_u = sp.simplify(sp.trace(J))
omega = sp.Matrix([
    sp.diff(u[2], y) - sp.diff(u[1], z),
    sp.diff(u[0], z) - sp.diff(u[2], x),
    sp.diff(u[1], x) - sp.diff(u[0], y),
])
ez = sp.Matrix([0, 0, 1])
origin = {x: 0, y: 0, z: 0}
alpha0 = sp.simplify((ez.T*S*ez)[0].subs(origin))
strain_gradient_source = sp.simplify((sp.diff(S, z)*ez).subs(origin))

print('div u =', div_u)
print('curl u =', omega.T)
print('S =')
sp.pprint(S)
print('alpha(0) =', alpha0)
print('(e_z . grad S)e_z at 0 =', strain_gradient_source.T)
