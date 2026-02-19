# Una list comprehension che applica una funzione lambda:
numeri = [1, 2, 3, 4, 5]
risultato = [(lambda x: x ** 2)(x) for x in numeri]

print(risultato)

# Una list comprehension classica, priva di una funzione lambda:
risultato = [x ** 2 for x in numeri]

print(risultato)