from aiogram.dispatcher.filters import Command

from create import dp, bot
from keyboards.keyboard_find import keyboard_find
from keyboards.keyboard_find_key import keyboard_find_key,keyboard_find_key_s
from keyboards.keyboard_find import support_callback
from keyword_search.search import search_message
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

    list_ques = []
    list_answ = []

    # Находим ключевые слова
    text_n = str(message.text)
    key_list = await search_message(text_n)

    # Проходимся по базе данных и вносим в словарик
    dict_numb = {}
    sql_key = list(sql.dict_factory())
    for key_n in key_list:
        for key_o in sql_key:
            if key_n == key_o[0]:
                number_list = key_o[1].split(" ")
                for key in number_list:
                    if key in dict_numb:
                        dict_numb[key] += 1
                    else:
                        dict_numb[key] = 1

    # Проверяем сколько раз встретился вопрос
    for key in dict_numb:
        if dict_numb[key] >= 2:
            list_ques.append(list(sql.get_quest_for_number(key))[0])
            list_answ.append(key)

    keyboard = await keyboard_find_key("find_key", list_ques, list_answ)
    await message.answer("Вас интересует что-то из этих вопросов? Если вы не нашли нужную информацию, то "
                         "нажмите /support или /support_call", reply_markup=keyboard)

    await state.reset_state()
    sql.close()

@dp.callback_query_handler(keyboard_find_key_s.filter(messages="find_key"))
# Декоратор оборачивает функцию, когда нажимается кнопка с отправкой одного сообщения модератору
async def click_on_ques(call, callback_data):
    """Функция, которая обрабатывает нажатие на кнопку отправки сообщения"""
    sql = SQL("sql/faq.db")
    await call.answer()
    await call.message.answer(f"{list(sql.get_answ_for_number(callback_data.get('answer')))[0]}")
    sql.close()