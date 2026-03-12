testo = "Python è potente, veloce e super divertente!"

# Il metodo replace() sostituisce le parole con un'emoji
testo_fico = testo.replace("potente", "💪 potente").replace("divertente", "😄 divertente")

print("Testo trasformato:", testo_fico)

# Il metodo replace() può essere utilizzato per fare sostituzioni multiple dinamicamente.
sostituzioni = {"Python": "🐍 Python", "veloce": "⚡ veloce"}

for chiave, valore in sostituzioni.items():
    testo_cool = testo_fico.replace(chiave, valore)

print("Testo finale super cool:", testo_cool)
