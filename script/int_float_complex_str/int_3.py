# 3.
# Scrivere una funzione che, dato in ingresso un numero intero:
#   a. Verifichi che sia un numero perfetto;
#   b. Restituisca la somma dei suoi divisori propri.

# Inizializzazione:
n = int(input("Inserisci un numero intero ---> "))
somma_dei_divisori = 0

# Calcolo della somma dei divisori propri del numero intero dato in ingresso:
for divisore in range(1, n):
    if n % divisore == 0:
        somma_dei_divisori = somma_dei_divisori + divisore
else:
    if somma_dei_divisori == n:
        print(f"Il numero dato in ingresso: {n} è perfetto poiché è uguale alla somma dei suoi divisori: {somma_dei_divisori}")
    else:
        print(
            f"Il numero dato in ingresso: {n} non è perfetto poiché non è uguale alla somma dei suoi divisori: {somma_dei_divisori}")
