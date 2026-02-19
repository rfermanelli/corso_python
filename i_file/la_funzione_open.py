try:
    file = open("file_di_testo.txt", "r")
except FileNotFoundError:
    file = open("file_di_testo.txt", "w")
