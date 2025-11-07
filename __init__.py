import asyncio
import os

from dotenv import load_dotenv

import static_check as sc
from src import bot

if __name__ == "__main__":
    load_dotenv()

    TESTING = os.getenv("TESTING", "False") == "True"
    TOKEN = os.getenv("BOT_TOKEN")

    if TESTING:
        sc.run_utils()

    asyncio.run(bot.run(str(TOKEN)))
