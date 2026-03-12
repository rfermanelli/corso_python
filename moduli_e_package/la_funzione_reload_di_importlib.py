import time
import importlib
import math_operations as mathop

while True:
    print(f"Versione modulo: {mathop.VERSIONE}")
    print("2 + 3 =", mathop.addizione(2, 3))
    print("2 * 3 =", mathop.moltiplicazione(2, 3))
    print("PI =", mathop.PI)
    print("-" * 30)

    time.sleep(3)

    # hot reload del modulo
    importlib.reload(mathop)


