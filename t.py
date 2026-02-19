def ruota_matrice_90_gradi(a):
    n = len(a)
    i = 0
    j = 0
    b = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    while i < n:
        while j < n:
            b[j][n - 1- i] = a[i][j]
            j = j + 1
        i = i + 1
        j = 0
    return b

l = []
i = 0

print(ruota_matrice_90_gradi([[3, 3, 3], [4, 4, 4], [5, 5, 5]]))