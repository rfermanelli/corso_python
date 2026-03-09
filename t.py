class A:
    def process(self):
        print('A process()')

class B(A):
    pass

class C(A):
    def process(self):
        print('C process()')

class D(B, C):
    pass

obj = D()
obj.process()

# Per vedere l'ordine di risoluzione dei metodi
print(D.__mro__)