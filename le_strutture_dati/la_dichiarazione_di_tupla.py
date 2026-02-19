# La dichiarazione di tupla vuota con i metodi list literal e constructor call.
t_1 = ()
t_2 = tuple()
# La dichiarazione di tupla di dati con i metodi list literal e constructor call.
t_3 = (0, 1)
t_4 = tuple([0, 1])
#
print(t_1, t_2, t_3, t_4)
#
# La dichiarazione di tupla con il modello della tuple comprehension.
t_c_1 = (e * 10 for e in t_3)
t_c_2 = tuple((e * 10 for e in t_3))
t_c_3 = list((e * 10 for e in t_3))
print(t_c_1, t_c_2, t_c_3, sep=" --- ")
