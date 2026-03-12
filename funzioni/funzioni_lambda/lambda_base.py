# La definizione classica di una funzione
def raddoppia(x):
    return x * 2

# La definizione di una funzione lambda che è assegnata a una variabile:
raddoppia = lambda x: x ** 2

print(raddoppia(5))

# La funzione lambda utilizzata senza essere assegnata a una variabile:
print((lambda x: x ** 2)(5))

