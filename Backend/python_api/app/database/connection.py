import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

# Carrega as variáveis do .env
load_dotenv()

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        if connection.is_connected():
            return connection
            
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None

def close_connection(connection):
    if connection and connection.is_connected():
        connection.close()