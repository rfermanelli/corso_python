# 1) while statement, senza la keyword else, sulla stessa linea.
x = True
while x: x = False

# 2) while statement, con la keyword else, sulla stessa linea.
# y = True
# while y == True: y = False else: y = True

# 3) while statement indentato.
z = True
while z:
    z = False
else:
    z = True

# 4)
y = 10
while y > 0:
    print(y, end=' ')
    y = y - 1
else:
    print('\nFine')