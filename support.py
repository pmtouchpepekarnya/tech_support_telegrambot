import asyncio
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards import start_keyboard, support_button
from aiogram.utils.exceptions import NetworkError
from dispatcher import dp, bot
from aiogram.dispatcher import FSMContext


class SupportState(StatesGroup):
    waiting_for_support_request = State()
    in_conversation = State()


# ID чата техподдержки - замените на реальный ID
SUPPORT_CHAT_ID = -1002121131295





@dp.message_handler(state=SupportState.waiting_for_support_request)
async def get_support_request(message: types.Message, state: FSMContext):
    from user_datebase import add_support_request , connect_db
    conn = connect_db()
    add_support_request(conn, str(message.from_user.id))
    await bot.send_message(SUPPORT_CHAT_ID, f"Пользователь {message.from_user.id} отправил запрос: {message.text}\n"
                          f"/reply {message.from_user.id} ")
    await message.answer("Ваш запрос был отправлен в техподдержку")
    await state.set_state(SupportState.in_conversation)

@dp.message_handler(content_types=types.ContentType.PHOTO, state=[SupportState.waiting_for_support_request, SupportState.in_conversation])
async def handle_photo(message: types.Message, state: FSMContext):
    await bot.send_message(SUPPORT_CHAT_ID, f"Пользователь {message.from_user.id} отправил фотографию:")
    await bot.forward_message(chat_id=SUPPORT_CHAT_ID, from_chat_id=message.chat.id, message_id=message.message_id)
    await message.answer("Ваш запрос был отправлен в техподдержку")

@dp.message_handler(content_types=types.ContentType.VIDEO, state=[SupportState.waiting_for_support_request, SupportState.in_conversation])
async def handle_video(message: types.Message, state: FSMContext):
    await bot.send_message(SUPPORT_CHAT_ID, f"Пользователь {message.from_user.id} отправил видеосообщение:")
    await bot.forward_message(chat_id=SUPPORT_CHAT_ID, from_chat_id=message.chat.id, message_id=message.message_id)
    await message.answer("Ваш запрос был отправлен в техподдержку")

@dp.message_handler(content_types=types.ContentType.VOICE, state=[SupportState.waiting_for_support_request, SupportState.in_conversation])
async def handle_voice(message: types.Message, state: FSMContext):
    await bot.send_message(SUPPORT_CHAT_ID, f"Пользователь {message.from_user.id} отправил голосовое сообщение:")
    await bot.forward_message(chat_id=SUPPORT_CHAT_ID, from_chat_id=message.chat.id, message_id=message.message_id)
    await message.answer("Ваш запрос был отправлен в техподдержку")

@dp.message_handler(state=SupportState.in_conversation)
async def handle_support_conversation(message: types.Message):
    await bot.send_message(SUPPORT_CHAT_ID, f"Пользователь {message.from_user.id} отправил сообщение: {message.text}")
    await message.answer("Ваше сообщение было отправлено в техподдержку.\n")

@dp.message_handler(commands='reply')
async def reply_command(message: types.Message):
    user_id, reply_text = message.text.split(maxsplit=2)[1:]
    try:
        await bot.send_message(user_id, reply_text)
    except NetworkError:
        await asyncio.sleep(1)  
        await bot.send_message(user_id, reply_text)
    await message.answer("Ответ успешно отправлен")
    await message.answer(f"Закончить обращение: /end_conversation {message.from_user.id} ")

@dp.message_handler(commands='end_conversation', is_chat_admin=True)
async def end_conversation(message: types.Message, state: FSMContext):
    args = message.get_args()
    if not args:
        await message.answer("Пожалуйста, укажите ID пользователя.")
        return

    user_id = int(args)  # Преобразуем аргумент в число, чтобы получить ID пользователя
    
    # Создаем новый FSMContext для пользователя, чье состояние нужно сбросить
    user_state = Dispatcher.get_current().current_state(chat=user_id, user=user_id)
    await user_state.reset_state(with_data=False)  # Сбрасываем состояние пользователя
    
    # Отправляем пользователю сообщение о завершении разговора
    try:
        await bot.send_message(user_id, "Разговор завершен. Если у вас есть еще какие-то вопросы, обращайтесь снова.")
        await message.answer(f"Разговор с пользователем {user_id} успешно завершен.")
    except Exception as e:
        await message.answer(f"Произошла ошибка при отправке сообщения пользователю {user_id}: {e}")

    # Сбрасываем состояние оператора техподдержки
    await state.finish()

async def handle_support_conversation(message: types.Message, state: FSMContext):
    try:
        if message.text.startswith('/reply'):
            user_id, text = message.text.split(' ', 2)[1:]
            await bot.send_message(user_id, text)
        elif message.text.startswith('/end_conversation'):
            user_id = message.text.split(' ', 1)[1]
            await bot.send_message(user_id, "Разговор завершён. Если у вас возникнут дополнительные вопросы, напишите в техподдержку.")
            await state.reset_state(with_data=False)
        else:
            await message.answer("Ваше сообщение было отправлено в техподдержку.\n")
    except IndexError:
        await message.answer("Ошибка: неправильный формат команды.")
    except Exception as e:
        await message.answer(f"Произошла ошибка: {str(e)}")

async def support(message: types.Message, state: FSMContext):
    await message.answer("Пожалуйста, введите ваш запрос в техподдержку.")
    await state.set_state(SupportState.waiting_for_support_request)
    from user_datebase import add_support_request
    from user_datebase import connect_db
    conn = connect_db()
    add_support_request(conn, str(message.from_user.id))

async def get_id_command(message: types.Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    await message.answer(f"ID чата: {chat_id}\nID пользователя: {user_id}")

def register_handlers_support(dp: Dispatcher):
    dp.register_message_handler(support, lambda message: message.text == "Написать в техподдержку", state=None)
    dp.register_message_handler(get_support_request, state=SupportState.waiting_for_support_request)
    dp.register_message_handler(handle_support_conversation, state=SupportState.in_conversation)
    dp.register_message_handler(end_conversation, commands=['end_conversation'], state=SupportState.in_conversation)
    dp.register_message_handler(get_id_command, commands='getid')

    