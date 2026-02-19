# La dichiarazione di dizionario vuoto con i metodi list literal e constructor call.
d_1 = {}
d_2 = dict()
# La dichiarazione di dizionario di dati con i metodi list literal e constructor call.
d_3 = {0: "zero", 1: "uno"}
d_4 = dict({0: "zero", 1: "uno"})
#
print(d_1, d_2, d_3, d_4)
#
# La dichiarazione di dizionario con il modello della dictionary comprehension.
d_1 = {v: k * 10 for k, v in d_3.items()}
print(d_1, list(d_1), sep=" --- ")