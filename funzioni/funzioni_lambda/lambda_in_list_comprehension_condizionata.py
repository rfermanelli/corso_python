# La funzione lambda in una list comprehension condizionata:
numeri = [1, 2, 3, 4, 5]
risultato = [(lambda x: x * 2 if x % 2 == 0 else x * 3)(x) for x in numeri]

print(risultato)