from aiogram import Bot, Dispatcher
import json
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import types
from aiogram.dispatcher.filters import BoundFilter



# Чтение токена из файла JSON
with open('config.json', 'r') as f:
    config = json.load(f)

bot = Bot(token=config['TOKEN'])
dp = Dispatcher(bot, storage=MemoryStorage())


