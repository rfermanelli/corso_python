# Una frase da analizzare.
frase = "Python è potente, veloce e super divertente!"

# Il metodo split() divide la frase nelle sue singole parole.
parole = frase.split()  # di default divide dove ci sono gli spazi.
print("Lista delle singole parole della frase:", parole)

# Il metodo split() divide  la frase utilizzando come separatore il carattere ','.
frase = "Python,Java,C++, CSS e JavaScript"
linguaggi = frase.split(",")
print("Lista dei nomi dei linguaggi della frase:", linguaggi)



