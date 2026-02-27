"""
Esiste una lunga sequenza di misure di luminosità provenienti da una singola stella osservata da un telescopio spaziale.
Ogni valore rappresenta quanta luce la stella emette in un certo istante.
Per la maggior parte del tempo la luminosità ondeggia in modo regolare, seguendo il suo normale battito stellare.
Poi succede qualcosa di più curioso. In un tratto di pochi minuti o poche ore, la luminosità scende ripetutamente
in modo non previsto. Non un singolo calo — che potrebbe essere un disturbo strumentale — ma una piccola serie di
cali ravvicinati. Forse tre o quattro immersioni successive, una accanto all’altra nella serie temporale.
Queste cadute allineate formano il cluster: un gruppo di valori anomali che si manifesta nello stesso intervallo ristretto.
Da un punto di vista astronomico potrebbe suggerire il passaggio di detriti, un transito planetario irregolare
o perfino un comportamento impulsivo della stella stessa.
Una finestra scorrevole, passando sopra quella regione, vedrebbe la densità degli “affossamenti” aumentare improvvisamente,
rivelando l’esistenza del grumo anomalo.
Quel piccolo grumo diventa una storia celeste da decifrare,
un tentativo di capire se l’universo sta lanciando un sassolino o un pianeta intero.

Esercizio n. 1
Scrivere una funzione che, data in input una serie temporale di dati partizionata in blocchi asincroni
della stessa dimensione, restituisca i cluster di valori anomali.
"""

import asyncio
import random

async def brightness_sequence(sequence):
    for block in [sequence[i:i + 10] for i in range(0,len(sequence),10)]:
        await asyncio.sleep(10)
        yield block


async def main():
    sequence = [el for el in [random.randint(0, 1000) for _ in range(100)]]
    print(sequence)

    async for block in brightness_sequence(sequence):
        # Qui deve essere inserita la funzione di riconoscimento del cluster.
        print(f"Blocco ricevuto: {block}")

# Esecuzione asincrona della funzione brightness_sequence.
asyncio.run(main())

