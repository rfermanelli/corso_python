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

    # Comportamento
    def accelerazione(self, accelerazione):
        self.velocita = self.velocita + accelerazione

# Istanze di due oggetti di tipo Elettrone
e_1 = Elettrone(0)
e_2 = Elettrone(10e5)

print(f"\nLa massa dell'elettrone e_1 a riposo è pari a: {e_1.massa} chilogrammi")
print(f"La carica dell'elettrone e_1 è: {e_1.carica} \n")

print(f"La massa dell'elettrone e_2 a riposo è pari a: {e_2.massa} chilogrammi")
print(f"La carica dell'elettrone e_2 è: {e_2.carica} \n")

e_1.accelerazione(1e5)

print(f"La velocità dell'elettrone e_1 è di: {e_1.velocita} chilometri al secondo \n")

e_2.accelerazione(1e5)

print(f"La velocità dell'elettrone e_2 è di: {e_2.velocita} chilometri al secondo!!! \n")

# La variabile di classe 'carica' è modificata solo per l'oggetto e_2
e_2.carica = +1

print(f"La carica dell'elettrone e_1 è: {e_1.carica}")
print(f"La carica dell'elettrone e_2 è: {e_2.carica}")