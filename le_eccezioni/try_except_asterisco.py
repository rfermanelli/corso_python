import asyncio

async def fallisci_dopo(delay, errore):
    await asyncio.sleep(delay)
    raise errore

async def main():
    try:
        try:
            await asyncio.gather(
                fallisci_dopo(0.1, ValueError("Errore di valore")),
                fallisci_dopo(0.2, TypeError("Errore di tipo")),
                fallisci_dopo(0.3, KeyError("Errore di chiave")),
            )
        except* ValueError as e:
            print("Gestiti ValueError:", e)
        except* TypeError as e:
            print("Gestiti TypeError:", e)
    except* Exception as e:
        print("Gestiti tutti gli altri tipi di eccezione:", e)

asyncio.run(main())
