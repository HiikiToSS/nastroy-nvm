from aiogram import Bot, Dispatcher, types, F, Router
from aiogram.filters import Command, StateFilter
from aiogram.types import BufferedInputFile, Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import asyncio
from dotenv import load_dotenv
import os
from datetime import *

from photoGenerator import generate_simple_plot
from db import addMood

load_dotenv()

bot = Bot(token=os.getenv("TG_BOT_TOKEN"))
dp = Dispatcher()


async def send_notif():
    target_time = time(3, 16)  # интересующее время
    while True:
        now = datetime.now().time()
        if now.hour == target_time.hour and now.minute == target_time.minute:
            await bot.send_message(chat_id=1895572923, text="⏰ Время   пришло!")
            await asyncio.sleep(61)  # чтобы не спамить слип на 61 сек
        await asyncio.sleep(30)  # прерывание каждые 30 сек

@dp.message(Command("start"))
async def send_welcome(message: Message):
    await message.answer(
        "📈 Бот для мониторинга состояния пациента жёлтого дома"
    )




@dp.message(Command("help"))
async def send_nudes(message: Message):
    await message.answer('команды: \n/start \n/graph \n/mood \nили любая хрень - тоже отвечу, но по-тупому')


# Определяем состояние
class MoodForm(StatesGroup):
    waiting_for_mood = State()

# Хэндлер для команды /mood
@dp.message(Command(commands=["mood"]))
async def start_mood(message: types.Message, state: FSMContext):
    await message.reply("Как настроение (0–15)?")
    await state.set_state(MoodForm.waiting_for_mood)

# Хэндлер для обработки ответа

'''
юзер может ставить оценку 0+ раз за сутки, соответственно нужно это ограничить:
 - говорить, что сегодня он уже поставил оценку
 - предлагать изменить уже поставленную
'''


@dp.message(StateFilter(MoodForm.waiting_for_mood))
async def process_mood(message: types.Message, state: FSMContext):
    try:
        mood = int(message.text)
        if 0 <= mood <= 15:
            # Здесь будет код для сохранения в MongoDB
            await message.reply(f"Настроение {mood} записано!")
            print(mood, message.from_user.id)
            addMood(mood, message.from_user.id)
            await state.clear()  # Завершаем состояние
        else:
            await message.reply("Число должно быть от 0 до 15. Попробуй ещё раз.")
    except ValueError:
        await message.reply("Введи число, а не текст!")



@dp.message(Command("graph"))
async def send_graph(message: Message):
    plot = generate_simple_plot(message.from_user.id)
    image = BufferedInputFile(plot.getvalue(), filename="graph.png")
    await message.answer_photo(image, caption="График данных (шкала 0-15)")




#НИЖЕ ВСЕХ ДРУГИХ ОБРАБТЧИКОВ
@dp.message(F.text)
async def handle_hello(message: Message):
    await message.answer("Не хочу тыкать пальцем, но:\n - либо кому-то впадлу нажать /help\n - либо кто-то придурок")

async def main():
    asyncio.create_task(send_notif())
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())