"""
КОНСПЕКТ ПО КОРТЕЖАМ (TUPLES) В PYTHON
Источник: https://www.w3schools.com/python/python_tuples.asp
"""

# =============================================
# 1. Создание и базовые операции
# =============================================

# 1.1 Создание кортежей
tuple1 = ()                     # Пустой кортеж
tuple2 = (1, 2, 3)              # Кортеж с числами
tuple3 = ("apple", True, 2.5)   # Разные типы данных
tuple4 = tuple([1, 2, 3])       # Конструктор tuple()

# Особенность: кортеж с одним элементом требует запятой
single_item = ("hello",)        # Правильно
not_a_tuple = ("hello")         # Это строка, НЕ кортеж!

print(type(tuple3))  # <class 'tuple'>
print(type(not_a_tuple))  # <class 'str'>

# 1.2 Индексация и срезы
colors = ("red", "green", "blue", "yellow")
print(colors[1])       # green
print(colors[-1])      # yellow
print(colors[1:3])     # ('green', 'blue')

# =============================================
# 2. Основные особенности кортежей
# =============================================

# 2.1 Неизменяемость (immutable)
# Попытка изменить элемент вызовет ошибку:
# colors[0] = "pink"  # TypeError: 'tuple' object does not support item assignment

# 2.2 Пересоздание кортежа
colors = ("pink",) + colors[1:]  # Создаем новый кортеж
print(colors)  # ('pink', 'green', 'blue', 'yellow')

# 2.3 Распаковка кортежей
a, b, c = (10, 20, 30)
print(b)  # 20

# 2.4 Вложенные кортежи
matrix = ((1, 2), (3, 4), (5, 6))
print(matrix[1][0])  # 3

# =============================================
# 3. Методы кортежей
# =============================================

# 3.1 count() - подсчет элементов
letters = ('a', 'b', 'c', 'a', 'b')
print(letters.count('a'))  # 2

# 3.2 index() - поиск индекса элемента
print(letters.index('c'))  # 2 (первое вхождение)

# 3.3 Проверка наличия
print("red" in colors)  # True

# =============================================
# 4. Преобразования
# =============================================

# 4.1 Кортеж ↔ Список
my_list = list(colors)     # Преобразование в список
my_tuple = tuple(my_list)  # Обратное преобразование

# 4.2 Конкатенация
combined = (1, 2) + (3, 4)  # (1, 2, 3, 4)

# 4.3 Умножение
repeated = ("Hi",) * 3      # ('Hi', 'Hi', 'Hi')

# =============================================
# 5. Практические примеры
# =============================================

# 5.1 Возврат нескольких значений из функции
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers)/len(numbers)

stats = get_stats([10, 20, 30])
print(stats)  # (10, 30, 20.0)

# 5.2 Использование как ключа словаря
locations = {
    (35.6895, 139.6917): "Tokyo",
    (40.7128, -74.0060): "New York"
}
print(locations[(40.7128, -74.0060)])  # New York

# 5.3 Сравнение кортежей
print((1, 2, 3) < (1, 2, 4))  # True (лексикографическое сравнение)

"""
КЛЮЧЕВЫЕ ТЕЗИСЫ:
1. Кортежи неизменяемы: элементы нельзя добавлять/удалять/менять
2. Используются круглые скобки (), но для создания обязательно нужна запятая
3. Поддерживают все типы данных и вложенные структуры
4. Основные методы: count(), index()
5. Преимущества перед списками:
   - Безопасность данных
   - Быстродействие
   - Возможность использовать как ключи словарей
6. Распаковка позволяет удобно работать с несколькими значениями
7. Поддерживают те же операции, что и списки, кроме изменяющих содержимое
8. Для "изменения" кортежа нужно создавать новый объект
9. Используются для возврата нескольких значений из функций
10. Пустой кортеж создается как (), кортеж с одним элементом - (item,)
"""