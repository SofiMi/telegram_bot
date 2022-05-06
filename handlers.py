from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove

from main import bot, dp
from config import admin_id
from keyboard import menu

async def send_to_admin(*args):
    await bot.send_message(chat_id=admin_id, text="Бот запущен")


"""@dp.message_handler()
async def echo(message: Message):
    text = f"Привет, ты написал: {message.text}"
    await message.reply(text=text)"""


@dp.message_handler(Command("menu"))
async def show_keyboard(message):
    """Команда, отвечающая за вывод текстовых кнопок"""
    # Вызывается командой /menu
    await message.answer("Кнопки", reply_markup=menu)



@dp.message_handler(Text(equals=["Большааая кнопка", "Парная кнопка 1", "Парная кнопка 2"]))
# В случае передачи неправильного названия кнопки, бот не будет на нее реагировать при нажатии
async def get_keyboard(message):
    """Команда, отвечающая за использование текстовых кнопок"""
    await message.answer(f"Вы выбрали {message.text}. Спасибо", reply_markup=ReplyKeyboardRemove())