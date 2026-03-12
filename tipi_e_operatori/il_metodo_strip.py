# Frase con spazi e simboli strani ai bordi.
frase = "   ✨✨Python è magico!✨✨   "

# Il metodo strip() rimuove solo gli spazi all'inizio e alla fine della frase.
solo_spazi = frase.strip()
print("La frase senza gli spazi iniziali e finali è:", solo_spazi)

# Il metodo strip() rimuove gli spazi all'inizio e alla fine della frase e i simboli specifici ✨.
pulita = frase.strip(" ✨")
print("La frase senza gli spazi iniziali e finali e i simboli è:", pulita)

