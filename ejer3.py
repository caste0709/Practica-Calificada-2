import sympy as sp
v, P, b, R, T, a = sp.symbols('v P b R T a', positive=True)
f = P*v**3 - (P*b + R*T)*v**2 + a*v - a*b
fp, fpp = sp.diff(f, v), sp.diff(f, v, 2)
print("f'(v) =", fp); print("f''(v) =", fpp)

vals = {P:1.0e6, T:300, R:8.314, a:0.3640, b:4.267e-5}
v_star = 2.3811e-3
fp_n  = float(fp.subs(vals).subs(v, v_star))
fpp_n = float(fpp.subs(vals).subs(v, v_star))
M = abs(fpp_n)/(2*abs(fp_n))
print(f"f'(v*)={fp_n:.4f}  f''(v*)={fpp_n:.4f}  M={M:.4f}")