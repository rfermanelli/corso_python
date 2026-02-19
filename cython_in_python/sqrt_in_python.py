# sqrt.cp313-win_amd64.pyd
# (è il modulo compilato: codice macchina)
#
# Cartella `build/
# (Equivalente alla cartella `__pycache__` ma per la compilazione Cython)
# temp.win-amd64-cpython-313/`
# (File temporanei della compilazione)
# lib.win-amd64-cpython-313/
# (Copia del file .pyd)
#
# Struttura pulita:
#
# cython_in_python/
# ├── sqrt.pyx  (sorgente)
# ├── setup.py  (script di compilazione)
# ├── sqrt_p.py (eseguibile python)
# └── sqrt.cp313-win_amd64.pyd  (modulo compilato - solo questo serve per usare)
#
#
import sqrt

print("Radice quadrata di 25:", sqrt.cython_sqrt(25.0))
print("Radice quadrata di 2:", sqrt.cython_sqrt(2.0))