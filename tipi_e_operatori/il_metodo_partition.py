testo = "Python è potente, veloce e super divertente!"

# Il metodo partition() divide le parole della frase alla prima virgola.
prima, separatore, dopo = testo.partition(",")

print("Le parole della frase prima del separatore sono:", prima)
print("Il separatore utilizzato è:", separatore)
print("Le parole della frase dopo il separatore sono:", dopo)

