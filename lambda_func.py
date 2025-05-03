"""
КОНСПЕКТ ПО ЛЯМБДА-ФУНКЦИЯМ В PYTHON
Источник: https://www.w3schools.com/python/python_lambda.asp
"""

# =============================================
# 1. Базовый синтаксис
# =============================================

# 1.1 Простая lambda-функция
square = lambda x: x ** 2
print(square(5))  # 25

# 1.2 Множественные аргументы
multiply = lambda a, b: a * b
print(multiply(3, 4))  # 12

# 1.3 Лямбда без аргументов
greet = lambda: "Hello World"
print(greet())  # Hello World

# =============================================
# 2. Использование с функциями высшего порядка
# =============================================

# 2.1 Сортировка списка словарей
users = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 20}
]

# Сортировка по возрасту
users_sorted = sorted(users, key=lambda x: x["age"])
print(users_sorted)  # [{'name': 'Charlie', ...}, {'name': 'Alice', ...}, ...]

# 2.2 Фильтрация списка
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4, 6]

# 2.3 Преобразование элементов
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)  # [2, 4, 6, 8, 10, 12]

# =============================================
# 3. Вложенные лямбда-функции
# =============================================

# 3.1 Лямбда внутри другой функции
def power(exponent):
    return lambda base: base ** exponent

square = power(2)
cube = power(3)

print(square(4))  # 16
print(cube(3))    # 27

# =============================================
# 4. Ограничения lambda-функций
# =============================================

# 4.1 Только одно выражение
# invalid = lambda x: print(x); return x * 2  # SyntaxError

# 4.2 Невозможность аннотации типов
# valid: Callable[[int], int] = lambda x: x*2  # Требует импорта typing

# =============================================
# 5. Практические примеры
# =============================================

# 5.1 Обработка событий GUI (пример с tkinter)
# btn = Button(text="Click", command=lambda: print("Button clicked"))

# 5.2 Динамические вычисления
operations = {
    "add": lambda a, b: a + b,
    "subtract": lambda a, b: a - b
}
print(operations["add"](10, 5))      # 15
print(operations["subtract"](10, 5)) # 5

# 5.3 Цепочка операций
process = lambda x: (x ** 2) + 5 if x > 0 else abs(x)
print(process(-3))  # 3
print(process(2))   # 9

"""
КЛЮЧЕВЫЕ ТЕЗИСЫ:
1. Лямбда-функции - анонимные функции с синтаксисом: lambda args: expression
2. Основные характеристики:
   - Могут принимать любое количество аргументов
   - Содержат только одно выражение
   - Не поддерживают аннотации типов
   - Не могут содержать return, pass или raise
3. Идеальные случаи использования:
   - Короткие операции в map()/filter()
   - Ключи для сортировки (key=...)
   - Простые коллбэки
4. Ограничения:
   - Невозможность многострочных операций
   - Отсутствие документации (__doc__)
   - Сложность отладки
5. Best practices:
   - Используйте для простых однострочных операций
   - Избегайте сложных лямбда-выражений
   - Для сложной логики используйте обычные функции
6. Альтернативы:
   - Генераторы списков вместо map()/filter()
   - Функции из operator модуля (itemgetter, attrgetter)
   - Частичные функции (functools.partial)
"""