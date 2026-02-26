class Pianeta:
    def __init__(self, nome, massa):
        self.nome = nome
        self.massa = massa  # kg

    # Rappresentazione utile per debug
    def __repr__(self):
        return f"Pianeta(nome='{self.nome}', massa={self.massa})"

    # Overloading dell'operatore di uguaglianza
    def __eq__(self, other):
        if not isinstance(other, Pianeta):
            return NotImplemented
        return self.massa == other.massa

    # Overloading dell'operatore di disuguaglianza
    def __ne__(self, other):
        if not isinstance(other, Pianeta):
            return NotImplemented
        return self.massa != other.massa

    # Overloading dell'operatore di minore di
    def __lt__(self, other):
        if not isinstance(other, Pianeta):
            return NotImplemented
        return self.massa < other.massa

    # Overloading dell'operatore di minore o uguale
    def __le__(self, other):
        if not isinstance(other, Pianeta):
            return NotImplemented
        return self.massa <= other.massa

    # Overloading dell'operatore di maggiore di
    def __gt__(self, other):
        if not isinstance(other, Pianeta):
            return NotImplemented
        return self.massa > other.massa

    # Overloading dell'operatore di maggiore o uguale
    def __ge__(self, other):
        if not isinstance(other, Pianeta):
            return NotImplemented
        return self.massa >= other.massa


terra = Pianeta("Terra", 5.97e24)
marte = Pianeta("Marte", 6.39e23)
clone_terra = Pianeta("Terra2", 5.97e24)

print(terra == clone_terra)  # True, Python cerca automaticamente il metodo __eq__() della classe Pianeta
print(terra != marte)        # True
print(marte < terra)         # True
print(marte <= terra)        # True
print(terra > marte)         # True
print(terra >= clone_terra)  # True