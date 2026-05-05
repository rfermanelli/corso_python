"""
Esercizio n. 1 - Il dado truccato
Un dado a sei facce viene lanciato due volte. Si determini se la somma dei due risultati è maggiore di 8.
Scrivere un algoritmo, rappresentato tramite diagramma di flusso, che:
Acquisisca il risultato del primo lancio (un intero tra 1 e 6).
Acquisisca il risultato del secondo lancio (un intero tra 1 e 6).
Verifichi che entrambi i valori siano validi (compresi tra 1 e 6); in caso contrario, segnali un errore e termini.
Calcoli la somma dei due risultati.
Determini e stampi quante delle 36 combinazioni possibili producono una somma maggiore di 8 (suggerimento: si usino due contatori e due cicli annidati).
Calcoli e stampi la probabilità (in percentuale) che la somma superi 8, come rapporto tra i casi favorevoli e i 36 casi totali.
Stampi infine se la coppia di valori inserita dall'utente è un caso favorevole.

"""

# Acquisizione e validazione dei lanci
lancio1 = int(input("Inserisci il risultato del primo lancio (1-6): "))
lancio2 = int(input("Inserisci il risultato del secondo lancio (1-6): "))

# Validazione
if lancio1 < 1 or lancio1 > 6 or lancio2 < 1 or lancio2 > 6:
    print("Errore: i valori devono essere compresi tra 1 e 6.")
else:
    # Calcolo della somma
    somma = lancio1 + lancio2

    # Conteggio dei casi favorevoli (somma > 8)
    favorevoli = 0
    for i in range(1, 7):
        for j in range(1, 7):
            if i + j > 8:
                favorevoli += 1

    # Calcolo della probabilità
    probabilita = (favorevoli / 36) * 100

    # Output
    print(f"\nCasi favorevoli (somma > 8): {favorevoli} su 36")
    print(f"Probabilità: {probabilita:.2f}%")

    if somma > 8:
        print(f"\nLa tua coppia ({lancio1}, {lancio2}) con somma {somma} è un CASO FAVOREVOLE.")
    else:
        print(f"\nLa tua coppia ({lancio1}, {lancio2}) con somma {somma} NON è un caso favorevole.")