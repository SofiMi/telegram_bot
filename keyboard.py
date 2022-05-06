from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    # Текстовые кнопки
    keyboard=[
        [
            # Первая строка наших кнопок
            KeyboardButton(text="Большааая кнопка"),
        ],
        [
            # Вторая строка: содержит две кнопки
            KeyboardButton(text="Парная кнопка 1"),
            KeyboardButton(text="Парная кнопка 2")
        ],
    ],
    # Необходимо, чтобы наши кнопки не занимали много пространства
    resize_keyboard=True
)