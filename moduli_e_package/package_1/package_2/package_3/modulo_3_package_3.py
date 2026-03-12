# Import della funzione dal modulo del secondo livello usando la sintassi con punti
from ..modulo_2_package_2 import funzione_di_secondo_livello

def funzione_di_terzo_livello():
    # Chiamata alla funzione del primo livello
    risultato = funzione_di_secondo_livello()
    return f"Secondo livello: {risultato}"