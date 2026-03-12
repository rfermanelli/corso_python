try:
    file = open("file_di_testo.txt", "a")
    file.write("Spiderman")
except FileExistsError:
    print("Il file esiste.")

