try:
    file = open("file_di_testo.txt", "x")
    file.write("Batman")
    file.close()
except FileExistsError:
    file = open("file_di_testo_1.txt", "w")
    file.write("Batman")



