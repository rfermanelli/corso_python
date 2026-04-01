from random import randrange
x = [(lambda number: randrange(0,number))(number) for number in range(1,10)]
print(x)