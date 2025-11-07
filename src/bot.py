from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           WebAppInfo)

dp = Dispatcher()


@dp.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    web_app_info = WebAppInfo(url="https://pinecv.onrender.com/")
    button_text = "Launch"
    web_app_button = KeyboardButton(text=button_text, web_app=web_app_info)

    keyboard = ReplyKeyboardMarkup(
        keyboard=[[web_app_button]], resize_keyboard=True
    )
    await message.answer(
        "Click the button to open the PineCV application.",
        reply_markup=keyboard,
    )


async def run(token: str) -> None:
    bot = Bot(token=token)
    await dp.start_polling(bot)
