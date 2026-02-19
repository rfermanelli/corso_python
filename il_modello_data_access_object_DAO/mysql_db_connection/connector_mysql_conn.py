import mysql.connector

__mysql_configuration_dict = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'root',
    'database': 'corso_python',
    'port': 3307,
    'charset': 'utf8mb4'
}

def connessione_db_mysql():
    try:
        connessione_mysql = mysql.connector.connect(**__mysql_configuration_dict)
        return connessione_mysql
    except mysql.connector.Error as errore_connessione_mysql:
        return errore_connessione_mysql

print(connessione_db_mysql())