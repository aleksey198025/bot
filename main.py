from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from db import DataBase

name_db = "bot.db"

db_client = DataBase(name_db)

TOKEN = "6903817748:AAF0XbjrRgl6A4jE70iwvRPH0AzS_xE3Q2o"

# FUNCTION


# BUTTONS


# KEYBOARDS


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


# bot launch handling
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    tg_id = int(message.from_user.id)
    db_client.add_user(tg_id, "start")
    await message.reply(f'Привет, {message.from_user.first_name}, бот отправляет то, что ему ввели')


# handling incoming messages
# @dp.message_handler()


if __name__ == '__main__':
    executor.start_polling(dp)
