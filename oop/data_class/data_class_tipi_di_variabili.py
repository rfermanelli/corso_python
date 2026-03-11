from dataclasses import dataclass, field
from typing import List, Dict, Any, ClassVar

@dataclass
class Studente:
    # Campi obbligatori durante la instanziazione
    nome: str
    cognome: str

    # Campi con valori di default
    eta: int = 18
    # La variabile 'voti' è di tipo List ed è generata per ogni istanza
    # (la funzione 'list' viene chiamata ogni volta che viene creata una nuova istanza)
    # e ogni oggetto ottiene una lista separata, indipendente dalle altre
    # ossia: 'voti' è una variabile con un valore predefinito creato da una factory,
    # cioè una nuova lista vuota per ogni istanza.
    # Se 'voti' venisse definita come voti: List[int] = []
    # allora tutte le istanze condividerebbero la stessa lista,
    # perché le liste sono oggetti mutabili.
    voti: List[int] = field(default_factory=list)

    # Campo calcolato (non incluso in __init__)
    @property
    def nome_completo(self) -> str:
        return f"{self.nome} {self.cognome}"

    # Variabile di classe
    # La variabile 'scuola' è di tipo ClassVar, ossia: di classe
    scuola: ClassVar[str] = "Liceo Scientifico"

    # Campo con validazione
    #__post_init__(self) è un hook chiamato automaticamente subito dopo che
    # la dataclass ha inizializzato gli attributi.
    # Esegue operazioni di inizializzazione e/o validazioni oppure calcoli
    # sugli attributi già assegnati.
    def __post_init__(self):
        if self.eta < 0:
            raise ValueError("L'età non può essere negativa")


# Utilizzo
studente = Studente("Anna", "Bianchi", 20, [8, 9, 7])
print(f"Il nome dello studente è {studente.nome_completo}")  # Anna Bianchi
print(f"I voti di {studente.nome} sono: {studente.voti}")
print(f"Il nome della scuola frequentata da {studente.nome} è {Studente.scuola}")  # Liceo Scientifico

