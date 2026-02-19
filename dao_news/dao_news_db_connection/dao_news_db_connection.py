import mysql.connector
from dao_news.dao_news_db_configuration_file.dao_news_db_configuration_file import mysql_configuration_dictionary

def mysql_db_connection_f():
    try:
        dao_news_db_connection_state_v = mysql.connector.connect(mysql_configuration_dictionary)
        return dao_news_db_connection_state_v
    except mysql.connector.Error as dao_news_db_error_state_v:
        return dao_news_db_error_state_v

print(mysql_db_connection_f())