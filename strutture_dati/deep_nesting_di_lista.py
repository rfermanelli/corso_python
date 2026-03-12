import copy

# Lista di partenza
a = [[1, 2], [3, 4]]

# Copia profonda
b = copy.deepcopy(a)

# Modifica di una sottolista
a[0].append(99)

print("a = ", a)
print("b = ", b)