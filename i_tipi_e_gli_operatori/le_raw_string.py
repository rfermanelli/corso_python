"""
Una raw string (stringa grezza) è una stringa nella quale i caratteri di escape (‘\’)
non sono interpretati come tali.
Una raw string non deve terminare con il carattere ‘\’.
Una raw string è utile per:
1) La definizione di percorsi (path).
2) La definizione di espressioni regolari.
"""
# La funzione print() che segue visualizza il percorso.
print(r"C:\Users\r.fermanelli\Desktop\In lavorazione\Python")
# La funzione print() che segue solleva una eccezione.
#print("C:\Users\r.fermanelli\Desktop\In lavorazione\Python")
