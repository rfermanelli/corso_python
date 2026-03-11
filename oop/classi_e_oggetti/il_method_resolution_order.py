# Ereditarietà multilivello
class A:
    def saluta(self):
        print("Metodo di A")

class B(A):
    def saluta(self):
        print("Metodo di B")

class C(B):
    pass


oggetto = C()
oggetto.saluta()

print(C.__mro__)

"""
Ereditarietà multipla

D.metodo() stampa "D"
super() → prossimo metodo() nella MRO → B
B stampa "B"
super() → prossimo metodo() nella MRO → C
C stampa "C"
super() → prossimo metodo() nella MRO → A
A stampa "A"
"""
class A:
    def metodo(self):
        print("Metodo di A")

class B(A):
    def metodo(self):
        print("Metodo di B")
        super().metodo()

class C(A):
    def metodo(self):
        print("Metodo di C")
        super().metodo()

class D(B, C):
    def metodo(self):
        print("Metodo di D")
        super().metodo()


oggetto = D()
oggetto.metodo()

print(D.__mro__)
#
class A:
    def metodo(self):
        print("Metodo di A")

class B(A):
    pass

class C(A):
    def metodo(self):
        print("Metodo di C")
        super().metodo()

class D(B, C):
    pass


oggetto = D()
oggetto.metodo()

print(D.__mro__)

"""
Ereditarietà multipla
Una nota sulla ricerca di metodo() che procede utilizzando 
il modello della visita anticipata di un albero binario: 
la radice, il sotto albero sinistro, il sotto albero destro.

A non può essere visitata prima di B poiché A è una superclasse di B.
"""
class A:
    def metodo(self):
        print("Metodo di A")

class B(A):
    def metodo(self):
        print("Metodo di B")

#class C(A, B):
class C(B, A):
    def metodo(self):
        print("Metodo di C")
        super().metodo()


oggetto = C()
oggetto.metodo()

print(C.__mro__)
