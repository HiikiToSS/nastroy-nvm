import matplotlib.pyplot as plt
from io import BytesIO


#потом вытаскивать из файла с бд
data = {
    "День": [1, 2, 3, 4, 5],
    "Значение": [9, 14, 7, 8, 12]
}

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