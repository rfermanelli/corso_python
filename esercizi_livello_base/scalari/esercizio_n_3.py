"""
Esercizio n. 3 - Il metodo di bisezione
Si vuole trovare, approssimativamente, uno zero di una funzione continua nell'intervallo [a, b], usando il metodo di bisezione. Si considera la funzione:
f(x) = x³ - 2x - 5
Scrivere un algoritmo, rappresentato tramite diagramma di flusso, che:
Acquisisca gli estremi dell'intervallo a e b (reali).
Verifichi che i valori siano validi, ovvero che a < b e che f(a) e f(b) abbiano segno opposto (condizione del teorema degli zeri); in caso contrario, segnali un errore e termini.
Acquisisca la tolleranza tol (es. 0.0001), che deve essere positiva.
Applichi il metodo di bisezione: ad ogni iterazione calcoli il punto medio:
 m = (a + b) / 2
valuti f(m)
aggiorni l'intervallo e incrementi un contatore iterazioni
Si fermi quando l'ampiezza dell'intervallo (b - a) è minore della tolleranza.
Stampi la radice approssimata, il valore della funzione in quel punto e il numero di iterazioni necessarie.
Stampi infine se la radice trovata ricade nella metà sinistra o destra dell'intervallo originale.

"""
# Definizione della funzione
def f(x):
    return x**3 - 2*x - 5

# Acquisizione dati
a = float(input("Inserisci l'estremo sinistro a: "))
b = float(input("Inserisci l'estremo destro b: "))

# Validazione intervallo
if a >= b:
    print("Errore: deve essere a < b.")
else:
    fa = f(a)
    fb = f(b)

    # Validazione teorema degli zeri
    if fa * fb >= 0:
        print("Errore: f(a) e f(b) devono avere segno opposto.")
    else:
        tol = float(input("Inserisci la tolleranza (es. 0.0001): "))

        # Validazione tolleranza
        if tol <= 0:
            print("Errore: la tolleranza deve essere positiva.")
        else:
            meta_orig = (a + b) / 2
            iterazioni = 0

            # Metodo di bisezione
            while (b - a) >= tol:
                m = (a + b) / 2
                fm = f(m)
                iterazioni += 1

                if fa * fm < 0:
                    b = m
                    fb = fm
                else:
                    a = m
                    fa = fm

            m = (a + b) / 2
            fm = f(m)

            # Output
            print(f"\nRadice approssimata:     {m:.6f}")
            print(f"Valore f(radice):        {fm:.6f}")
            print(f"Numero di iterazioni:    {iterazioni}")

            if m <= meta_orig:
                print(f"\nLa radice ricade nella metà SINISTRA dell'intervallo originale.")
            else:
                print(f"\nLa radice ricade nella metà DESTRA dell'intervallo originale.")