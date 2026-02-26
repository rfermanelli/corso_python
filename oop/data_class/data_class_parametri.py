from dataclasses import dataclass
#
# @dataclass con l'impostazione esplcita di parametri di configurazione: repr=True

@dataclass(init=True, repr=True, eq=True, order=False, frozen=False)
class Configurazione:
    """Classi con diversi parametri di configurazione"""
    # init=True: genera __init__
    # repr=True: genera __repr__
    # eq=True: genera __eq__
    # order=False: non genera metodi di confronto
    # frozen=False: l'istanza è mutabile
    nome: str
    valore: int = 100

c = Configurazione("Alan Ford", 1)
print(print(f"La stringa di presentazione dell'oggetto c di tipo Configurazione (repr=True) è: {repr(c)}"))

#
# @dataclass con l'impostazione esplcita di parametri di configurazione: repr=False

@dataclass(init=True, repr=False, eq=True, order=False, frozen=False)
class Config:
    """Classi con diversi parametri di configurazione"""
    # init=True: genera __init__
    # repr=True: genera __repr__
    # eq=True: genera __eq__
    # order=False: non genera metodi di confronto
    # frozen=False: l'istanza è mutabile
    nome: str
    valore: int = 100

c = Config("Bob Rock")
print(f"La stringa di presentazione dell'oggetto c di tipo Config (repr=False) è: {repr(c)}")

# @dataclass con l'impostazione esplcita di parametri di configurazione aventi diverse configurazioni:

@dataclass(order=True)
class PuntoOrdinato:
    x: int
    y: int

@dataclass(frozen=True)
class PuntoImmutable:
    x: int
    y: int

p1 = PuntoOrdinato(1, 2)
p2 = PuntoOrdinato(3, 4)
print(p1 < p2)  # True - perché order=True

p_imm = PuntoImmutable(5, 6) #p_imm.x = 10  # Errore! frozen=True