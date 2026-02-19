# Script import_from.py
from math_operations import addizione, moltiplicazione

somma = addizione(5, 3)  # Non serve math_operations.somma()
print(somma)  # Output: 8

prodotto = moltiplicazione(4, 2)
print(prodotto)  # Output: 8

# Questo causerebbe errore perché PI non è stato importato
# print(PI)  # NameError: name 'PI' is not defined




