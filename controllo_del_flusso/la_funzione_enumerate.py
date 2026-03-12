# 1) la enumerazione degli elementi di una tupla.
frutti = ("mela", "banana", "ciliegia")
for indice, frutto in enumerate(frutti):
    print(indice, frutto)

# 2) la enumerazione degli elementi di una lista.
frutti = ["mela", "banana", "ciliegia"]
for indice, frutto in enumerate(frutti):
    print(indice, frutto)

# 3) la enumerazione degli elementi di un dizionario.
frutti = {0: "mela", 1: "banana", 2: "ciliegia"}
for indice, frutto in enumerate(frutti.items()):
    print(indice, frutto)

# 4) la enumerazione degli elementi di un insieme.
frutti = {"mela", "banana", "ciliegia"}
for indice, frutto in enumerate(frutti):
    print(indice, frutto)

# 5) la enumerazione degli elementi di una stringa.
frutti = "mela, banana, ciliegia"
for indice, frutto in enumerate(frutti):
    print(indice, frutto)
