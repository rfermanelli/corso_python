import random

# Gioco: indovina il numero.
numero_segretissimo = random.randint(1, 10)

while True:
    try:
        guess = int(input("Indovina un numero tra 1 e 10: "))
        # Se il numero in input non appartiene all'intervallo [1, 10]
        # è sollevata una eccezione sull'asserzione.
        assert guess in range(1, 11)
    except ValueError as ve:
        print(f"Errore: {ve}")
        continue  # Ripeti il ciclo senza crashare
    except AssertionError:
        print(f"Errore sull'asserzione {guess} compreso tra 1 e 10.")
        continue  # Il gioco ricomincia.
    else:
        if guess == numero_segretissimo:
            print("Complimenti, hai indovinato!")
            break
        else:
            print("Riprova!")
