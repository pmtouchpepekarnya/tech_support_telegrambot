from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Основная клавиатура
start_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Что делать утром?")],
        [KeyboardButton(text="Группы WhatsApp")],
        [KeyboardButton(text="Телеграм отчет")],
        [KeyboardButton(text="Написать в техподдержку")],
        [KeyboardButton(text="Связаться c IIKO")]
    ],
    resize_keyboard=True
)

# Клавиатура для техподдержки
support_button = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="Написать в техподдержку")]],
    resize_keyboard=True
)

# Клавиатура для утренних действий
morning_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Как начать смену?")],
        [KeyboardButton(text="Как сделать утренний фотоотчет?")],
        [KeyboardButton(text="Как сделать выкладку витрины?")],
        [KeyboardButton(text="Как заполнить стоп-лист?")],
        [KeyboardButton(text="В главное меню")]
    ],
    resize_keyboard=True
)

# Клавиатура для WhatsApp групп
whatsapp_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Как начать смену?")],
        [KeyboardButton(text="Как сделать утренний фотоотчет?")],
        [KeyboardButton(text="Как сделать выкладку витрины?")],
        [KeyboardButton(text="Как заполнить стоп-лист?")],
        [KeyboardButton(text="В главное меню")]
    ],
    resize_keyboard=True
)

# Клавиатура для Telegram отчетов
telegram_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Таблица остатков десертов, хлеба")],
        [KeyboardButton(text="Z-отчет по айке и Заполненный инкассационный бланк")],
        [KeyboardButton(text="Чеки изъятий, любимые гости, и карты блогера")],
        [KeyboardButton(text="Каспи терминал с отчетом по продажам за весь день")],
        [KeyboardButton(text="Z-отчёт по веб кассе")],
        [KeyboardButton(text="Заполнить текстовую таблицу")],
        [KeyboardButton(text="В главное меню")]
    ],
    resize_keyboard=True
)
