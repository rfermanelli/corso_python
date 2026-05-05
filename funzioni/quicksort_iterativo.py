def quicksort_iterativo(a, n):

    if len(a) > 1:
        perno = a[0]
        p = 1
        q = n - 1
        while c < n:
            while p != q and (not (perno < a[p] and perno > a[q])):
                if perno < a[p]:
                    q = q - 1
                else:
                    p = p + 1
            if p != q:
                tran = a[p]
                a[p] = a[q]
                a[q] = tran
                p = p + 1
                q = q - 1
            else:
                a = a[1:q]

        print(a)

quicksort_iterativo([30, 40, 25, 50, 15, 45, 38, 5, 10, 35], 10)