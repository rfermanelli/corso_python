x = 0.1
y = 0.2
z = x + y
print("La somma dei numeri float 0.1 e 0.2 è:", z)

"""
La funzione abs() stabilisce un criterio di tolleranza, ossia:
la differenza tra i due numeri 0.1 + 0.2 e 0.3 (che dovrebbe essere il risultato esatto
della addizione 0.1 + 0.2) è abbastanza piccola da poter essere tollerata? 
"""
if abs(z - 0.3) < 1e-9:
    print(abs(z - 0.3))
