"""
Il formato pascal case
Per convenzione l’identificatore di una classe è scritto con la lettera iniziale maiuscola
e, se è costituito da più parole, ogni parola inizia con una lettera maiuscola
ed è giustapposta alla parola che la precede e alla parola che la segue.
"""
class Elettrone:

    # Variabili di classe
    __carica = -1
    massa = 9.109e-31

    # Metodo costruttore
    def __init__(self, velocita):
        # Variabili di istanza
        self.velocita = velocita

    # Comportamento dinamico
    def accelerazione(self, accelerazione):
        self.velocita = self.velocita + accelerazione

e_1 = Elettrone(5e4)

print(f"\nLa carica dell'elettrone e_1 è: {e_1.carica}")
# Una variabile privata è accessibile utilizzando la tecnica del name mangling
print(f"La carica dell'elettrone e_1 è: {e_1._Elettrone__carica}")