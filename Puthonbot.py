from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = Bot('7865712822:AAHNyLmjKtL146KjRmWqTkn6b23mFUac2Q8')
dp = Dispatcher(bot)

WEBAPP_URL = "https://parfenmarkevich.github.io/webapp-shop/"

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    # Создаем кнопку с WebApp
    webapp_button = InlineKeyboardButton(
        text="Магазин",
        web_app=types.WebAppInfo(url=WEBAPP_URL)
    )
    keyboard = InlineKeyboardMarkup().add(webapp_button)

    await message.answer(
        "Добро пожаловать в наш магазин! Нажмите на кнопку ниже, чтобы сделать покупку.",
        reply_markup=keyboard
    )

executor.start_polling(dp)
