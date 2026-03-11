# La funzione somma_naturali(n) calcola la somma
# dei primi n numeri naturali.
def somma_naturali(n):
    if n == 1:
        return 1
    else:
        return n + somma_naturali(n - 1)

n = int(input("Inserire un numero naturale: "))
somma_dei_naturali = somma_naturali(n)
print(f"La somma dei primi {n} naturali è: {somma_dei_naturali}")
#
# Utilizzo di una funzione lambda per la chiamata alla funzione fattoriale(n).
print(f"La somma dei primi {n} naturali è: {(lambda somma_n: somma_naturali(n))(n)}")
