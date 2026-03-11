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

    def gravita_superficie(self) -> float:
        # Accelerazione gravitazionale alla superficie (m/s^2)
        return G * self.massa / self.raggio**2 * self.temperatura

    def velocita_fuga(self, spinta_gravitazionale) -> float:
        # Velocità di fuga (m/s)
        return math.sqrt(2 * G * self.massa / self.raggio * spinta_gravitazionale)

    def tipo(self) -> str:
        return "Stella"


# Istanza dell'oggetto di tipo Stella
star = Stella("Alpha", 2000, 1500000, 3000)
# Overriding del metodo velocita_fuga() del tipo CorpoCeleste
print(f"La velocità di fuga della stella {star.nome} è: {star.velocita_fuga(10e100)}")
# Overriding del metodo gravit_superficie del tipo CorpoCeleste
print(f"La gravità superficiale della stella {star.nome} è: {star.gravita_superficie()}")


