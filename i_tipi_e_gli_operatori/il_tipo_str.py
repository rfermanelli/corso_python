print("Le funzioni ord() e chr():")
print("Il code point del carattere 'a' è:", ord("a"))
print("Il code point del carattere 'A' è:", ord("A"))
print("Il carattere associato al code point 100 è:", chr(100))
print()

#
print("I caratteri di escape:")
print("Ciao sto studiando\nPython")
print("Ciao sto studiando\tPython")
print("Ciao sto studiando\\Python")
print("Ciao sto studiando\rPython")
print("Ciao sto studiando\bPython")
print()

#
print("I caratteri di escape numerico:")
print("Il carattere espresso dal codice esadecimale 45 è: ", "\x45")
print("Il carattere espresso dal codice Unicode U+0065 è: ", "\u0065")
print()

#
print("Le raw string:")
print(r"C:\Users\r.fermanelli\Desktop\In lavorazione\Python")
#print(r"C:\Users\r.fermanelli\Desktop\In lavorazione\Python\")

#
print("Le f-string:")
d1 = "users"
d2 = "Desktop"
print(f"C:\\{d1}\\r.fermanelli\\{d2}\\In lavorazione\\Python")
#print(r"C:\Users\r.fermanelli\Desktop\In lavorazione\Python\")

# La list comprehension
# Stampa una lista di quadrati
print([x**2 for x in range(5)])
# Output: [0, 1, 4, 9, 16]
# Stampa numeri pari
print([x for x in range(10) if x % 2 == 0])
# Output: [0, 2, 4, 6, 8]
# Stampa tabelline
print([f"{i} x {j} = {i*j}" for i in range(1, 3) for j in range(1, 4)])
# Output: ['1 x 1 = 1', '1 x 2 = 2', '1 x 3 = 3', '2 x 1 = 2', '2 x 2 = 4', '2 x 3 = 6']
# Filtra e trasforma una lista
nomi = ['anna', 'MARIO', 'luca', 'SOFIA']
print([nome.title() for nome in nomi if nome[0].isupper()])
# Output: ['Mario', 'Sofia']
# Operazioni complesse
print([f"{x} è {'pari' if x % 2 == 0 else 'dispari'}" for x in range(5)])
# Output: ['0 è pari', '1 è dispari', '2 è pari', '3 è dispari', '4 è pari']

# il generator expression
# Stampa senza creare una lista in memoria
print(*(x**2 for x in range(5)))
# Output: 0 1 4 9 16

# Con separatore personalizzato
print(*(x for x in range(10) if x % 2 == 0), sep=', ')
# Output: 0, 2, 4, 6, 8

# join di stringhe
# Unisce elementi in una stringa
print(', '.join(str(x**2) for x in range(5)))
# Output: 0, 1, 4, 9, 16

# Lettere maiuscole
print(' '.join(chr.upper() for chr in 'python'))
# Output: P Y T H O N