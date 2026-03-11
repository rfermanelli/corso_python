from abc import ABC, abstractmethod
import math

# Costanti fisiche (CODATA)
G = 6.67430e-11         # Costante gravitazionale (m^3 kg^-1 s^-2)
c = 299_792_458         # Velocità della luce (m/s)
sigma = 5.670374419e-8  # Costante di Stefan-Boltzmann (W m^-2 K^-4)

# Classe astratta base
class CorpoCeleste(ABC):
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


# Classe derivata: Stella
class Stella(CorpoCeleste):
    def __init__(self, nome: str, massa: float, raggio: float, temperatura: float):
        super().__init__(nome, massa, raggio)
        self.temperatura = temperatura  # K

    def luminosita(self) -> float:
        """
        Legge di Stefan-Boltzmann:
        L = 4πR^2 σT^4
        """
        return 4 * math.pi * self.raggio**2 * sigma * self.temperatura**4

    def tipo(self) -> str:
        return "Stella"


# Classe derivata: Pianeta
class Pianeta(CorpoCeleste):
    def __init__(self, nome: str, massa: float, raggio: float, periodo_orbitale: float):
        super().__init__(nome, massa, raggio)
        self.periodo_orbitale = periodo_orbitale  # secondi

    def velocita_orbitale_media(self, r_orbita: float) -> float:
        """
        v = sqrt(GM / r)
        (approssimazione orbita circolare attorno a corpo molto più massivo)
        """
        return math.sqrt(G * self.massa / r_orbita)

    def tipo(self) -> str:
        return "Pianeta"


# Classe derivata: BucoNero
class BucoNero(CorpoCeleste):
    def __init__(self, nome: str, massa: float):
        # Il raggio iniziale è calcolato come raggio di Schwarzschild
        r_s = 2 * G * massa / c**2
        super().__init__(nome, massa, r_s)

    def raggio_schwarzschild(self) -> float:
        return self.raggio

    def tipo(self) -> str:
        return "Buco Nero"


# Esempio reale

# Dati fisici reali
sole = Stella(
    nome="Sole",
    massa=1.98847e30,
    raggio=6.9634e8,
    temperatura=5778
)

terra = Pianeta(
    nome="Terra",
    massa=5.9722e24,
    raggio=6.371e6,
    periodo_orbitale=365.25 * 24 * 3600
)

print("\nLa luminosità del Sole è:", sole.luminosita(), "W \n")
print("La gravità della Terra è:", terra.gravita_superficie(), "m/s^2 \n")
print("La velocità di fuga della Terra è:", terra.velocita_fuga(), "m/s")