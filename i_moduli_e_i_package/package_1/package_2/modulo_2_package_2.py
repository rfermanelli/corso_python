# # L'import che segue è definito in modo nominale,
#  àossia: dichiarando gli identificatori di tutti i package
# from i_moduli_e_i_package.package_1.modulo_1_package_1 import f
# print(f())
#
# # L'import che segue è definito in modo puntuale,
# # ossia: utilizzando la sintassi:
# # 1) punto singolo (.) importazione dal modulo corrente;
# # 2) due punti (..)  importazione dal pacchetto genitore (un livello sopra);
# # 3) tre punti (...) importazione dal pacchetto nonno (due livelli sopra)).
# from ..modulo_1_package_1 import f
# print(f())

# Import della funzione dal modulo del primo livello usando la sintassi con punti
from ..modulo_1_package_1 import funzione_di_primo_livello

def funzione_di_secondo_livello():
    # Chiamata alla funzione del primo livello
    risultato = funzione_di_primo_livello()
    return f"Secondo livello: {risultato}"



