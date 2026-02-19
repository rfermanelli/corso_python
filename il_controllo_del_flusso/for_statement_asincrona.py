import asyncio  # asyncio è la libreria standard per la programmazione asincrona.

# La funzione ricevi_messaggi è un "generatore asincrono": produce dati poco alla volta, nel tempo.
async def ricevi_messaggi():
    messaggi = ["Ciao!", "Come va?", "Sto arrivando...", "Fatto!"]
    for m in messaggi:
        await asyncio.sleep(10)  # simula un ritardo di rete
        yield m  # restituisce il messaggio

# async for legge i messaggi uno alla volta.
async def main():
    async for messaggio in ricevi_messaggi():
        print("Messaggio ricevuto:", messaggio)

# Esecuzione asincrona.
asyncio.run(main())
