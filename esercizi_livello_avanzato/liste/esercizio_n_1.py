"""
Esercizio n. 1: Segmenti massimali con vincoli multipli

Data una lista di interi, trovare tutti i segmenti contigui massimali tali che:
1. La somma degli elementi sia positiva
2. Il numero di elementi distinti sia pari
3. La rimozione di qualsiasi elemento alle estremità invalida almeno una delle condizioni
Restituire i segmenti come coppie di indici (i, j).

Nota 1: Un segmento contiguo di estremi i, j (0<=i<j<=n) di una lista L è una sottolista L1 i cui elementi sono gli elementi della lista L che vanno dall’indice i fino all’indice j - 1.
Nota 2: un segmento contiguo [i, j) è detto massimale se non può essere esteso né a sinistra né a destra senza violare almeno uno dei vincoli.
"""

def list_maximal_segment(lista):

    maximal_segment_dictionary = {}

    for i in range(len(lista)):
        for j in range(len(lista)):
            maximal = True
            if (0 <= i) and (i < j) and (j <= len(lista)):
                # La somma degli elementi del segmento deve essere positiva
                # Il numero di elementi distinti del segmento deve essere pari
                if sum(lista[i:j]) > 0 and len(set(lista[i:j])) % 2 == 0:
                    # L'estensione a sinistra o a destra del segmento viola uno dei primi due vincoli
                    # ---> Il segmento è massimale
                    if i:
                        if len(set(lista[i - 1:j])) % 2 != 0 or sum(lista[i - 1:j]) < 0:
                            maximal = True
                    if j < len(lista):
                        if len(set(lista[i:j + 1])) % 2 != 0 or sum(lista[i:j + 1]) < 0:
                            maximal = True
                    if maximal:
                        maximal_segment_dictionary[f"segmento ({i}, {j})"] = lista[i:j]

    return max(list(map(lambda x: x[1], maximal_segment_dictionary.items())))


l = [2, -1, 2, -1, -1, 2, -1]
print(list_maximal_segment(l))




