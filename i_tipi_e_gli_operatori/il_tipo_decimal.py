x = 0.1
y = 0.2
z = x + y
print("La somma dei numeri float 0.1 e 0.2 è:", z)

"""
Il tipo Decimal() del modulo decimal è un tipo numerico. 
Rappresenta i numeri in base 10, non in base 2.
Internamente i numeri sono memorizzati come una terna costituita da:
un segno, una tupla di cifre, e un esponente che rappresenta la potenza di 10.
"""
from decimal import Decimal
z = Decimal("0.1") + Decimal("0.2")
print("La somma decimale dei numeri float 0.1 e 0.2 è:", z)
# La visualizzazione della rappresentazione del tipo Decimal
d = Decimal("12.34")
print("La rappresentazione del tipo Decimal 12.34 è:", d.as_tuple())
print("La gestione del tipo Decimal può essere data con la struttura di lista:", list(d.as_tuple()))
