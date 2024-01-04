from dispatcher import dp, bot
from aiogram.dispatcher import FSMContext
from aiogram import Dispatcher
from aiogram import types
import keyboards as kb
import asyncio
import sqlite3
import support



@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer("Привет! 👋 Я - бот-помощник Пекарни №5, созданный специально для поддержки наших кассиров.\n"
                          "Если у тебя возникли вопросы по работе кассы, ассортименту, ценам или ты столкнулся с какими-либо сложностями - пиши, и я постараюсь помочь! 🧾🥖", reply_markup=kb.start_keyboard)

@dp.message_handler(lambda message: message.text == 'Связаться c IIKO')
async def morning(message: types.Message):
    await message.answer("Чтобы обратиться в iiko перейдите по ссылке: t.me/RestoIT_support_bot", parse_mode='HTML')

@dp.message_handler(lambda message: message.text == 'Что делать утром?')
async def morning(message: types.Message):
    await message.answer("Выберите с чем у вас вопрос", reply_markup=kb.morning_keyboard)


@dp.message_handler(lambda message: message.text == 'Как начать смену?')
async def start_shift(message: types.Message):
    await message.answer("Чтобы начать смену, первым делом включите кофемашину и чайник.\n\n"
                     "Если вы не уверены, как это сделать, всегда можете спросить у бариста.\n\n"
                     "Не забудьте сделать утренний фотоотчет.\n\n"
                     "<b>Важно: все фотоотчеты должны быть сделаны до 8:00!</b>",
                         parse_mode='html', reply_markup=kb.morning_keyboard)


@dp.message_handler(lambda message: message.text == "Как сделать утренний фотоотчет?")
async def morning_report(message: types.Message):
    await message.answer("<b>Фотография открытой смены пример: </b>", parse_mode='HTML')
    await message.answer_photo('AgACAgIAAxkBAAIB_2WNC88qJeKDA9PmeNBkGpHj-cM3AAJi1DEbOyhpSE-3mCGXT7fLAQADAgADcwADMwQ')
    await message.answer("<b>Внешний вид смены пример: </b>", parse_mode='HTML')
    await message.answer_photo('AgACAgIAAxkBAAICCWWNDK3ADQw4swAB6ylgjZrOK3cr1wACt9AxGx_XaEiRU6BaYeLxiQEAAwIAA3MAAzME')
    await message.answer("<b>ВНИМАНИЕ!</b> \n"
    "Ваш внешний вид должен соответствовать стандартам: \n"
    "1. Однотонный низ и черный верх. \n "
    "2. Фартук и кепка соответственно (для девочек косынка).",
    parse_mode='HTML', reply_markup=kb.morning_keyboard)


@dp.message_handler(lambda message: message.text == "Как сделать выкладку витрины?")
async def display_case(message: types.Message):
    await message.answer("Витрина с выпечкой должна выглядеть так как на фото, не нужно наваливать друг на друга выпечку, "
        "она продавливается под весом, если у вас слишком много выпечки и она не помещается, "
        "можно отложить немного в контейнер. Всё выглядит аккуратно и красиво, так и должно быть.",
                         parse_mode='html')
    await message.answer_photo('AgACAgIAAxkBAAICGWWNDjw374D3VqpB_B9S_1zg_aWXAAK50DEbH9doSE-awpm-DeuGAQADAgADcwADMwQ')
    await message.answer("Расположение холодильной витрины\n"
        "Первая полочка: Макарунсы, Эклеры, немного пирожных, пончики\n"
        "Вторая полка: пирожные\n"
        "Третья полка: чизкейки\n\n"
        "<b><i>Важно!!! Чтобы десерты не выходили за подложки, а круассаны за крафт бумагу!!</i></b>", parse_mode='HTML', reply_markup=kb.morning_keyboard)
    await message.answer_photo('AgACAgIAAxkBAAICG2WNDpHdp-tQL1Wkh70Kjpb5TK1-AAK60DEbH9doSFlSA9Nci7krAQADAgADcwADMwQ')


@dp.message_handler(lambda message: message.text == "Как заполнить стоп-лист?")
async def stop_list(message: types.Message):
    await message.answer("После того как все десерты и выпечка выложены, и вы выглядите нормально для "
        "работника общепита, а ваши мешки под глазами можно заправлять в штаны, пришло время вбивать стоп-лист. Выпечку и десерты нужно "
        "обязательно пересчитать, чтобы избежать расхождений в инвентаре.")
    await message.answer("Заходим в меню, это можно сделать нажав три полоски сверху, само меню выглядит так:", parse_mode='HTML')
    await message.answer_photo('AgACAgIAAxkBAAICNWWND43hm2hkh3NHidjiunWgBzUiAAK80DEbH9doSCOldwExvlGUAQADAgADcwADMwQ')
    await message.answer("Вам нужно нажать кнопку 'Стоп-лист'. Это меню стоп листа, в котором вы начинаете забивать "
        "количество позиций по списку, который вы пересчитали.", parse_mode='HTML')
    await message.answer_photo('AgACAgIAAxkBAAICN2WND-1JDjL59fLE3q8bheBTj06SAAK90DEbH9doSA767TfByM9IAQADAgADcwADMwQ')
    await message.answer_photo('AgACAgIAAxkBAAICOWWNEAAB61eL7Bnd8a2I1NyZhdg2MwACv9AxGx_XaEiG_G3LqROjFQEAAwIAA3MAAzME')


@dp.message_handler(lambda message: message.text == 'В главное меню')
async def back_to_main(message: types.Message):
    await cmd_start(message)


@dp.message_handler(lambda message: message.text == 'Группы WhatsApp')
async def whatsapp_groups(message: types.Message):
    await message.answer('<b>Группа Фотоотчеты</b>\nВ этой группе вы найдете фотографии витрин, готовности к смене и вечерних закрытий, а также документацию о порядке. График отправки фото витрин: 8:00, 11:00, 14:00, 16:00, 18:00, 20:00.', parse_mode='HTML')
    await message.answer("https://chat.whatsapp.com/JYReiQqivHbIywlce2TsLt", parse_mode='HTML')
    await message.answer('<b>Группа Стоп лист</b>\nЗдесь вы можете скидывать всё, что ставится на стоп, а также списанную выпечку и чаи.', parse_mode='HTML')
    await message.answer("https://chat.whatsapp.com/DQCd3MsqHyy27sweqJCAyZ", parse_mode='HTML')
    await message.answer('<b>Группа ЦЕХ+МАГАЗИН</b>\nГруппа цех нужна для связи магазинов и цеха\nСюда мы скидываем если вам или гостям кажется что с выпечкой и десертами что-то не так\n'
            "Сюда скидываем таблицы с остатками десертов, и хлеба.\n"
         "Сюда мы скидываем фото тетради прихода десертов.", parse_mode='HTML')
    await message.answer("https://chat.whatsapp.com/KSpXBCSHBvJ5k0t3Yfs40K", parse_mode='HTML')
    await message.answer('<b>Группа Предзаказы</b>\nСюда вы отправляете предзаказы на хлеб, выпечку, десерты и тортики', parse_mode='HTML')
    await message.answer("https://chat.whatsapp.com/DYuDWOluhwsFX15yOTAqkd", parse_mode='HTML')
    await message.answer('<b>Номер оператора</b>\nОператор связывается с вами по поводу доставок, самовывозу, выпечки или предзаказу, а также другим вопросам.', parse_mode='HTML')
    await message.answer("https://wa.me/77004755542", parse_mode='HTML')
    await message.answer('<b>Группа Закуп</b>\nСюда вы скидываете ревизии, накладные и пишете по поводу того что вам нужно на точку', parse_mode='HTML')
    await message.answer("https://chat.whatsapp.com/F7SviwgDBWB6C3Ia05jhMg", parse_mode='HTML')
    await message.answer('<b>Хоз Вопросы</b>\nСюда мы пишем, если у вас отключили свет, воду, или если у вас сломалось что то на точке. Для связи с хаус мастером и тех. Директором.', parse_mode='HTML')
    await message.answer("https://chat.whatsapp.com/IQWRemDxIt50BqN1mF3eHB", parse_mode='HTML')
    await message.answer('<b>Важная Информация</b>\nСюда пишут все нововведения, расписание, а также всю важную информацию', parse_mode='HTML')
    await message.answer("https://chat.whatsapp.com/Bqj31wIXfQiJiFZgFiTs6s", parse_mode='HTML')


@dp.message_handler(lambda message: message.text == "Телеграм отчет")
async def stop_list(message: types.Message):
    await message.answer("Бета тест, ЖДЕМ ЛЕШУ\n" 
                         "<b>ЛЕША^ ПРИДИ!!!!</b>",parse_mode='HTML', reply_markup=kb.telegram_keyboard)


@dp.message_handler(lambda message: message.text == "Таблица остатков десертов, хлеба")
async def stop_list(message: types.Message):
    await message.answer("Конкретнее)", reply_markup=kb.telegram_keyboard)
    await message.answer_photo('AgACAgIAAxkBAAICpGWNG3xwJqd_1eb7rQ7PhdlH28GSAALr0DEbH9doSF82Mi4ZH0znAQADAgADcwADMwQ')
    await message.answer_photo('AgACAgIAAxkBAAICpmWNG9wEgz1WMiI7AkJFGiDttWLNAALv0DEbH9doSC8YYlSot4xvAQADAgADcwADMwQ')

@dp.message_handler(lambda message: message.text == "Заполненный инкассационный бланк")
async def stop_list(message: types.Message):
    await message.answer("Конкретнее)", reply_markup=kb.telegram_keyboard)
    await message.answer_photo('AgACAgIAAxkBAAICpGWNG3xwJqd_1eb7rQ7PhdlH28GSAALr0DEbH9doSF82Mi4ZH0znAQADAgADcwADMwQ')
    await message.answer_photo('AgACAgIAAxkBAAICpmWNG9wEgz1WMiI7AkJFGiDttWLNAALv0DEbH9doSC8YYlSot4xvAQADAgADcwADMwQ')