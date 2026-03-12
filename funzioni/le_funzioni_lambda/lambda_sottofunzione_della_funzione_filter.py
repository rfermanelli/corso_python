"""
La funzione filter() applica una funzione a ogni elemento di un oggetto iterabile
e restituisce l'elemento se e solo se la funzione a esso applicata restituisce True.
"""

numeri = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# La funzione lambda come argomento della funzione filter:
pari = list(filter(lambda x: x % 2 == 0, numeri))

print(pari)
