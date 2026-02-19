from dataclasses import dataclass

@dataclass
class Veicolo:
    marca: str
    modello: str
    anno: int

@dataclass
class Auto(Veicolo):
    numero_porte: int = 4
    carburante: str = "benzina"

@dataclass
class Moto(Veicolo):
    cilindrata: int
    tipo: str = "sportiva"

# Le istanze di tipo Auto e di tipo Moto:
auto = Auto("Toyota", "Corolla", 2022, 4, "ibrido")
moto = Moto("Yamaha", "MT-07", 2023, 689)

print(auto)  # Auto(marca='Toyota', modello='Corolla', anno=2022, numero_porte=4, carburante='ibrido')