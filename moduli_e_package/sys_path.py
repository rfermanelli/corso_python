from sys import path
# sys.path: elenco dei percorsi utilizzati da Python per cercare il modulo da compilare in bytecode:
print("sys.path: elenco dei percorsi utilizzati da Python per cercare il modulo da compilare in bytecode:\n")
for p in path:
    print(p)
# Un percorso nuovo è aggiunto alla variabile sys.path:
path.append("C:\\Users\\r.fermanelli\\Python\\PythonProject")
print()
print("sys.path aggiornato:\n")
# sys.path aggiornato con il nuovo percorso:
for p in path:
    print(p)
# sys.path ripristinato:
path.pop()
print()
print("sys.path ripristinato:\n")
for p in path:
    print(p)
