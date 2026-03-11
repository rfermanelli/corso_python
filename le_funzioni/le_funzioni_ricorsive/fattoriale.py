# La funzione fattoriale(n) calcola il fattoriale di n chiamando se stessa.
def fattoriale(n):
    if n < 2:
        return 1
    else:
        return n * fattoriale(n - 1)

n = int(input("Inserire un numero naturale: "))
fattoriale_di_n = fattoriale(n)
print(f"Il fattoriale di {n} è:", fattoriale_di_n)
#
# Utilizzo di una funzione lambda per la chiamata alla funzione fattoriale(n).
print(f"Il fattoriale di {n} è: {(lambda fatt_n: fattoriale(n))(n)}")
