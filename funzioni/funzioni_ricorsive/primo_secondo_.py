"""
Problema
Dato un vettore a, di dimensione 2^h, h ∈ N, di interi totalmente ordinati,
calcolare l’intero più grande e quello immediatamente successivo
nell'ordine decrescente.
"""
def primo_secondo_(a, n):
    if n == 2:
        if a[0] > a[1]:
            return a[0], a[1]
        else:
            return a[1], a[0]
    # a_1 è il vettore a dal quale è stato eliminato l'ultimo elemento.
    a_1 = a[:(n - 1)]
    # Le chiamate ricorsive si succedono fintantoché
    # la dimensione del vettore a_1 è maggiore di due.
    p, s = primo_secondo_(a_1, n - 1)
    #
    if p < a[n - 1]:
        s = p
        p = a[n - 1]
    else:
        if s < a[n - 1]:
            s = a[n - 1]
    return p, s


p, s = primo_secondo_([9, 3, 4, 2, 1, 5, 8, 6], 8)
print(f"Il numero più grande dell'insieme è: {p}, e il successivo in ordine decresente è: {s}")
