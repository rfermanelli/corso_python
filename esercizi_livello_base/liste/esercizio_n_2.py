"""
Esercizio n. 2 - Il sommatore binario a n bit
Dati due numeri rappresentati come vettori di n bit, si vuole calcolare la somma binaria bit a bit, gestendo il riporto (carry) ad ogni posizione, esattamente come fa un sommatore ripple-carry. Si vuole inoltre contare quante posizioni generano riporto e verificare se la somma produce overflow.
Scrivere un algoritmo, rappresentato tramite diagramma di flusso, che:
Acquisisca la dimensione n (numero di bit, intero positivo).
Verifichi che n sia valido (maggiore di zero); in caso contrario, segnali un errore e termini.
Acquisisca i due vettori A e B di n bit ciascuno, verificando che ogni elemento sia 0 oppure 1; in caso contrario, segnali un errore e termini.
Esegua la somma bit a bit dal bit meno significativo (indice n-1) al più significativo (indice 0), calcolando ad ogni posizione i la somma parziale s = A[i] + B[i] + carry, il bit risultante S[i] = s % 2 e il nuovo riporto carry = s // 2
Conti quante posizioni generano un riporto verso la posizione successiva, tramite un contatore posizioni_con_riporto.
Verifichi se al termine del ciclo il riporto finale è 1 (overflow: la somma non è rappresentabile con n bit).
Stampi i due vettori in input, il vettore risultante S, il numero di posizioni con riporto e se si è verificato overflow oppure no.
"""

# Acquisizione e validazione della dimensione
n = int(input("Inserisci il numero di bit n: "))

if n <= 0:
    print("Errore: n deve essere un intero positivo.")
else:
    # Acquisizione e validazione del vettore a
    a = []
    print(f"\nInserisci i {n} bit del vettore A (dal più significativo al meno significativo):")
    errore = False
    for i in range(n):
        bit = int(input(f"  a[{i}] = "))
        if bit != 0 and bit != 1:
            print("Errore: ogni bit deve essere 0 oppure 1.")
            errore = True
            break
        a.append(bit)

    if not errore:
        # Acquisizione e validazione del vettore b
        b = []
        print(f"\nInserisci i {n} bit del vettore B (dal più significativo al meno significativo):")
        for i in range(n):
            bit = int(input(f"  b[{i}] = "))
            if bit != 0 and bit != 1:
                print("Errore: ogni bit deve essere 0 oppure 1.")
                errore = True
                break
            b.append(bit)

    if not errore:
        # Somma bit a bit dal bit meno significativo al più significativo
        S = [0] * n
        carry = 0
        posizioni_con_riporto = 0

        for i in range(n - 1, -1, -1):
            s = a[i] + b[i] + carry
            S[i] = s % 2
            carry = s // 2
            if carry == 1:
                posizioni_con_riporto += 1

        # Conversione in decimale per verifica
        val_a = 0
        val_b = 0
        val_S = 0
        for i in range(n):
            val_a += a[i] * (2 ** (n - 1 - i))
            val_b += b[i] * (2 ** (n - 1 - i))
            val_S += S[i] * (2 ** (n - 1 - i))

        # Output
        print(f"\nVettore A:  {''.join(str(b) for b in a)}  (decimale: {val_a})")
        print(f"Vettore B:  {''.join(str(b) for b in b)}  (decimale: {val_b})")
        print(f"Somma   S:  {''.join(str(b) for b in S)}  (decimale: {val_S})")
        print(f"\nPosizioni con riporto generato: {posizioni_con_riporto} su {n}")

        if carry == 1:
            print(f"\nOVERFLOW: la somma {val_a} + {val_b} = {val_a + val_b} "
                  f"non è rappresentabile con {n} bit.")
        else:
            print(f"\nNessun overflow: la somma è correttamente rappresentata con {n} bit.")