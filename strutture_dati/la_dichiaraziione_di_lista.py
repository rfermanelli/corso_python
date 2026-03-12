# La dichiarazione di lista vuota con i metodi list literal e constructor call.
l_1 = []
l_2 = list()
# La dichiarazione di lista di dati con i metodi list literal e constructor call.
l_3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
l_4 = list([0, 1])
#
print(l_1, l_2, l_3, l_4)
#
# La dichiarazione di lista con il modello della list comprehension.
l_c = [e * 10 for e in l_3]
print("La lista che segue è stata costruita con una list comprehension:", l_c)
