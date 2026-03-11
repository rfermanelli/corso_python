from abc import ABC, abstractmethod
import math

# Costanti fisiche
G = 6.67430e-11
sigma = 5.670374419e-8


# Classe 1: Corpo gravitazionale
class CorpoCeleste:
    def __init__(self, nome: str, massa: float, raggio: float):
        self.nome = nome
        self.massa = massa
        self.raggio = raggio

    def gravita_superficie(self) -> float:
        return G * self.massa / self.raggio**2


# Classe 2: Sorgente radiativa
class SorgenteRadiativa(ABC):
    def __init__(self, temperatura: float):
        self.temperatura = temperatura

    def luminosita_termica(self, raggio: float) -> float:
        return 4 * math.pi * raggio**2 * sigma * self.temperatura**4

    @abstractmethod
    def spettro(self):
        pass


# Classe 3: Oggetto magnetico
class OggettoMagnetico:
    def __init__(self, campo_magnetico: float):
        self.campo_magnetico = campo_magnetico  # Tesla

    def energia_magnetica(self, volume: float) -> float:
        # Energia magnetica: B^2 / (2μ0) * volume
        mu0 = 4 * math.pi * 1e-7
        return (self.campo_magnetico**2 / (2 * mu0)) * volume


# Ereditarietà multipla
class Magnetar(CorpoCeleste, SorgenteRadiativa, OggettoMagnetico):
    """
    Una magnetar è una particolare forma di stella di neutroni
    caratterizzata da un campo magnetico estremamente intenso,
    il più forte conosciuto nell’universo.
    """
    def __init__(self, nome, massa, raggio, temperatura, campo_magnetico):
        CorpoCeleste.__init__(self, nome, massa, raggio)
        SorgenteRadiativa.__init__(self, temperatura)
        OggettoMagnetico.__init__(self, campo_magnetico)

    def spettro(self):
        return "Spettro dominato da emissione X e gamma"

    def volume(self):
        return (4/3) * math.pi * self.raggio**3


# Esempio reale

magnetar = Magnetar(
    nome="SGR 1806-20",
    massa=2.8e30,
    raggio=1.2e4,
    temperatura=1e6,
    campo_magnetico=1e11
)

print("\nGravità superficiale:", magnetar.gravita_superficie(), "m/s^2\n")
print("Luminosità:", magnetar.luminosita_termica(magnetar.raggio), "W\n")
print("Energia magnetica:", magnetar.energia_magnetica(magnetar.volume()), "J")