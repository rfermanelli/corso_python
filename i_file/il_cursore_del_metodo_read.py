# Apriamo il file in modalità lettura
with open('file_di_testo.txt', 'r') as file:

    print("=== INIZIO LETTURA ===")

    # 1. Posizione iniziale del cursore
    print(f"1. Posizione iniziale: {file.tell()}")  # Output: 0

    # 2. Leggiamo i primi 10 caratteri
    primi_10 = file.read(10)
    print(f"2. Primi 10 caratteri: '{primi_10}'")
    print(f"   Posizione dopo: {file.tell()}")  # Output: 10

    # 3. Leggiamo altri 5 caratteri
    successivi_5 = file.read(5)
    print(f"3. Successivi 5 caratteri: '{successivi_5}'")
    print(f"   Posizione dopo: {file.tell()}")  # Output: 15

    # 4. Torniamo indietro di 8 caratteri
    file.seek(7)  # Spostiamo il cursore alla posizione 7
    print(f"4. Cursore riposizionato a: {file.tell()}")  # Output: 7

    # 5. Leggiamo da questa nuova posizione
    da_posizione_7 = file.read(6)
    print(f"5. 6 caratteri da posizione 7: '{da_posizione_7}'")
    print(f"   Posizione dopo: {file.tell()}")  # Output: 13

    # 6. Torniamo all'inizio e leggiamo tutto
    file.seek(0)  # Torna all'inizio
    tutto = file.read()
    print(f"6. Contenuto completo dal cursore 0:\n{tutto}")

    # 7. Il cursore è ora alla fine
    print(f"7. Posizione finale: {file.tell()}")  # Output: lunghezza totale file

    # 8. Proviamo a leggere ancora (stringa vuota!)
    nulla = file.read(5)
    print(f"8. Lettura dalla fine: '{nulla}' (lunghezza: {len(nulla)})")