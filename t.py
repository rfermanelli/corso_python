class Automobile:
    def __init__(self, marca, modello, cilindrata):
        self.marca_automobile = marca
        self.modello_automobile = modello
        self.cc_automobile = cilindrata


auto = Automobile("FIAT", "Panda", 900)

print(auto.cc_automobile)