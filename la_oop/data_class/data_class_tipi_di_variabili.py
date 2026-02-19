from dataclasses import dataclass, field
from typing import List, Dict, Any, ClassVar

@dataclass
class Studente:
    # Campi obbligatori
    nome: str
    cognome: str

    # Campi con valori di default
    eta: int = 18
    voti: List[int] = field(default_factory=list)

    # Campo calcolato (non incluso in __init__)
    @property
    def nome_completo(self) -> str:
        return f"{self.nome} {self.cognome}"

    # Variabile di classe
    scuola: ClassVar[str] = "Liceo Scientifico"

    # Campo con validazione
    def __post_init__(self):
        if self.eta < 0:
            raise ValueError("L'età non può essere negativa")


# Utilizzo
studente = Studente("Anna", "Bianchi", 20, [8, 9, 7])
print(studente.nome_completo)  # Anna Bianchi
print(Studente.scuola)  # Liceo Scientifico
