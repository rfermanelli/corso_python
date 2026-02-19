# 1.
# Scrivere una funzione che, dato in ingresso un numero intero,
# restituisca in uscita il numero delle cifre che lo costituiscono,
# senza utilizzare la conversione in una stringa.

# Inizializzazione:
numero_intero = int(input("Inserisci un numero intero ---> "))
numero_cifre_intero = 0

# Calcolo del numero delle cifre costituenti il numero intero dato in ingresso:
while numero_intero:
    numero_cifre_intero = numero_cifre_intero + 1
    numero_intero = int(numero_intero / 10)
else:
    if not numero_cifre_intero:
        print("Il numero intero inserito è costituito da", numero_cifre_intero + 1, "cifra.")
    else:
        print("Il numero intero inserito è costituito da", numero_cifre_intero, "cifre.")