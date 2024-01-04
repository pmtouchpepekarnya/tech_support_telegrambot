import json
import aiosqlite
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dispatcher import dp, bot


# Загрузка ID администратора из файла config.json
with open('config.json') as f:
    config = json.load(f)
ADMIN_ID = int(config['ADMIN_ID'])


def register_handlers():
    from support import support
    dp.register_message_handler(support, lambda message: message.text == "Написать в техподдержку", state="*")
    
register_handlers()

async def on_startup(dispatcher: Dispatcher):
    # Логика, выполняемая при запуске бота
    await bot.send_message(chat_id=config['ADMIN_ID'], text='Бот запущен')
    dispatcher.storage = await aiosqlite.connect('my_database.db')

async def on_shutdown(dispatcher: Dispatcher):
    # Логика, выполняемая при остановке бота
    await bot.send_message(chat_id=config['ADMIN_ID'], text='Бот остановлен')
    await dispatcher.storage.close()
