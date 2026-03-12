messaggi = [
    "#Python è fantastico!",
    "Oggi studio Python",
    "#Coding è divertente",
    "Buongiorno a tutti!"
]

# Il metodo startwith() seleziona solo i messaggi che iniziano con #.
hashtag_messaggi = [m for m in messaggi if m.startswith("#")]
print("I messaggi che iniziano con l'hashtag sono:", hashtag_messaggi)
#
frasi = [
    "Python è fantastico!",
    "Oggi studio Python",
    "Coding è divertente!",
    "Buongiorno a tutti"
]

# Il metodo endwith() aggiunge un emoji solo alle frasi esclamative.
frasi_evidenziate = [f"🎉 {f}" if f.endswith("!") else f for f in frasi]
print("Le frasi escalmative sono quelle con l'emoji:", frasi_evidenziate)
