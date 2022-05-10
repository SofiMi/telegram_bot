from aiogram.dispatcher.filters import Command

from create import dp, bot
from keyboards.keyboard_find import keyboard_find
from keyboards.keyboard_find import support_callback
from keyword_search.search import search_message
from keyboards.keyboard_find_key import keyboard_find_key, keyboard_find_key_s
from sql.sql_handling import SQL

@dp.message_handler(Command("find"))
async def start_find(message):
    """Cообщение, которое высвечивается при запросе поиска похожих сообщений"""
    text = "Хотите найти похожее сообщение?"
    keyboard = await keyboard_find(messages="find")
    await message.answer(text, reply_markup=keyboard)


@dp.callback_query_handler(support_callback.filter(messages="find"))
async def click_on_the_button_find(call, state, callback_data):
    """Функция, которая обрабатывает нажатие на кнопку отправки сообщения"""
    await call.answer()
    await call.message.answer("Задайте вопрос")
    await state.set_state("find_message")


@dp.message_handler(state="find_message")
async def get_support_message_find(message, state):
    "Функция, которая выводит потенциально нужные вопросы из базы данных"
    sql = SQL("sql/faq.db")
    text_n = str(message.text)
    keys = []
    sql_key = list(sql.dict_factory())
    for key in sql_key:
        keys.append(key[0])
    new_keys = set(await search_message(text_n)) & set(keys)
    list_ques = []
    list_answ = []
    for n_key in new_keys:
        for old_key in sql_key:
            if n_key == old_key[0]:
                list_ques.append(old_key[1])
                list_answ.append(old_key[2])
    keyboard = await keyboard_find_key("find_key", list_ques, list_answ)
    await message.answer("Вас интересует что-то из этих вопросов? Если вы не нашли нужную информацию, то "
                         "нажмите /support или /support_call", reply_markup=keyboard)

    await state.reset_state()
    sql.close()

@dp.callback_query_handler(keyboard_find_key_s.filter(messages="find_key"))
# Декоратор оборачивает функцию, когда нажимается кнопка с отправкой одного сообщения модератору
async def click_on_ques(call, callback_data):
    """Функция, которая обрабатывает нажатие на кнопку отправки сообщения"""
    await call.answer()
    await call.message.answer(f"{callback_data.get('answer')}")
