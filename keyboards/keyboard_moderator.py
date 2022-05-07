from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from create import dp

# Параметры кнопок: 1 - префикс (имя), 2.. - функциональные: то, что мы хотим сохранить о наших кнопках
# messages - параметр, который определяет, будет ли вестись диалог между пользователем и модератором
# или будет обмен одним сообщением
# as_user определяет, кто нажал данную кнопку: модератор или пользователь
support_callback = CallbackData("ask_support", "messages", "user_id", "as_user")

async def support_keyboard(messages, user_id = None):
    """Функция, которая передает нужную клавиатуру"""
    if user_id:
        # Если указан user_id, то данная клавиатура передается модератору
        contact_id = int(user_id)
        text = "Ответить пользователю"
        as_user = "no"
    else:
        # Данная клавиатура передается пользователю
        as_user = "yes"
        if messages == "one":
            text = "Написать 1 сообщение модератору"
        else:
            text = "Начать диалог с модератором"

    contact_id = 1970715638
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton(
            text=text,
            # В инлайн-кнопках важно передавать callback_data или другой дополнительный параметр
            # Если передавать просто текст работать не будет
            callback_data=support_callback.new(
                messages=messages,
                user_id=contact_id,
                as_user=as_user
            )
        )
    )

    return keyboard