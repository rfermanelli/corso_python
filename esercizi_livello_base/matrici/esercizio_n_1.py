"""
Esercizio n. 1 - Vettori linearmente indipendenti
Dati tre vettori u, v, w di dimensione n, si vuole determinare se sono linearmente indipendenti verificando se l'unica soluzione della combinazione lineare:
α·u + β·v + γ·w = 0
è quella banale α = β = γ = 0. Nel caso di tre vettori in ℝ³ (n=3), questo è equivalente a verificare che la matrice 3×3 formata dai tre vettori abbia determinante non nullo.
Scrivere un algoritmo, rappresentato tramite diagramma di flusso, che:
Acquisisca in input la dimensione n dei vettori.
Verifichi che la dimensione n sia valida (n = 3); in caso contrario, segnali in output un errore e termini.
Acquisisca in input le tre componenti dei tre vettori u, v, w.
Costruisca la matrice M = [u | v | w] affiancando i tre vettori come colonne.
Calcoli il determinante della matrice 3×3 con il metodo di Sarrus, usando un ciclo per i termini positivi e uno per i termini negativi, con un contatore termini_calcolati.
Conti quante componenti nulle sono presenti complessivamente nei tre vettori, tramite un contatore componenti_nulle.
Stampi in output il determinante, il numero di componenti nulle e un messaggio che informa se i vettori sono linearmente indipendenti (det ≠ 0) oppure linearmente dipendenti (det = 0).
"""

# Acquisizione e validazione della dimensione
n = int(input("Inserisci la dimensione n dei liste (deve essere 3): "))

if n != 3:
    print("Errore: questo metodo è applicabile solo per liste di dimensione 3.")
else:
    # Acquisizione dei tre liste
    vettori = []
    nomi = ["u", "v", "w"]
    for nome in nomi:
        vett = []
        print(f"\nInserisci le 3 componenti del vettore {nome}:")
        for i in range(3):
            componente = float(input(f"  {nome}[{i}] = "))
            vett.append(componente)
        vettori.append(vett)

    u = vettori[0]
    v = vettori[1]
    w = vettori[2]

    # Costruzione della matrice M = [u | v | w] per colonne
    M = []
    for i in range(3):
        riga = [u[i], v[i], w[i]]
        M.append(riga)

    # Calcolo del determinante con la regola di Sarrus
    # Termini positivi: diagonali principali
    termini_calcolati = 0
    det = 0.0

    for i in range(3):
        prodotto = 1.0
        for j in range(3):
            prodotto *= M[j][(i + j) % 3]
        det += prodotto
        termini_calcolati += 1

    # Termini negativi: diagonali secondarie
    for i in range(3):
        prodotto = 1.0
        for j in range(3):
            prodotto *= M[j][(i - j) % 3]
        det -= prodotto
        termini_calcolati += 1

    # Conteggio delle componenti nulle
    componenti_nulle = 0
    for vett in vettori:
        for i in range(3):
            if vett[i] == 0.0:
                componenti_nulle += 1

    # Output
    print(f"\nVettore u: {u}")
    print(f"Vettore v: {v}")
    print(f"Vettore w: {w}")
    print(f"\nMatrice M = [u | v | w]:")
    for riga in M:
        print(f"  {riga}")
    print(f"\nTermini calcolati (Sarrus): {termini_calcolati}")
    print(f"Componenti nulle totali:    {componenti_nulle} su 9")
    print(f"Determinante:               {det:.4f}")

    if det != 0.0:
        print("\nI tre liste sono LINEARMENTE INDIPENDENTI (det ≠ 0).")
    else:
        print("\nI tre liste sono LINEARMENTE DIPENDENTI (det = 0).")