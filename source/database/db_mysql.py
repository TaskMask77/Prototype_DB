import mysql.connector

def get_connection():
    try:
        return mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'root2024',
            database = 'psicosocial'
        )

    except mysql.connector.errors as er:
        raise er