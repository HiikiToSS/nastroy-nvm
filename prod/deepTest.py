import matplotlib.pyplot as plt
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import BufferedInputFile
from io import BytesIO
import asyncio
from dotenv import load_dotenv
import os
load_dotenv()

# Ваши данные (день -> значение)
data = {
    "День": [1, 2, 3, 4, 5],
    "Значение": [9, 14, 7, 8, 12]
}

bot = Bot(token=os.getenv("TG_BOT_TOKEN"))
dp = Dispatcher()

def generate_simple_plot():
    """Генерирует линейный график с фиксированными осями"""
    plt.figure(figsize=(8, 5))
    
    # Создаём график
    plt.plot(data["День"], data["Значение"], 
             marker='o', 
             color='blue',
             linestyle='-',
             linewidth=2)
    
    # Настройки осей
    plt.ylim(0, 15)  # Фиксированный диапазон от 0 до 15
    plt.xlim(min(data["День"]) - 0.5, max(data["День"]) + 0.5)  # Небольшие отступы по X
    
    # Подписи и оформление
    plt.title("График данных (шкала 0-15)", pad=20)
    plt.xlabel("День", labelpad=10)
    plt.ylabel("Значение", labelpad=10)
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Добавляем горизонтальные линии для удобства
    for y in range(0, 16, 5):  # Линии через каждые 5 единиц
        plt.axhline(y=y, color='gray', linestyle=':', alpha=0.3)
    
    # Сохраняем в буфер
    buf = BytesIO()
    plt.savefig(buf, format='png', dpi=120, bbox_inches='tight')
    buf.seek(0)
    plt.close()
    return buf

@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.answer(
        "📈 Бот для генерации графиков\n"
        "Отправьте /graph чтобы получить график с фиксированной шкалой (0-15)"
    )

@dp.message(Command("graph"))
async def send_graph(message: types.Message):
    plot = generate_simple_plot()
    image = BufferedInputFile(plot.getvalue(), filename="graph.png")
    await message.answer_photo(image, caption="График данных (шкала 0-15)")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())