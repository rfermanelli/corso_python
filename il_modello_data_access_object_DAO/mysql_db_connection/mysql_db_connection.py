# funzione di connessione al database mysql.

from DAO.mysql_db_config.mysql_configuration_file import __mysql_configuration_dict
#import mysql.connector
from mysql.connector import connect, Error

def connessione_db_mysql():
    try:
        connessione_mysql = connect(**__mysql_configuration_dict)
        return connessione_mysql
    except Error as errore_connessione_mysql:
        return errore_connessione_mysql


if __name__ == "__main__":
    print(connessione_db_mysql())
#print(connessione_db_mysql())


