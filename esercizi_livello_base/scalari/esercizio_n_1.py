"""
Esercizio n. 1 - Il dado truccato
Un dado a sei facce viene lanciato due volte. Si determini se la somma dei due risultati è maggiore di 8.
Scrivere un algoritmo, rappresentato tramite diagramma di flusso, che:
Acquisisca in input il risultato del primo lancio del dado.
Acquisisca in input il risultato del secondo lancio del dado.
Verifichi che i risultati dei due lanci del dado siano validi (devono essere numeri interi compresi  tra 1 e 6); in caso contrario, segnali in output un errore e termini.
Calcoli la somma dei risultati dei due lanci del dado.
Determini e stampi in output il numero delle combinazioni dei due lanci del dado (delle 36 combinazioni possibili) che producono una somma maggiore di 8 (suggerimento: si usino due contatori e due cicli annidati).
Calcoli e stampi in output la probabilità (in percentuale) che la somma dei risultati dei due lanci del dado superi 8 (suggerimento: è il rapporto tra il numero dei casi favorevoli calcolati al punto 5) e i 36 casi totali moltiplicato per 100).
Stampi infine un messaggio che informi sul tipo della combinazione dei due lanci del dado: combinazione favorevole (la somma dei risultati è > 8); combinazione sfavorevole (la somma dei risultati è <= 8).
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