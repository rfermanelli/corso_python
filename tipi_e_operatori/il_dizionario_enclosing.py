def f():
    x = 10
    y = 20
    # Visualizzazione del dizionario locale della funzione f()
    print("Il dizionario locals() della funzione f():", locals())
    def g():
        z = 5
        global x
        x = 200
        # Visualizzazione del dizionario locale della funzione interna()
        print("Il dizionario locals() della funzione g():", locals())
    g()

f()

# Visualizzazione del dizionario locale/globale del modulo dizionario_enclosing:
print("Il dizionario locals()/globals() del modulo dizionario_enclosing:", globals())