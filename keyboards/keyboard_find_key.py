from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

support_callback = CallbackData("ask_support", "messages")

async def keyboard_find_key(messages, list):
    """Функция, которая передает клавиатуру find"""
    keyboard = InlineKeyboardMarkup()
    for i in range(len(list)):
        keyboard.add(
            InlineKeyboardButton(
                text=list[i],
                callback_data=support_callback.new(
                    messages=messages
                )
            )
        )
    return keyboard