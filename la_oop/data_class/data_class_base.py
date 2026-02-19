from dataclasses import dataclass

# Definizione di @dataclass
@dataclass
class Persona:
    nome: str
    cognome: str
    eta: int = 0  # Valore di default

# Istanza di @dataclass (configurazione iniziale con il metodo __init__()).
persona_1 = Persona("Mario", "Rossi", 30)
persona_2 = Persona("Luigi", "Bianchi", 28)

#
print(repr(persona_1))
print(persona_1 == persona_2)
