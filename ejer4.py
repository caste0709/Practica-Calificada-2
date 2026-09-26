def f_vdw(v, P, T, a, b, R=8.314):
    return P*v**3 - (P*b + R*T)*v**2 + a*v - a*b

def secante(f, v0, v1, tol=1e-8, maxit=200):
    for i in range(maxit):
        f0, f1 = f(v0), f(v1)
        v2 = v1 - f1*(v1 - v0)/(f1 - f0)
        if abs(f(v2)) < tol:
            return v2, i+1, abs(f(v2))
        v0, v1 = v1, v2
    return v2, maxit, abs(f(v2))

a, b, T, P, R = 0.5536, 3.049e-5, 500, 2.63e6, 8.314
Tc = 8*a/(27*R*b)
print(f"Tc = {Tc:.2f} K -> subcrítico: {T < Tc}")

f = lambda v: f_vdw(v, P, T, a, b, R)
vl, nl, resl = secante(f, 1.1*b, 1.2*b)
v0g, v1g = R*T/P, 0.9*R*T/P
vg, ng, resg = secante(f, v0g, v1g)

print(f"{'Fase':10s}{'raiz (m3/mol)':>16s}{'iters':>8s}{'residuo':>12s}")
print(f"{'Líquida':10s}{vl:16.6e}{nl:8d}{resl:12.2e}")
print(f"{'Gaseosa':10s}{vg:16.6e}{ng:8d}{resg:12.2e}")