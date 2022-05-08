from aiogram.dispatcher.filters import Command

from create import dp, bot
from keyboards.keyboard_find import keyboard_find
from keyboards.keyboard_find import support_callback
from keyword_search.search import search_message
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
    text_n = str(message.text)
    new_text = await search_message(text_n)
    await message.answer(f"Вы отправили это сообщение {new_text}!")
    # Передаем данные модератору/пользователю
    await state.reset_state()
