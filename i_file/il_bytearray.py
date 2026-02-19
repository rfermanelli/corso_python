# Creazione di un bytearray da una stringa
data = bytearray("Ciao! Sto usando Python", "utf-8")
print("Bytearray iniziale:", data)

# Accesso ai singoli byte
print("Il primo byte della stringa è:", data[0])

# Modifica di un byte
data[0] = ord('B')  # ord('B') restituisce il valore numerico del carattere
print("La stringa dopo la modifica è:", data)

# Aggiunta di nuovi byte
data.extend(b" - il semplice -")
print("La stringa dopo l'estensione è:", data)

# Rimozione di un byte (ad esempio il primo)
del data[0]
print("La stringa dopo la cancellazione del primo byte è:", data)

# Conversione del bytearray in stringa
stringa_finale = data.decode("utf-8")
print("Bytearray convertito in stringa:", stringa_finale)


