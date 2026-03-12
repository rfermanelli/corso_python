# La dichiarazione di insieme vuoto con i metodi list literal e constructor call.
i_1 = {}
i_2 = set()
# La dichiarazione di insieme di dati con i metodi list literal e constructor call.
i_3 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
i_4 = set({0, 1})
#
print(i_1, i_2, i_3, i_4, sep='\n')
#
# La dichiarazione di insieme con il modello della set comprehension.
s_c = {e + 100 for e in i_3}
print("L'insieme che segue è stata costruita con una list comprehension:", s_c)
#
# La dichiarazione di insieme con il modello del frozen set.
f_s = frozenset({e + 100 for e in i_3})
print("L'insieme che segue è stata costruito come un frozen set:",f_s)
