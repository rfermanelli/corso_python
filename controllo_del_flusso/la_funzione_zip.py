# 1) Corrispondeza tra gli elementi di una tupla e di una lista.
frutti = ("mela", "banana", "ciliegia")
colore = ["verde", "giallo", "rosso"]

frutteria = zip(frutti, colore)

print(frutteria)
print(list(frutteria))
print(tuple(frutteria))
print(set(frutteria))
print(dict(frutteria))

# 2) Corrispondeza tra gli elementi di una tupla e di una stringa.
frutti = ("mela", "banana", "ciliegia")
colore = "verde, giallo, rosso"

frutteria = zip(frutti, colore)

print(list(frutteria))

# 3) Corrispondeza tra gli elementi di una lista e di una stringa.
frutti = ["mela", "banana", "ciliegia"]
colore = "verde, giallo, rosso"

frutteria = zip(frutti, colore)

print(list(frutteria))

# 3) Corrispondeza tra gli elementi di una lista e di una insieme.
frutti = ["mela", "banana", "ciliegia"]
colore = {"verde, giallo, rosso"}

frutteria = zip(frutti, colore)

print(list(frutteria))
