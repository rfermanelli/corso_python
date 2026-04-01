from random import randint

def vernam_codec(signal):
    def random_number(signal):
        yield randint(0, signal)


    r_number = [number for number in random_number(signal)]
    return r_number


print(vernam_codec(6))







