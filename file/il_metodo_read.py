file = open("file_di_testo.txt", "w")
file.write("Hulk\nThor")
file.close()

file = open("file_di_testo.txt", "r")

# read() - Legge caratteri/byte
contenuto = file.read()
print("Il contenuto del file file_di_testo.txt è", contenuto)
file.seek(0)

# readline() - Legge una riga
riga = file.readline()
print("Il contenuto della prima riga del file file_di_testo.txt è:", riga)
file.seek(0)

# readlines() - Legge tutte le righe in una lista
righe = file.readlines()
print("Il contenuto del file file_di_testo.txt è:", righe)
file.seek(0)

# read(n) - Legge n caratteri
primi_n = file.read(2)
print("Il contenuto dei primi due caratteri del file file_di_testo.txt è:", primi_n)

