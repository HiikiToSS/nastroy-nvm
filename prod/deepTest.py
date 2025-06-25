from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import BufferedInputFile, Message

import asyncio
from dotenv import load_dotenv
import os
from datetime import *
load_dotenv()
from photoGenerator import generate_simple_plot


bot = Bot(token=os.getenv("TG_BOT_TOKEN"))
dp = Dispatcher()


async def send_notif():
    target_time = time(3, 16)  # интересующее время
    while True:
        now = datetime.now().time()
        if now.hour == target_time.hour and now.minute == target_time.minute:
            await bot.send_message(chat_id=1895572923, text="⏰ Время пришло!")
            await asyncio.sleep(61)  # чтобы не спамить слип на 61 сек
        await asyncio.sleep(30)  # прерывание каждые 10 сек

@dp.message(Command("start"))
async def send_welcome(message: Message):
    await message.answer(
        "📈 Бот для генерации графиков\n"
        "Отправьте /graph чтобы получить график"
    )

@dp.message(Command("graph"))
async def send_graph(message: Message):
    plot = generate_simple_plot()
    image = BufferedInputFile(plot.getvalue(), filename="graph.png")
    await message.answer_photo(image, caption="График данных (шкала 0-15)")


#НИЖЕ ВСЕХ ДРУГИХ ОБРАБТЧИКОВ
@dp.message(F.text)
async def handle_hello(message: Message):
    await message.answer("Не хочу тыкать пальцем, но:\n - либо кому-то впадлу нажать /start\n  либо кто-то придурок")
    # users.insert_one(message.text)

async def main():
    asyncio.create_task(send_notif())
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())