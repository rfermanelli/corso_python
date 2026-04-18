"""
Problema
Dato un vettore a, di dimensione 2^h, h ∈ N, di interi totalmente ordinati,
calcolare l’intero più grande e quello immediatamente successivo
nell'ordine decrescente.
"""
def primo_secondo_r_1(a, n):
    if n == 2:
        if a[0] > a[1]:
            return a[0], a[1]
        else:
            return a[1], a[0]
    # a_1 e a_2 sono le due partizioni, aventi stessa dimensione, del vettore a.
    a_1 = a[:(n//2)]
    a_2 = a[n//2:]
    # Le chiamate ricorsive si succedono fintantoché
    # la dimensione dei vettori a_1 e a_2 è maggiore di due.
    p_1, s_1 = primo_secondo_r_1(a_1, n//2)
    p_2, s_2 = primo_secondo_r_1(a_2, n//2)
    #
    if p_1 > p_2:
        p = p_1
        if p_2 > s_1:
            s = p_2
        else:
            s = s_1
    else:
        p = p_2
        if p_1 > s_2:
            s = p_1
        else:
            s = s_2

    return p, s


p, s = primo_secondo([9, 3, 4, 2, 1, 5, 8, 6], 8)
print(f"Il numero più grande dell'insieme è: {p}, e il successivo in ordine decresente è: {s}")