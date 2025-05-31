"""
КОНСПЕКТ ПО МАТЕМАТИЧЕСКИМ ФУНКЦИЯМ В PYTHON
Источник: https://www.w3schools.com/python/python_math.asp
"""

# =============================================
# 1. Встроенные математические функции
# =============================================

# 1.1 Базовые операции
a, b = 10, 3
print(a + b)  # 13   - сложение
print(a - b)  # 7    - вычитание
print(a * b)  # 30   - умножение
print(a ** b) # 1000 - возведение в степень
print(a / b)  # 3.333... - деление
print(a // b) # 3    - целочисленное деление
print(a % b)  # 1    - остаток от деления

# 1.2 Функции преобразования
x = 3.7
print(int(x))    # 3 - преобразование в целое
print(float(x))  # 3.7 - преобразование в float
print(abs(-5))   # 5 - модуль числа

# 1.3 Округление
print(round(3.14159))     # 3
print(round(3.14159, 2))  # 3.14
print(round(3.5))         # 4 (банковское округление)

# =============================================
# 2. Модуль math
# =============================================
import math

# 2.1 Константы
print(math.pi)   # 3.141592653589793
print(math.e)    # 2.718281828459045
print(math.tau)  # 6.283185307179586 (2*pi)
print(math.inf)  # inf - бесконечность

# 2.2 Основные функции
print(math.sqrt(25))     # 5.0 - квадратный корень
print(math.pow(2, 3))    # 8.0 - возведение в степень
print(math.exp(2))       # ~7.389 - e^x
print(math.log(100, 10)) # 2.0 - логарифм
print(math.log2(8))      # 3.0
print(math.log10(1000))  # 3.0

# 2.3 Тригонометрия
angle = math.radians(60) # градусы → радианы
print(math.sin(angle))   # ~0.866
print(math.cos(angle))   # 0.5
print(math.tan(angle))   # ~1.732

# 2.4 Округление и целые числа
print(math.floor(3.9))  # 3 - округление вниз
print(math.ceil(3.1))   # 4 - округление вверх
print(math.trunc(-3.7)) # -3 - отбрасывание дробной части
print(math.factorial(5))# 120 - факториал

# =============================================
# 3. Модуль random
# =============================================
import random

# 3.1 Базовые функции
print(random.random())          # [0.0, 1.0) - случайное float
print(random.uniform(1.5, 5.5)) # float в диапазоне
print(random.randint(1, 10))    # целое в диапазоне [1, 10]

# 3.2 Работа с последовательностями
colors = ["red", "green", "blue"]
print(random.choice(colors))    # случайный элемент
random.shuffle(colors)          # перемешать список
print(colors)                   # ['green', 'red', 'blue'] (пример)

# 3.3 Выборки
print(random.sample(range(100), 5)) # 5 уникальных чисел из 100

# =============================================
# 4. Модуль statistics
# =============================================
import statistics

data = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]

# 4.1 Основные статистические показатели
print(statistics.mean(data))    # 5.0 - среднее
print(statistics.median(data))  # 5.0 - медиана
print(statistics.mode(data))    # 5   - мода
print(statistics.stdev(data))   # ~2.58 - стандартное отклонение

# =============================================
# 5. Полезные математические операции
# =============================================

# 5.1 Минимум/максимум
print(min(5, 10, 25))  # 5
print(max(5, 10, 25))  # 25

# 5.2 Сумма и произведение
print(sum([1, 2, 3]))           # 6
print(math.prod([1, 2, 3, 4]))  # 24 (Python 3.8+)

# 5.3 НОД и НОК
print(math.gcd(48, 18))         # 6 - наибольший общий делитель
print(math.lcm(15, 20))         # 60 - наименьшее общее кратное (Python 3.9+)

# =============================================
# 6. Практические примеры
# =============================================

# 6.1 Расчет гипотенузы
a, b = 3, 4
c = math.sqrt(a**2 + b**2)
print(f"Гипотенуза: {c:.1f}")  # 5.0

# 6.2 Генерация пароля
def generate_password(length=8):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
    return ''.join(random.sample(chars, length))

print(f"Пароль: {generate_password()}")  # iK3!p9L#

# 6.3 Статистический анализ
temps = [22.5, 23.7, 24.8, 21.9, 25.3, 26.1, 24.5]
print(f"Средняя температура: {statistics.mean(temps):.1f}°C")
print(f"Максимальная температура: {max(temps)}°C")
print(f"Стандартное отклонение: {statistics.stdev(temps):.2f}")

# 6.4 Геометрические расчеты
radius = 5
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius
print(f"Площадь круга: {area:.2f}")
print(f"Длина окружности: {circumference:.2f}")

"""
КЛЮЧЕВЫЕ ТЕЗИСЫ:
1. Встроенные функции:
   - abs(), round(), min(), max(), sum()
   - int(), float() для преобразования типов
   - ** для возведения в степень

2. Модуль math:
   - Константы: pi, e, tau, inf
   - Функции: sqrt(), pow(), sin(), cos(), tan()
   - Округление: floor(), ceil(), trunc()
   - Логарифмы: log(), log2(), log10()
   - Факториал: factorial()

3. Модуль random:
   - random() - случайное float [0,1)
   - uniform(a,b) - float в диапазоне
   - randint(a,b) - целое в диапазоне [a,b]
   - choice(seq) - случайный элемент
   - shuffle(seq) - перемешать последовательность

4. Модуль statistics (Python 3.4+):
   - mean() - среднее арифметическое
   - median() - медиана
   - mode() - мода
   - stdev() - стандартное отклонение

5. Полезные операции:
   - math.gcd() - наибольший общий делитель
   - math.lcm() - наименьшее общее кратное (Python 3.9+)
   - math.prod() - произведение элементов (Python 3.8+)

6. Best practices:
   - Используйте math вместо **0.5 для квадратного корня
   - Для финансовых расчетов используйте decimal
   - Для научных вычислений - numpy/scipy
   - Для статистики - pandas

7. Применение:
   - Геометрические расчеты
   - Генерация случайных данных
   - Статистический анализ
   - Криптография (в сочетании с hashlib)
   - Машинное обучение и data science
"""