import os
from psycopg2 import connect
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class Conexion:
    def __init__(self, table, where=''):
        self.conn = connect(database=os.getenv("DB_NAME"),user=os.getenv("DB_USER"),password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT"),host=os.getenv("DB_HOST"))
        self.cursor = self.conn.cursor()
        self.table = table
        self.where = where

    def get_one(self):  
        query = f"SELECT * FROM {self.table} {self.where}"
        self.cursor.execute(query)
        return self.cursor.fetchone()

    def get_all(self):
        query = f"SELECT * FROM {self.table}"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def execute_query(self,query):
        self.cursor.execute(query)
        return self.cursor

    def commit(self):
        self.conn.commit()
        return True

    def close_connection(self):
        self.conn.close()