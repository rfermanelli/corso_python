import pymysql

__mysql_configuration_dict = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'root',
    'database': 'corso_python',
    'port': 3307
}

def connessione_db_mysql():
    try:
        connessione_mysql = pymysql.connect(**__mysql_configuration_dict)
        cursore = connessione_mysql.cursor()
        cursore.execute("insert into studente(matricola, nome_studente) values(7, 'Conte Oliver')")
        connessione_mysql.commit()
        cursore.close()
        connessione_mysql.close()
        return connessione_mysql
    except pymysql.connect.Error as errore_connessione_mysql:
        return errore_connessione_mysql

print(connessione_db_mysql())