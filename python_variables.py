"""
КОНСПЕКТ ПО ТЕМЕ "ПЕРЕМЕННЫЕ В PYTHON"
Источник: https://www.w3schools.com/python/python_variables.asp
"""

# =============================================
# 1. Основные концепции переменных
# =============================================

# 1.1 Что такое переменная?
# Переменная - это именованная ссылка на область памяти, где хранится значение.
# В Python переменные создаются в момент первого присваивания значения.

# Пример:
message = "Hello Python"  # Создаем переменную message и связываем ее со строкой
print(message)            # Доступ к значению через имя переменной

# 1.2 Свойства переменных:
# - Динамическая типизация: тип определяется автоматически
# - Переменная - это ссылка на объект (все в Python - объекты)
# - Одно значение может иметь несколько ссылок

a = 5
b = a  # Оба имени ссылаются на один объект
print(id(a), id(b))  # Выведет одинаковые идентификаторы

# 1.3 Основные типы данных (для понимания работы переменных):
# - Неизменяемые (immutable): int, float, bool, str, tuple
# - Изменяемые (mutable): list, dict, set

# Пример различий:
# Immutable
x = 10
print(id(x))  # > 140704485614112 (пример)
x += 5
print(id(x))  # Новый идентификатор, другой объект

# Mutable
arr = [1, 2, 3]
print(id(arr))  # > 2105289261120 (пример)
arr.append(4)
print(id(arr))  # Идентификатор остался прежним

# =============================================
# 2. Детали работы с переменными
# =============================================

# 2.1 Присвоение значений
# - Простое присвоение
name = "Alice"

# - Множественное присвоение
x, y, z = 1, 2, 3

# - Цепочное присвоение
a = b = c = 0

# 2.2 Динамическое изменение типа
var = 100       # Сейчас var - integer
var = "Text"    # Теперь var - string
var = [1,2,3]   # Теперь var - list

# 2.3 Удаление переменных
del var         # Удаление ссылки на объект
# print(var)    # Вызовет NameError

# =============================================
# 3. Области видимости (Scope)
# =============================================

# 3.1 Глобальные переменные
global_var = "I'm global"

def show_global():
    print(global_var)  # Чтение глобальной переменной

show_global()

# 3.2 Локальные переменные
def create_local():
    local_var = "I'm local"
    print(local_var)

create_local()
# print(local_var)  # Ошибка - переменная не существует вне функции

# 3.3 Ключевое слово global
counter = 0

def increment():
    global counter
    counter += 1

increment()
print(counter)  # > 1

# 3.4 Ключевое слово nonlocal (для вложенных функций)
def outer():
    outer_var = "outer"
    
    def inner():
        nonlocal outer_var
        outer_var = "modified"
    
    inner()
    print(outer_var)  # > modified

outer()

# =============================================
# 4. Работа с типами данных
# =============================================

# 4.1 Проверка типа
value = 3.14
print(type(value))        # > <class 'float'>
print(isinstance(value, float))  # > True

# 4.2 Явное преобразование типов
num_str = "123"
num_int = int(num_str)    # Преобразование строки в integer

# 4.3 Автоматическое преобразование (Type Coercion)
result = 3 + 4.5          # int + float = float
print(result)             # > 7.5

# =============================================
# 5. Строковые операции с переменными
# =============================================

# 5.1 Конкатенация
first = "Hello"
second = "World"
full = first + " " + second  # "Hello World"

# 5.2 f-строки (форматирование)
age = 25
info = f"I'm {age} years old"  # I'm 25 years old

# 5.3 Многострочные строки
multi_line = """Это многострочная
строка"""

# =============================================
# 6. Особенности именования
# =============================================

# 6.1 Правильные имена:
my_var = 10        # Стиль snake_case
MAX_SIZE = 100     #"Константы" (соглашение)
_count = 5         # Внутреннее использование

# 6.2 Недопустимые имена:
# 2var = 5         # Начинается с цифры
# var-name = 5     # Дефис запрещен
# class = 5        # Зарезервированное слово

# 6.3 Регистрозависимость:
Var = 1
var = 2
print(Var + var)  # 3 (это разные переменные)

# =============================================
# 7. Практические примеры
# =============================================

# 7.1 Обмен значений
a, b = 5, 10
a, b = b, a  # Теперь a=10, b=5

# 7.2 Распаковка коллекций
colors = ["red", "green", "blue"]
first_color, *rest = colors  # first_color = "red", rest = ["green", "blue"]

# 7.3 Переменные в выражениях
x = 10
y = x ** 2 + 3*x - 5  # 10^2 + 3*10 -5 = 125

# =============================================
# 8. Лучшие практики
# =============================================

# - Используйте описательные имена (user_age вместо age)
# - Избегайте однобуквенных имен (кроме временных переменных)
# - Для констант используйте UPPER_CASE
# - Соблюдайте PEP8 (79 символов в строке, пробелы вокруг операторов)
# - Комментируйте сложные части кода
# - Удаляйте неиспользуемые переменные

"""
КЛЮЧЕВЫЕ ТЕЗИСЫ:
1. Переменные - это ссылки на объекты в памяти
2. Python использует динамическую типизацию
3. Область видимости определяет доступность переменной
4. Имена должны быть понятными и соответствовать стилю
5. Избегайте глобальных перемененых где это возможно
6. Используйте type() и isinstance() для проверки типов
"""