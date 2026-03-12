try:
    n = int(input('Inserisci un numero intero ---> '))
    assert n != 0
    print(1 / n)
except AssertionError:
    print(f"Il valore in ingresso è: {n}; la divisione non è rappresentabile.")

#
try:
    n = input('Inserisci un numero intero ---> ')
    assert ord(n) not in {48, 49}, "int(n) % 2 == 1"
    print(1 / int(n))
except AssertionError:
    print('Il numero inserito è 0 oppure è 1')

