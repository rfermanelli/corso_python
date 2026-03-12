def f():
    a = 10
    b = "ciao"
    c = [1, 2, 3]
    # Visualizzazione della vista del dizionario locale alla funzione f():
    print("locals():", locals())
    # Modifica di una variabile tramite il dizionario locals():
    locals()['a'] = 42
    print("a dopo locals()['a'] =", a)

f()

# Visualizzazione del dizionario globale del modulo dizionario_locals:
print("globals():", globals())
