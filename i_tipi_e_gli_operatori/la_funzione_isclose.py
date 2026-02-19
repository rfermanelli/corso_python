import math

x = 0.1
y = 0.2
z = x + y
print("La somma dei numeri float 0.1 e 0.2 è:", z)

"""
La funzione isclose() del modulo math verifica se i due numeri sono sufficientemente vicini
in funzione degli errori di approssimazione.
Utilizza la funzione abs(). 
La funzione math.isclose(x, y, rel_tol=1e-09, abs_tol=0.0) è True se:
abs(x - y) <= max(rel_tol * max(abs(x), abs(y)), abs_tol)
"""
if math.isclose(x, y, rel_tol=1e-9, abs_tol=0.0):
    print(math.isclose(x, y, rel_tol=1e-09, abs_tol=0.0))
