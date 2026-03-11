from abc import ABC, abstractmethod
import math

# Costanti fisiche (SI)
G = 6.67430e-11
sigma = 5.670374419e-8


# Livello 1: Oggetto fisico generico
class OggettoFisico(ABC):
    def __init__(self, massa: float):
        self.massa = massa  # kg

    def energia_riposo(self) -> float:
        # E = mc^2
        c = 299_792_458
        return self.massa * c**2

    @abstractmethod
    def descrizione(self) -> str:
        pass


# Livello 2: Corpo celeste
class CorpoCeleste(OggettoFisico):
    def __init__(self, nome: str, massa: float, raggio: float):
        super().__init__(massa)
        self.nome = nome
        self.raggio = raggio  # m

    def gravita_superficie(self) -> float:
        return G * self.massa / self.raggio**2

    def descrizione(self) -> str:
        return f"{self.nome} è un corpo celeste."


# Livello 3: Stella
class Stella(CorpoCeleste):
    def __init__(self, nome: str, massa: float, raggio: float, temperatura: float):
        super().__init__(nome, massa, raggio)
        self.temperatura = temperatura  # K

    def luminosita(self) -> float:
        # Legge di Stefan-Boltzmann
        return 4 * math.pi * self.raggio**2 * sigma * self.temperatura**4

    def descrizione(self) -> str:
        return f"{self.nome} è una stella con T = {self.temperatura} K."


# Livello 4: Gigante Rossa
class GiganteRossa(Stella):
    def __init__(self, nome: str, massa: float, raggio: float, temperatura: float, perdita_massa: float):
        super().__init__(nome, massa, raggio, temperatura)
        self.perdita_massa = perdita_massa  # kg/s

    def tasso_espansione(self) -> float:
        # Modello semplificato proporzionale alla perdita di massa
        return self.perdita_massa / self.massa

    def descrizione(self) -> str:
        return f"{self.nome} è una gigante rossa con forte perdita di massa."


# Esempio reale
# Parametri approssimativi di Betelgeuse
betelgeuse = GiganteRossa(
    nome="Betelgeuse",
    massa=1.64e31,
    raggio=6.0e11,
    temperatura=3500,
    perdita_massa=1e19
)

print(f"\n{betelgeuse.descrizione()}")
print("\nLa luminosità di betelgeuse è:", betelgeuse.luminosita(), "W\n")
print("La gravità superficiale di betelgeuse è:", betelgeuse.gravita_superficie(), "m/s^2\n")
print("L'energia di riposo di betelgeuse è:", betelgeuse.energia_riposo(), "J")