# Una frase da analizzare.
frase = "Python è potente, veloce e super divertente!"

"""
Il metodo join() unisce i singoli caratteri delle parole della frase utilizzando un carattere separatore.
Nell'esempio seguente il carattere separatore è "#"
"""
frase_join = "#".join(frase)
print("La frase costruita inserendo il carattere '#' fra ogni carattere della frase iniziale è", frase_join)

"""
Il metodo join() unisce i singoli caratteri delle parole, estratte al contrario, della frase.
Il metodo join() necessita di una stringa di separazione a cui è applicata.
Nell'esempio seguente la stringa è ""
"""
frase_invertita = "".join(frase[::-1])
print("La frase invertita è:", frase_invertita)

"""
Il metodo join() unisce i singoli elementi di una lista utilizzando un carattere separatore.
Nell'esempio seguente il carattere separatore è " --- ".
"""
lista = ["banane", "mele", "arance"]
lista_join = " --- ".join(lista)
print("La lista unita è:", lista_join)


