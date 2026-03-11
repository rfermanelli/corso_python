# Ereditarietà multipla
class A:
    def process(self):
        print('A process()')

class B:
    pass

class C(A, B):
    pass

obj = C()
obj.process()
print(C.mro())  # print MRO for class C

# Ereditarietà multipla
class A:
    def process(self):
        print('A process()')

class B:
    def process(self):
        print('B process()')

class C(A, B):
    pass

obj = C()
obj.process()
print(C.mro())  # print MRO for class C

# Ereditarietà ibrida
class A:
    def process(self):
        print('A process()')

class B:
    def process(self):
        print('B process()')

class C(A, B):
    def process(self):
        print('C process()')

class D(C, B):
    pass

obj = D()
obj.process()
print(D.mro())

# Ereditarietà ibrida
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
print(D.mro())

# Ereditarietà circolare
# class A:
#     def process(self):
#         print('A process()')
#
# class B(A):
#     def process(self):
#         print('B process()')
#
# class C(A, B):  # ERRORE: ereditarietà circolare
#     pass
#
# obj = C()
# obj.process()
# print(C.mro())

# Ereditarietà singola e multilivello
class A:
    def process(self):
        print('A process()')

class B(A):
    def process(self):
        print('B process()')

class C(B, A):
    pass

obj = C()
obj.process()
print(C.mro())