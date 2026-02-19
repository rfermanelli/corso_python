# 2.
# Scrivere una funzione che, dato in ingresso un numero intero,
# restituisca in uscita True se il numero è palindromo; False altrimenti,
# senza utilizzare la conversione in stringa.

# Inizializzazione:
numero = int(input("Inserisci un numero intero ---> "))
numero_cifre = 0
posizione = 1
numero_palindromo = 0

# Calcolo del numero di cifre costituenti il numero intero dato in ingresso:
n = numero
while n:
    numero_cifre = numero_cifre + 1
    n = int(n / 10)
else:
    print(f"Il numero intero dato in ingresso è costituito da {numero_cifre} cifre.")

# Calcolo del numero costituito dalle cifre invertite del numero intero dato in ingresso:
n = numero
while n:
    decimale = n / 10
    intero = n // 10
    cifra = int(round(decimale - intero, 1) * 10)
    numero_palindromo = numero_palindromo + cifra * 10 ** (numero_cifre - posizione)
    posizione = posizione + 1
    n = intero
else:
    print(f"Il numero intero costituito dalle cifre invertite del numero intero dato in ingresso è: {numero_palindromo}")
    if numero == numero_palindromo:
        print("True")
    else:
        print("False")