import asyncio
from aiogram import executor

from set_moderator import set_default_commands
from create import dp
from send_to_admin import send_start_to_admin

async def on_startup(dp):
    # Уведомляет про запуск
    await set_default_commands(dp)
    await send_start_to_admin(dp)

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)