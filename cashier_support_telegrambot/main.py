# main.py

from aiogram import executor
from dispatcher import dp, bot
import admin
from support import support
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from user_datebase import connect_db, add_user, get_users, check_records

async def on_startup(_):
    print('Бот запущен')

from notification import register_handlers
register_handlers()

if __name__ == '__main__':
    dp.register_message_handler(support, lambda message: message.text == "Написать в техподдержку", state="*")
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)