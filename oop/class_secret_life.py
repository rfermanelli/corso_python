from abc import ABC, abstractmethod
import math

# Costanti fisiche (CODATA)
G = 6.67430e-11         # Costante gravitazionale (m^3 kg^-1 s^-2)
c = 299_792_458         # Velocità della luce (m/s)
sigma = 5.670374419e-8  # Costante di Stefan-Boltzmann (W m^-2 K^-4)

# Classe astratta base
class CorpoCeleste(ABC):
    # Questa classe è utilizzata a scopo esemplificativo.
    """Questo è il commento che valorizza la variabile __doc__"""
    def __init__(self, nome: str, massa: float, raggio: float):
        self.nome = nome
        self.massa = massa      # kg
        self.raggio = raggio    # m

    def gravita_superficie(self) -> float:
        # Accelerazione gravitazionale alla superficie (m/s^2)
        return G * self.massa / self.raggio**2

    def velocita_fuga(self) -> float:
        # Velocità di fuga (m/s)
        return math.sqrt(2 * G * self.massa / self.raggio)

    @abstractmethod
    def tipo(self) -> str:
        pass


"""
__dict__ contiene il dizionario delle proprietà delle classi e dei metodi.
__name__ contiene il nome della classe.
__module__ contiene il nome del modulo che contiene la definizione di classe.
__qualname__ (qualified name) contiene il nome completo qualificato, cioè il nome che include anche il contesto in cui è definita.
__doc__ contiene la docstring, cioè la stringa di documentazione associata.
__bases__ contiene il nome delle classi che sono superclassi della classe. 
__annotations__ contiene le annotazioni di tipo associate a variabili, parametri di funzione e valori di ritorno.
"""
print(f"1)"f"{CorpoCeleste.__dict__}")
print(f"2)"f"{CorpoCeleste.__name__}")
print(f"3)"f"{CorpoCeleste.__module__}")
print(f"4)"f"{CorpoCeleste.__qualname__}")
print(f"5)"f"{CorpoCeleste.__doc__}")
print(f"6)"f"{CorpoCeleste.__bases__}")
print(f"7)"f"{CorpoCeleste.__annotations__}")
print(f"8)"f"{CorpoCeleste.__dict__.keys()}")
print(f"9)"f"{CorpoCeleste.__dict__.values()}")
print(f"10)"f"{CorpoCeleste.__dict__.items()}")



