try:
    with open("file_di_testo.txt", "r") as file:
        riga = file.readline()
        while riga:
            print(riga)
            riga = file.readline()
except FileNotFoundError:
    file = open("file_di_testo.txt", "w")


