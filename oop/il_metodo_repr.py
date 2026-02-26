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


    # Metodo di presentazione dell'oggetto che opera un override del metodo __str__()
    def __repr__(self):
        return f"\nL'elettrone e ha una velocita di: {self.velocita} chilometri al secondo"


e = Elettrone(2.5e5)
print(e)
