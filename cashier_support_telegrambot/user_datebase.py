
from create_bot import dp
from aiogram import types
from datetime import datetime
import sqlite3
from datetime import timedelta

def connect_db():
    conn = sqlite3.connect('user_datebase.db')
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            user_id TEXT,
            request TEXT,
            request_date TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS support_requests (
            id INTEGER PRIMARY KEY,
            user_id TEXT,
            request_date TEXT
        )
    """)
    conn.commit()
    return conn


def add_user(conn, user_id, request):
    request_date = datetime.now().isoformat()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (user_id, request, request_date) VALUES (?, ?, ?)", (user_id, request, request_date))
    conn.commit()

def get_users(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

def check_records(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM support_requests")
    count = cursor.fetchone()[0]
    return count

def add_support_request(conn, user_id):
    from create_bot import dp  # Перенесите импорт сюда
    request_date = datetime.now().isoformat()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO support_requests (user_id, request_date) VALUES (?, ?)", (user_id, request_date))
    conn.commit()

async def support(message: types.Message):
    conn = connect_db()
    add_support_request(conn, str(message.from_user.id))
    # Обработка запроса в техподдержку

async def handle_message(message: types.Message):
    conn = connect_db()
    add_user(conn, str(message.from_user.id), message.text)

@dp.message_handler(commands=['check_records'])
async def handle_check_records(message: types.Message):
    conn = connect_db()
    count = check_records(conn)
    if count == 0:
        await message.answer("В базе данных нет записей.")
    else:
        await message.answer(f"В базе данных {count} записей.")

@dp.message_handler(commands=['support'])
async def handle_support(message: types.Message):
    conn = connect_db()
    add_support_request(conn, str(message.from_user.id))
    await message.answer("Ваш запрос в техподдержку зарегистрирован.")

def get_support_stats(conn):
    cursor = conn.cursor()
    week_ago = (datetime.now() - timedelta(weeks=1)).isoformat()
    month_ago = (datetime.now() - timedelta(weeks=4)).isoformat()
    cursor.execute("SELECT COUNT(*) FROM support_requests WHERE request_date > ?", (week_ago,))
    week_count = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM support_requests WHERE request_date > ?", (month_ago,))
    month_count = cursor.fetchone()[0]
    return week_count, month_count

@dp.message_handler(commands=['stats'])
async def handle_stats(message: types.Message):
    conn = connect_db()
    week_count, month_count = get_support_stats(conn)
    await message.answer(f"Обращений в техподдержку за последнюю неделю: {week_count}\nОбращений в техподдержку за последний месяц: {month_count}")    