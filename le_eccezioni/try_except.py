try:
    n = int(input('Inserisci un numero intero ---> '))
    print(1 / n)
except ZeroDivisionError:
    n = 1
    print(1 / n)
    print('Il numero inserito è 0 e quindi non posso eseguire la divisione.')
except ValueError:
    print('Il valore inserito non è numerico e quindi non posso eseguire la divisione.')
except TypeError:
    print('Il valore inserito non è numerico e quindi non posso eseguire la divisione.')
except:
    pass
else:
    try:
        print(1 / int((1 / n)))
    except:
        print("Divisione per zero completata.")
finally:
    print("Try statement terminato senza eccezioni")
