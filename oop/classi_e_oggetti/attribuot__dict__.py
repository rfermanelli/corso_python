"""
Il formato pascal case
Per convenzione l’identificatore di una classe è scritto con la lettera iniziale maiuscola
e, se è costituito da più parole, ogni parola inizia con una lettera maiuscola
ed è giustapposta alla parola che la precede e alla parola che la segue.
"""
class Elettrone:

    # Variabili di classe
    carica = -1
    massa = 9.109e-31

    # Metodo costruttore
    def __init__(self, velocita):
        # Variabili di istanza
        self.velocita = velocita

    # Comportamento dinamico
    def accelerazione(self, accelerazione):
        self.velocita = self.velocita + accelerazione

electro = Elettrone(4e10)

print(f"Il dizionario dell'oggetto electro è: {electro.__dict__}")
print(f"\nIl dizionario della classe Elettrone è: {Elettrone.__dict__}")