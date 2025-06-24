import os
import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from dotenv import load_dotenv
load_dotenv()


async def echo(message: Message) -> None:
    await message.answer(message.text)
    print(message.text)


async def main() -> None:
    bot_token = os.getenv("TG_BOT_TOKEN")

    dp = Dispatcher()
    dp.message.register(echo, F.text)

    bot = Bot(token=bot_token)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())