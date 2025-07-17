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

# from db import addMood

load_dotenv()

bot = Bot(token=os.getenv("TG_BOT_TOKEN"))
dp = Dispatcher()


async def send_notif():
    target_time = time(3, 16)  # интересующее время
    while True:
        now = datetime.now().time()
        if now.hour == target_time.hour and now.minute == target_time.minute:
            await bot.send_message(chat_id=1895572923, text="⏰ Время пришло!")
            await asyncio.sleep(61)  # чтобы не спамить слип на 61 сек
        await asyncio.sleep(30)  # прерывание каждые 30 сек

@dp.message(Command("start"))
async def send_welcome(message: Message):
    await message.answer(
        "📈 Бот для генерации графиков\n"
        "Отправьте /graph чтобы получить график"
    )


@dp.message(Command("help"))
async def send_nudes(message: Message):
    await message.answer('комманды: \n/start \n/graph \n/mood \nили любая хрень - тоже отвечу, но по-тупому')


# Создаём Router вместо Dispatcher для модульности
router = Router()

# Определяем состояние
class MoodForm(StatesGroup):
    waiting_for_mood = State()

# Хэндлер для команды /mood
@router.message(Command(commands=["mood"]))
async def start_mood(message: types.Message, state: FSMContext):
    await message.reply("Как настроение (0–15)?")
    await state.set_state(MoodForm.waiting_for_mood)

# Хэндлер для обработки ответа
@router.message(StateFilter(MoodForm.waiting_for_mood))
async def process_mood(message: types.Message, state: FSMContext):
    try:
        mood = int(message.text)
        if 0 <= mood <= 15:
            # Здесь будет код для сохранения в MongoDB
            await message.reply(f"Настроение {mood} записано!")
            await state.finish()  # Завершаем состояние
        else:
            await message.reply("Число должно быть от 0 до 15. Попробуй ещё раз.")
    except ValueError:
        await message.reply("Введи число, а не текст!")



@dp.message(Command('setN'))
async def send_N(message: Message):
    global currUserId
    currUserId = message.from_user.id
    await message.answer("Как жизнь? (0-15)")

@dp.message(Command("graph"))
async def send_graph(message: Message):
    plot = generate_simple_plot()
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