"""
КОНСПЕКТ ПО ОБРАБОТКЕ ИСКЛЮЧЕНИЙ В PYTHON
Источник: https://www.w3schools.com/python/python_try_except.asp
"""

# =============================================
# 1. Основы обработки исключений
# =============================================

# 1.1 Блок try-except
try:
    print(10 / 0)  # Попытка деления на ноль
except ZeroDivisionError:
    print("Ошибка: деление на ноль!")

# 1.2 Обработка нескольких исключений
try:
    # Код, который может вызвать разные исключения
    value = int("abc")
    result = 10 / value
except (ValueError, ZeroDivisionError) as e:
    print(f"Произошла ошибка: {type(e).__name__} - {e}")

# =============================================
# 2. Полная структура обработки исключений
# =============================================

# 2.1 Блоки else и finally
try:
    file = open("data.txt", "r")
    content = file.read()
    number = int(content)
except FileNotFoundError:
    print("Файл не найден!")
except ValueError:
    print("Ошибка преобразования числа!")
else:
    print(f"Успешно прочитано число: {number}")
finally:
    print("Завершение работы с файлом")
    if 'file' in locals() and not file.closed:
        file.close()

# =============================================
# 3. Встроенные типы исключений
# =============================================

# 3.1 Основные исключения:
# - ZeroDivisionError: деление на ноль
# - TypeError: операция с несовместимыми типами
# - ValueError: неверное значение
# - FileNotFoundError: файл не найден
# - IndexError: индекс вне диапазона
# - KeyError: ключ не найден в словаре
# - NameError: имя переменной не найдено
# - KeyboardInterrupt: прерывание пользователем (Ctrl+C)

# 3.2 Иерархия исключений:
# BaseException
#  ├── SystemExit
#  ├── KeyboardInterrupt
#  └── Exception
#        ├── ArithmeticError
#        │     ├── ZeroDivisionError
#        │     └── ...
#        ├── LookupError
#        │     ├── IndexError
#        │     └── KeyError
#        ├── OSError
#        │     ├── FileNotFoundError
#        │     └── ...
#        └── ...

# =============================================
# 4. Создание пользовательских исключений
# =============================================

# 4.1 Простое пользовательское исключение
class NegativeNumberError(Exception):
    """Ошибка при обнаружении отрицательного числа"""
    pass

# 4.2 Использование
def process_positive(number):
    if number < 0:
        raise NegativeNumberError("Число не может быть отрицательным")
    return number ** 2

try:
    print(process_positive(-5))
except NegativeNumberError as e:
    print(e)

# =============================================
# 5. Оператор raise
# =============================================

# 5.1 Генерация исключений
def validate_age(age):
    if age < 0:
        raise ValueError("Возраст не может быть отрицательным")
    if age < 18:
        raise PermissionError("Доступ разрешен только с 18 лет")
    return True

# 5.2 Повторное возбуждение исключения
try:
    validate_age(-5)
except ValueError as e:
    print(f"Ошибка: {e}")
    # raise  # Раскомментировать для повторного возбуждения

# =============================================
# 6. Практические примеры
# =============================================

# 6.1 Обработка ввода пользователя
def get_integer_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка: введите целое число!")

# age = get_integer_input("Введите ваш возраст: ")

# 6.2 Контекстный менеджер для файлов
try:
    with open("data.txt", "r") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("Файл не найден!")
except IOError:
    print("Ошибка чтения файла!")

# 6.3 Обработка нескольких ошибок в API
def fetch_data(url):
    try:
        import requests
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Генерирует HTTPError для 4xx/5xx статусов
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Ошибка запроса: {e}")
        return None

# data = fetch_data("https://api.example.com/data")

"""
КЛЮЧЕВЫЕ ТЕЗИСЫ:
1. Основные блоки:
   - try: содержит код, который может вызвать исключение
   - except: обработка исключений
   - else: выполняется при отсутствии исключений
   - finally: выполняется всегда (очистка ресурсов)

2. Обработка исключений:
   - Указывайте конкретные типы исключений
   - Используйте as для доступа к объекту исключения
   - Обрабатывайте несколько исключений в одном блоке через кортеж

3. Создание исключений:
   - Наследуйтесь от Exception или его подклассов
   - Используйте raise для генерации исключений
   - Добавляйте информативные сообщения об ошибках

4. Best practices:
   - Избегайте "голых" except: (без указания типа)
   - Логируйте исключения для диагностики
   - Используйте finally для освобождения ресурсов (файлы, сетевые соединения)
   - Создавайте иерархии пользовательских исключений
   - Документируйте возможные исключения в функциях

5. Особенности:
   - KeyboardInterrupt и SystemExit не наследуются от Exception
   - Можно перехватывать все исключения через except Exception
   - Блок else выполняется только при отсутствии исключений

6. Полезные методы:
   - args: аргументы исключения
   - __str__(): строковое представление
   - with_traceback(): добавление трассировки стека

7. Контекстные менеджеры (with):
   - Автоматически обрабатывают исключения и закрывают ресурсы
   - Реализуются через методы __enter__ и __exit__
   - Примеры: open(), lock.acquire(), соединения с БД

8. Принципы обработки ошибок:
   - "Ловите" только те исключения, которые можете обработать
   - Не используйте исключения для управления потоком выполнения
   - Предпочитайте проверку условий генерации исключений
   - Обеспечивайте атомарность операций
"""