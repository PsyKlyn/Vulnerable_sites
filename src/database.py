import mysql.connector

config = {
    'user': 'app_user',
    'password': 'App_DB_P@ss!',
    'host': 'db.internal.example.com',
    'database': 'production_db'
}

conn = mysql.connector.connect(**config)
