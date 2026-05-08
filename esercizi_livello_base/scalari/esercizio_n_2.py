"""
Esercizio n. 2 - Il tiro verticale
Un corpo c viene lanciato verticalmente verso l'alto con una certa velocità iniziale v0. Si analizzi il moto e si determini se l'oggetto supera una quota soglia prefissata.
Scrivere un algoritmo, rappresentato tramite diagramma di flusso, che:
Acquisisca in input la velocità iniziale v0 del corpo c (in m/s).
Acquisisca in input la quota soglia h_soglia (in metri).
Verifichi che sia la velocità iniziale v0 sia la quota soglia h_soglia siano valide (devono essere > 0); in caso contrario, segnali in output un errore e termini.
Calcoli la quota massima raggiunta dall'oggetto, usando la formula:
h_max = v0² / (2g) con g = 9.81 m/s²
Calcoli il tempo per raggiungere la quota massima:
t_max = v0 / g
Simuli il moto secondo per secondo da t = 0 fino a t_max, calcolando ad ogni istante la quota (legge oraria del moto uniformemente accelerato):
h(t) = v0·t - ½·g·t²
e conti quanti istanti la quota supera h_soglia
Stampi in output la quota massima, il tempo per raggiungerla, i secondi trascorsi sopra la soglia e infine un messaggio che informa se l'oggetto supera o meno la quota soglia.
"""

import math

g = 9.81  # m/s²

# Acquisizione dati
v0 = float(input("Inserisci la velocità iniziale v0 (m/s): "))
h_soglia = float(input("Inserisci la quota soglia (m): "))

# Validazione
if v0 <= 0 or h_soglia <= 0:
    print("Errore: i valori devono essere positivi.")
else:
    # Calcolo quota massima e tempo di vetta
    h_max = (v0 ** 2) / (2 * g)
    t_max = v0 / g

    # Simulazione secondo per secondo
    istanti_sopra = 0
    t = 0.0
    while t <= t_max:
        h = v0 * t - 0.5 * g * t ** 2
        if h > h_soglia:
            istanti_sopra += 1
        t += 1.0

    # Output
    print(f"\nQuota massima raggiunta: {h_max:.2f} m")
    print(f"Tempo per raggiungere la vetta: {t_max:.2f} s")
    print(f"Istanti (interi) trascorsi sopra la soglia: {istanti_sopra}")

    if h_max > h_soglia:
        print(f"\nL'oggetto SUPERA la quota soglia di {h_soglia:.2f} m.")
    else:
        print(f"\nL'oggetto NON supera la quota soglia di {h_soglia:.2f} m.")