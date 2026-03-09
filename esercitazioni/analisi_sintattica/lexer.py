import grammar

def lexer(linea):
    token = []
    trovato = 0
    sequenza_terminali = linea.split()
    for terminale in sequenza_terminali:
        if terminale in grammar.TERMINALI_LSW:
            for antecedente in grammar.produzioni_lsw.keys():
                if terminale in grammar.produzioni_lsw[antecedente]:
                    trovato = 1
                    token.append(antecedente)
                    break
            if not trovato:
                return f"Errore interno: '{terminale}' sconosciuto nella grammatica"
        else:
            return f"Errore lessicale in '{linea}': '{terminale}' sconosciuto"
    return token

linea = "il padawan ha un maestro"
print(lexer(linea))

