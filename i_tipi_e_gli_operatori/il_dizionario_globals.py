x = 5
y = "test"

# Visualizzazione del dizionario locale o globale del modulo dizionario_globals:
print("Il dizionario globals()/locals() del modulo dizionario_globals:", locals())

locals()['x'] = 42
print("Il dizionario globals()/locals() del modulo dizionario_globas dopo locals()['x'] = 42", locals())
