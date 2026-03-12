l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("La lista l di partenza: ", l)

# Il metodo extend()
l.extend([[0, 1], [2, 3]])
print("La lista l a cui è applicato il metodo extend(): ", l)

# Il metodo insert()
l.insert(0,[[0, 1], [2, 3]])
print("La lista l a cui è applicato il metodo extend(): ", l)

# il metodo remove()
l.remove([[0, 1], [2, 3]])
print(l)
#
l.pop()
print(l)
#
l.pop(6)
print(l)
#
l.clear()
print(l)
#
l = [0, 11, 2, 33, 4, 15, 6, 7, 8, 19]
#
l.sort()
print(l)
#
l = [0, 11, 2, 33, 4, 15, 6, 7, 8, 19]
#
l_1 = sorted(l)
print(l_1)
#
#
l[1:3].sort()
print(l)