# Import dei modelli DTO e DAO dello studente, del corso e dell'esame:
from DAO.dto.studente_dto import StudenteDTO
from DAO.service.studente_service import StudenteService
#
# La funzione riceve in ingresso il valore della scelta effettuata dall'utente
# e chiama la funzione DAO corrispondente.
def funzione_di_scelta(funzione):

    if funzione == "I":
        matricola = int(input("Inserisci la matricola dello studente: "))
        nome_studente = input("Inserisci il nome dello studente: ")
        studente = StudenteDTO(matricola=matricola, nome_studente=nome_studente)
        insert_studente = StudenteService.insert_studente(studente)
        return insert_studente

    if funzione == "S":
        matricola = int(input("Inserisci la matricola dello studente da cercare: "))
        studente_exact = StudenteService.select_studente(matricola, "")
        return studente_exact

    if funzione == "A":
        studente_all = StudenteService.select_studente_all()
        lista_s = []
        for row in studente_all:
            tupla = row.matricola, row.nome_studente
            lista_s.append(tupla)
        return lista_s
        #return studente_all
# Menù:
print("MENU' DI SCELTA\n___")
print("Funzione di inserimento di uno studente - scelta = I")
print("Funzione di aggiornamento di uno studente - scelta = U")
print("Funzione di cancellazione di uno studente - scelta = D")
print("Funzione di selezione di uno studente - scelta = S")
print("Funzione di selezione di tutti gli studenti - scelta = A")
print("Funzione di uscita dal menù - scelta = E")
# Scelta dell'utente:
while True:
    try:
        funzione_scelta = input("\nScegli una funzione - scelta = ")
        assert funzione_scelta in ("I", "U", "D", "S", "A", "E")
        break
    except AssertionError:
        print("Scegliere una delle funzioni del menù")
#
print(funzione_di_scelta(funzione_scelta))
