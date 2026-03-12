testo = "Python è potente e divertente"

# Il metodo maketrans() crea la tabella di traduzione.
tabella = str.maketrans({
    "a": "4",
    "e": "3",
    "i": "1",
    "o": "0",
    "P": "🐍",
})

# Il metodo translate() applica la trasformazione.
testo_hacker = testo.translate(tabella)

print(testo_hacker)
