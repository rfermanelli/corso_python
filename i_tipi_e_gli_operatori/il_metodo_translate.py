testo = "Python!!! è??? potente... e divertente!!!"

# 1) Il metodo maketrans() crea una tabella per:
# - la sostituzione delle vocali;
# - la rimozoone dei caratteri di punteggiatura.
tabella = str.maketrans(
    "aeiou",
    "43100",
    "!?."        # caratteri da rimuovere.
)

# 2) Applicazione del metodo translate()
testo_pulito = testo.translate(tabella)

print(testo_pulito)
