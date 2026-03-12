import math_operations as m

contenuto = dir(m)

for nome in contenuto:
    if not nome.startswith("__"):
        print(nome)

