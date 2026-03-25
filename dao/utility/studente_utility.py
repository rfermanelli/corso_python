from dao.mysql_db_connection.mysql_db_connection import connessione_db_mysql

try:
    connessione = connessione_db_mysql()
    cursore = connessione.cursor()
    cursore.execute('DROP TABLE studente')
    cursore.execute('CREATE TABLE studente (matricola INT NOT NULL, nome_studente VARCHAR(100) NOT NULL, CONSTRAINT pk_studente PRIMARY KEY (matricola));')
    connessione.commit()
    cursore.close()
    connessione.close()
except Exception as err_insert_studente:
    print(err_insert_studente)
else:
    print("La tabella 'studente' è stata creata")

