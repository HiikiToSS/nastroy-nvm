import matplotlib.pyplot as plt
from io import BytesIO
from db import get_userMood



#потом вытаскивать из файла с бд
data = {
    "День": [a['date'] for a in get_userMood()],
    "Значение": [a['mood'] for a in get_userMood()]
}


'''
данных будет дохера?
данных будет дохера

соответственно нужно будет делать 3 опции: стата за неделю, за месяц (подписи раз в 3 дня, а как быть с точками - пока хз) и в общем
как делать "в общем" пока тоже не совсем придумал, но точно нужно будет делать 10-12 точек и что-то с точками решать
возможно, есть смысл менять размер холста
'''


print(len(data['День']))

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
    plt.xlim(-0.5, len(data["День"]) - 0.5)  # Небольшие отступы по X
    
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