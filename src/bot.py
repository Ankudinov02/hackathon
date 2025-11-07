from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup, InlineKeyboardMarkup,
                           WebAppInfo, InlineKeyboardButton)

dp = Dispatcher()
WEBAPP_URL = "https://pinecv.onrender.com/"


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    keyboard = InlineKeyboardMarkup().add(
        InlineKeyboardButton(
            text="Open the app",
            web_app=WebAppInfo(url=WEBAPP_URL)
        )
    )
    await message.answer("Press the button to open the app", reply_markup=keyboard)


async def run(token: str) -> None:
    bot = Bot(token=token)
    await dp.start_polling(bot)
