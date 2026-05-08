"""
Esercizio n. 2 - La tabella di verità di una rete combinatoria
Data una rete logica con n ingressi, si vuole costruire e analizzare la sua tabella della verità completa, rappresentata come matrice. La rete implementa la funzione booleana:
f(A, B, C) = (A AND B) OR (NOT A AND C)
Scrivere un algoritmo, rappresentato tramite diagramma di flusso, che:
Acquisisca in input il numero n di ingressi.
Verifichi che n sia valido (deve essere esattamente 3 per questa funzione); in caso contrario, segnali in output un errore e termini.
Costruisca la matrice della tabella della verità T di dimensione 2ⁿ × (n+1), dove le prime n colonne contengono tutte le combinazioni di ingresso e l'ultima colonna contiene il valore dell'uscita f.
Riempia la matrice riga per riga usando un ciclo sulle 2ⁿ combinazioni, estraendo ogni bit con le operazioni (riga >> (n-1-j)) & 1 e calcolando l'uscita.
Conti, tramite un contatore uno_in_uscita, quante righe producono in uscita 1 (mintermine) e con un contatore zero_in_uscita quante righe producono in uscita 0 (maxtermine).
Stampi in output la matrice completa, il numero di mintermini e il numero di maxtermini.
"""

# Acquisizione e validazione del numero di ingressi
n = int(input("Inserisci il numero di ingressi n (deve essere 3): "))

if n != 3:
    print("Errore: questa funzione booleana richiede esattamente 3 ingressi.")
else:
    righe = 2 ** n  # 8 righe per n=3

    # Costruzione della matrice della tabella della verità
    # t ha dimensione righe x (n+1): prime n colonne = ingressi, ultima = uscita
    t = []
    for i in range(righe):
        riga = []

        # Estrazione dei bit della combinazione i-esima
        for j in range(n):
            bit = (i >> (n - 1 - j)) & 1
            riga.append(bit)

        # Calcolo dell'uscita: f(a,b,c) = (a AND b) OR (NOT a AND c)
        a = riga[0]
        b = riga[1]
        c = riga[2]
        f = ((a & b) | ((1 - a) & c))
        riga.append(f)

        t.append(riga)

    # Conteggio dei mintermini e maxtermini
    uni_uscita = 0
    for i in range(righe):
        if t[i][n] == 1:
            uni_uscita += 1

    zero_uscita = righe - uni_uscita

    # Conteggio delle righe con tutti gli ingressi uguali
    righe_con_tutti_ingressi_uguali = 0
    for i in range(righe):
        tutti_uguali = True
        for j in range(1, n):
            if t[i][j] != t[i][0]:
                tutti_uguali = False
        if tutti_uguali:
            righe_con_tutti_ingressi_uguali += 1

    # Stampa della tabella della verità
    print("\n--- TABELLA DELLA VERITÀ ---")
    print(" a  b  c | f(a,b,c)")
    print("---------+---------")
    for i in range(righe):
        a = t[i][0]
        b = t[i][1]
        c = t[i][2]
        f = t[i][3]
        print(f" {a}  {b}  {c} |    {f}")

    # Output riassuntivo
    print(f"\nDimensione matrice t: {righe} righe x {n + 1} colonne")
    print(f"Mintermini (uscita 1): {uni_uscita} su {righe}")
    print(f"Maxtermini (uscita 0): {zero_uscita} su {righe}")
    print(f"Righe con tutti gli ingressi uguali: {righe_con_tutti_ingressi_uguali}")

    if uni_uscita > zero_uscita:
        print("\nLa funzione è prevalentemente ATTIVA (più mintermini che maxtermini).")
    elif uni_uscita < zero_uscita:
        print("\nLa funzione è prevalentemente INATTIVA (più maxtermini che mintermini).")
    else:
        print("\nLa funzione è BILANCIATA (ugual numero di mintermini e maxtermini).")