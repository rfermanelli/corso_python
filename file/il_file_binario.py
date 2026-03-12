#Creazione e scrittura di un file binario.
try:
    stream = open("file_binario.bin", "wb")
    stream.write(bytearray(b"Hello World!"))
    stream.close()
except Exception as ex_err:
    print(ex_err)
# Lettura di un file binario.
try:
    bin_file = open("file_binario.bin", "rb")
    byte_array = bin_file.read()
    print(byte_array)
    bin_file.close()
except Exception as ex_err:
    print(ex_err)

