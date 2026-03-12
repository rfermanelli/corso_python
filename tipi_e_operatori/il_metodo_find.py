testo = "Python è potente, veloce e super divertente!"

# Il metodo find() cerca la posizione della parola "veloce".
posizione = testo.find("veloce")
print("La posizione della parola 'veloce' nella frase è:", posizione)

# Evidenziamo la parola trovata con emoji
if posizione != -1:  # -1 significa che il metodo find() non ha trovato la parola da cercare.
    lunghezza = len("veloce")
    evidenziata = (
        testo[:posizione] + "⚡" + testo[posizione:posizione+lunghezza] + "⚡" + testo[posizione+lunghezza:]
    )
    print("La frase con la parola da cercare evidenziata:", evidenziata)
else:
    print("Parola non trovata!")

# Il metodo find() restitisce -1 se la parola da cercare in una stringa non esiste.
print(f"La posizione della parola 'lento' nella frase è: Non trovata {testo.find("lento")}")
