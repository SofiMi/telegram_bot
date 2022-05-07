from aiogram import types
from aiogram.dispatcher.filters import Command

from keyboards.keyboard_moderator import support_keyboard
from create import dp
from keyboards.keyboard_inline import choice

@dp.message_handler(Command("support"))
async def ask_support(message: types.Message):
    """Сообщение отправки одного сообщения модератору"""
    text = "Хотите написать сообщение модератору? Нажмите на кнопку ниже!"
    # messages - параметр, который определяет, будет ли вестись диалог между пользователем и модератором
    # или будет обмен одним сообщением
    keyboard = await support_keyboard(messages="one")
    await message.answer(text, reply_markup=keyboard)
