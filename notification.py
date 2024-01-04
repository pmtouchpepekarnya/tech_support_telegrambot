from user_datebase import connect_db
import json
from dispatcher import dp, bot
from aiogram import types
from user_datebase import connect_db
from aiogram.dispatcher.filters import BoundFilter
import sqlite3

# Чтение токена из файла JSON   
with open('config.json') as f:
    config = json.load(f)
    ADMIN_ID = int(config['ADMIN_ID'])

def connect_db():
    conn = sqlite3.connect('user_datebase.db')
    return conn

def create_users_table(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            last_message TEXT,
            date TEXT
        )
    """)
    conn.commit()

def get_users(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT user_id FROM users")
    return [row[0] for row in cursor.fetchall()]    

conn = connect_db()
create_users_table(conn)
users = get_users(conn)

@dp.message_handler(commands=['notification'])
async def send_notification(message: types.Message):
    print("Обработчик send_notification вызван")  # Отладочное сообщение
    conn = connect_db()
    users = get_users(conn)
    print(f"Получены пользователи: {users}")  # Отладочное сообщение
    text = message.get_args()
    for user_id in users:
        try:
            await bot.send_message(user_id, text)
        except Exception as e:
            print(f"Ошибка при отправке сообщения пользователю {user_id}: {e}")

def register_handlers():
    dp.register_message_handler(send_notification, commands=['notification'])

