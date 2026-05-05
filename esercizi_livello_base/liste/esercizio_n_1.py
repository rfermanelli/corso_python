"""
Esercizio n. 1 - Il prodotto scalare
Dati due liste u e v di dimensione n, si vuole calcolare il loro prodotto scalare e determinare se i due liste sono ortogonali, ovvero se il prodotto scalare è zero. Si vuole inoltre trovare quante componenti hanno lo stesso segno nei due liste.
Scrivere un algoritmo, rappresentato tramite diagramma di flusso, che:
Acquisisca la dimensione n del vettore (intero positivo).
Verifichi che n sia valido (maggiore di zero); in caso contrario, segnali un errore e termini.
Acquisisca le n componenti del vettore u e le n componenti del vettore v.
Calcoli il prodotto scalare
ps = u[0]·v[0] + u[1]·v[1] + ... + u[n-1]·v[n-1]
Conti quante componenti di indice i che soddisfano la condizione: u[i] e v[i] hanno lo stesso segno (entrambe positive o entrambe negative), usando un contatore concordi.
Calcoli la norma (lunghezza) di ciascun vettore:
‖u‖ = √(u[0]² + ... + u[n-1]²)
‖v‖ = √(v[0]² + ... + v[n-1]²)
Stampi il prodotto scalare, le due norme, il numero di componenti concordi e determini se i due liste sono ortogonali oppure no

"""
import math

# Acquisizione e validazione della dimensione
n = int(input("Inserisci la dimensione n dei liste: "))

if n <= 0:
    print("Errore: n deve essere un intero positivo.")
else:
    # Acquisizione del vettore u
    u = []
    print(f"\nInserisci le {n} componenti del vettore u:")
    for i in range(n):
        componente = float(input(f"  u[{i}] = "))
        u.append(componente)

    # Acquisizione del vettore v
    v = []
    print(f"\nInserisci le {n} componenti del vettore v:")
    for i in range(n):
        componente = float(input(f"  v[{i}] = "))
        v.append(componente)

    # Calcolo del prodotto scalare
    ps = 0.0
    for i in range(n):
        ps += u[i] * v[i]

    # Conteggio delle componenti concordi
    concordi = 0
    for i in range(n):
        if (u[i] > 0 and v[i] > 0) or (u[i] < 0 and v[i] < 0):
            concordi += 1

    # Calcolo delle norme
    somma_u = 0.0
    somma_v = 0.0
    for i in range(n):
        somma_u += u[i] ** 2
        somma_v += v[i] ** 2
    norma_u = math.sqrt(somma_u)
    norma_v = math.sqrt(somma_v)

    # Output
    print(f"\nVettore u: {u}")
    print(f"Vettore v: {v}")
    print(f"\nProdotto scalare u·v:    {ps:.4f}")
    print(f"Norma di u ‖u‖:          {norma_u:.4f}")
    print(f"Norma di v ‖v‖:          {norma_v:.4f}")
    print(f"Componenti concordi:     {concordi} su {n}")

    if ps == 0.0:
        print("\nI due liste sono ORTOGONALI (prodotto scalare nullo).")
    else:
        print(f"\nI due liste NON sono ortogonali (prodotto scalare = {ps:.4f}).")