"""
Se due moduli hanno un attributo con lo stesso identificatore
allora si produce un conflitto di nomi e il nome importato per secondo
sostituirà quella importato per primo (disambiguazione).
"""
# Definizione delle funzioni addizione(a, b) e moltiplicazione(a, b)
# del modulo import_from_as.py
def addizione(a, b):
    return f"{a} + {b}"

def moltiplicazione(a, b):
    return f"{a} * {b}"

# Import delle funzioni addizione(a, b) e moltiplicazione(a, b)
# del modulo math_operations.py
# from math_operations import addizione, moltiplicazione
# L'aliasing risolve i casi di overriding (sovrapposizione).
from math_operations import addizione as add, moltiplicazione as mul

somma = add(5, 3)  # Non serve math_operations.addizione()
print(somma)  # Output: 8

prodotto = mul(4, 2) # Non serve math_operations.moltiplicazione()
print(prodotto)  # Output: 8


