import datetime
from dataclasses import dataclass

@dataclass
class EsameDTO:
    codice_esame: int
    codice_corso: str
    nome_studente: str
    data_esame: datetime.date


