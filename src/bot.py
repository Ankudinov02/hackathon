from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           WebAppInfo)

dp = Dispatcher()


@dp.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    await message.answer("Click the button to open the PineCV application.")


async def run(token: str) -> None:
    bot = Bot(token=token)

    web_app_info = WebAppInfo(
        url="https://pineapplebot-8f21292e4ac9.herokuapp.com/"
    )
    button_text = "Launch"
    web_app_button = KeyboardButton(text=button_text, web_app=web_app_info)

    _ = ReplyKeyboardMarkup(keyboard=[[web_app_button]], resize_keyboard=True)

    await dp.start_polling(bot)
