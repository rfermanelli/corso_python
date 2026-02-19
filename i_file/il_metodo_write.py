try:
    file = open("file_di_testo.txt", "x")
    file.write("Batman")
except FileExistsError:
    print("Il file esiste.")
else:
    file = open("file_di_testo.txt", "w")
    file.write("Batman")

