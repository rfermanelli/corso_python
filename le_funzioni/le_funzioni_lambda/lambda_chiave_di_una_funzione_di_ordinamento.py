"""
key è un parametro della funzione sorted che informa Python
sul tipo di confronto che deve fare per ordinare gli elementi:
Per ogni elemento dell'oggetto iterabile si esegue la funzione key
e si utilizza il valore restituito da key per fare i confronti durante l’ordinamento.
"""

persone = [('Alice', 25), ('Chuck', 18), ('Bob', 20), ('Charlie', 30)]

# La lista persone è ordinata per età in ordine crescente:
persone_ordinate_crescente = sorted(persone, key=lambda persona: persona[1])
# La lista persone è ordinata per età in ordine decrescente:
persone_ordinate_decrescente = sorted(persone, key=lambda persona: persona[1], reverse=True)
# La lista persone è ordinata per nome:
persone_ordinate_ = sorted(persone)

print("La lista persone ordinata per età in modo crescente: ", persone_ordinate_crescente)
print("La lista perosne ordinata per età in modo decrescente: ", persone_ordinate_decrescente)
print("La lista persone ordinata per nome: ", persone_ordinate_)