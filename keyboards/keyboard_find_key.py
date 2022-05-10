from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

keyboard_find_key_s = CallbackData("ask_support", "messages")

async def keyboard_find_key(messages, list, list_answer):
    """Функция, которая передает клавиатуру find"""
    keyboard = InlineKeyboardMarkup()
    for i in range(len(list)):
        keyboard.add(
            InlineKeyboardButton(
                text=list[i],
                callback_data=keyboard_find_key_s.new(
                    messages=messages,
                    answer=list_answer[i]
                )
            )
        )
    return keyboard