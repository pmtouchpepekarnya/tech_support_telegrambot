# database.py
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """Создать соединение с базой данных SQLite, указанной в db_file"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    """Создать таблицу по предоставленному SQL-запросу"""
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def add_support_request(conn, support_request):
    """Добавить запрос в поддержку в базу данных"""
    sql = ''' INSERT INTO support_requests(user_name,store_point,reason)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, support_request)
    return cur.lastrowid

# Здесь можно добавить дополнительные функции для работы с базой данных
