import logging
from aiogram import Dispatcher
from config import ADMINS


async def send_start_to_admin(dp: Dispatcher):
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, "Бот Запущен")

        except Exception as err:
            logging.exception(err)