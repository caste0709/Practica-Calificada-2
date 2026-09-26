R, P, T, b = 8.314, 5.0e6, 273.15, 3.87e-5
v_ideal = R*T/P
print(f"v_ideal = {v_ideal:.6e} m^3/mol")
print(f"v0 > b -> {v_ideal > b}  (v0/b = {v_ideal/b:.3f})")