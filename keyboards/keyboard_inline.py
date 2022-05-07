from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


choice = InlineKeyboardMarkup(inline_keyboard=[
    [
        # В инлайн-кнопках важно передавать callback_data или другой дополнительный параметр
        # Если передавать просто текст работать не будет
        InlineKeyboardButton(text="Маленький текст 1", callback_data="buy:apple"),
        InlineKeyboardButton(text="Маленький текст 2", callback_data="buy:apple")
    ],
    [
        InlineKeyboardButton(text="Отмена", callback_data="buy:apple")
    ]
])