"""
La funzione map() applica una funzione a ogni elemento di un oggetto iterabile
e restituisce un iteratore con i risultati ottenuti.

La funzione enumerate() applicata a un oggetto iterabile
restituisce sia l’indice sia il valore di ogni elemento.
"""

numeri = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# La funzione lambda come argomento della funzione map all'interno di una list comprehension:
quadrati = list(map(lambda x: x ** 2, numeri))

print(quadrati)

# La funzione lambda come argomento della funzione map all'interno di una set comprehension:
enumerazione = set(map(lambda x: x, enumerate(numeri)))

print(enumerazione)