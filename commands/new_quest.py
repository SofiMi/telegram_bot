from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from sql.sql_handling import SQL
from keyword_search.search import search_message

from create import dp

class Test(StatesGroup):
    add_quest = State()
    add_answ = State()

@dp.message_handler(Command("new_quest"), state=None)
async def enter_add(message: types.Message):
    await message.answer("Введите вопрос")
    await Test.add_quest.set()


@dp.message_handler(state=Test.add_quest)
async def add_question(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(quest=answer)
    await message.answer("Введите ответ на вопрос")
    await Test.next()

@dp.message_handler(state=Test.add_answ)
async def add_answer(message: types.Message, state: FSMContext):
    # Достаем переменные
    data = await state.get_data()
    quest = data.get("quest")
    answ = message.text

    key_word = await search_message(quest)

    sql = SQL("sql/faq.db")
    sql.add_question(quest, answ)

    for word in key_word:
        if not sql.find_key_word(word):
            sql.add_keys(word, sql.get_number(quest)[0])
        else:
            sql.update_number(word, sql.get_number(quest)[0])
    sql.close()

    await message.answer("Спасибо за проделанную работу!")
    await state.finish()