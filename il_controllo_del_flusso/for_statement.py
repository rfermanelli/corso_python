# 1) for statement, senza la keyword else, sulla stessa linea.
for x in range(2): print(x, end=' ')

# 2) for statement, con la keyword else, sulla stessa linea.
#for y in range(2): print(y, end=' ') else: print('Fine')

# 3) for statement, con la keyword else, indentato.
for y in range(12):
    print(y, end=' ')
else:
    print('\nFine')
