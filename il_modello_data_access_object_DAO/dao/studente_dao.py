from DAO.mysql_db_connection.mysql_db_connection import connessione_db_mysql
from DAO.dto.studente_dto import StudenteDTO

class StudenteDAO:
    @staticmethod
    def insert_studente(studente: StudenteDTO):
        try:
            connessione = connessione_db_mysql()
            cursore = connessione.cursor()
            cursore.execute("insert into studente (matricola, nome_studente) values (%s, %s)",
                            (studente.matricola, studente.nome_studente))
            connessione.commit()
            cursore.close()
            connessione.close()
            return 0 #connessione
        except Exception as err_insert_studente:
            return err_insert_studente

    @staticmethod
    def select_studente(studente: StudenteDTO):
        try:
            connessione = connessione_db_mysql()
            cursore = connessione.cursor()
            cursore.execute("select matricola, nome_studente from studente where matricola = %s",
                            (studente.matricola,))
            row = cursore.fetchone()
            connessione.commit()
            cursore.close()
            connessione.close()
            #if row:
            #    return StudenteDTO(matricola=row[0], nome_studente=row[1])
            return row
        except Exception as create_studente_err:
            print(create_studente_err)

    @staticmethod
    def update_studente(studente: StudenteDTO):
        try:
            connessione = connessione_db_mysql()
            cursore = connessione.cursor()
            cursore.execute("update studente set nome_studente = %s where matricola = %s",
                            (studente.nome_studente, studente.matricola))
            connessione.commit()
            cursore.close()
            connessione.close()
        except Exception as create_studente_err:
            print(create_studente_err)

    @staticmethod
    def delete_studente(studente: StudenteDTO):
        try:
            connessione = connessione_db_mysql()
            cursore = connessione.cursor()
            cursore.execute("delete from studente where matricola = %s",
                            (studente.matricola,))
            row = cursore.fetchone()
            connessione.commit()
            cursore.close()
            connessione.close()
            return row
        except Exception as create_studente_err:
            print(create_studente_err)

    @staticmethod
    def select_studente_all():
        try:
            # Apertura della connessione al database.
            connessione = connessione_db_mysql()
            # Apertura del cursore.
            cursore = connessione.cursor()
            # Esecuzione della query.
            cursore.execute("select matricola, nome_studente from studente order by matricola")
            # Estrazione globale delle tuple della entità.
            rows = cursore.fetchall()
            # Costruzione dell'output.
            studente_all = [StudenteDTO(matricola=row[0], nome_studente=row[1]) for row in rows]
            # Estrazione singolare delle tuple della entità e costruzione simultanea dell'output.
            #table_tuple = cursore.fetchone()
            #lista_di_tuple = []
            #while table_tuple:
            #    lista_di_tuple.append(table_tuple)
            #    table_tuple = cursore.fetchone()
            # Commit della query
            connessione.commit()
            # Chiusura del cursore.
            cursore.close()
            # Chiusura della connessione al database.
            connessione.close()
            # Output della funzione.
            return studente_all
            #return lista_s

        except Exception as create_studente_err:
            print(create_studente_err)
