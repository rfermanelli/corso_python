# 1) Utilizzo del generatore yield con la funzione next():
def generatore_():
    for i in ["a", "b", "c", "d", "e", "f"]:
        print(f"Generato: {i}")
        yield i
# Controllo della fine della iterazione:
try:
    gen = generatore_()
    while gen:
        print(next(gen))
except StopIteration:
    print("Fine iterazione")

# 2) Utilizzo del generatore yield senza la funzione next()
def generatore_numeri():
    for i in range(5):
        yield i

for gen in generatore_numeri():
    print(gen, end=" ")



