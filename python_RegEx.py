"""
КОНСПЕКТ ПО РЕГУЛЯРНЫМ ВЫРАЖЕНИЯМ В PYTHON
Источник: https://www.w3schools.com/python/python_regex.asp
"""

import re

# =============================================
# 1. Основные функции модуля re
# =============================================

# 1.1 re.search() - поиск первого совпадения
text = "Python is fun to learn"
match = re.search(r"fun", text)
if match:
    print(f"Найдено '{match.group()}' с позиции {match.start()} до {match.end()}")  # Найдено 'fun' с позиции 10 до 13

# 1.2 re.match() - проверка начала строки
match = re.match(r"Python", text)  # Совпадение в начале
print("Начало совпадает" if match else "Не совпадает")  # Начало совпадает

# 1.3 re.findall() - все совпадения
all_matches = re.findall(r"\b\w{3}\b", text)  # Все 3-буквенные слова
print(all_matches)  # ['fun'] (is - 2 буквы, to - 2, learn - 5)

# 1.4 re.finditer() - итератор совпадений
for match in re.finditer(r"\bt\w+", text):  # Слова на 't'
    print(match.group())  # to, затем learn? Нет, learn не на t. to

# 1.5 re.sub() - замена текста
new_text = re.sub(r"fun", "awesome", text)
print(new_text)  # Python is awesome to learn

# 1.6 re.split() - разделение по шаблону
parts = re.split(r"\s+", text)  # По пробелам
print(parts)  # ['Python', 'is', 'fun', 'to', 'learn']

# =============================================
# 2. Синтаксис регулярных выражений
# =============================================

# 2.1 Специальные символы:
# .     - любой символ кроме \n
# ^     - начало строки
# $     - конец строки
# *     - 0 или более повторений
# +     - 1 или более повторений
# ?     - 0 или 1 повторение
# {n}   - ровно n повторений
# {n,}  - n или более
# {n,m} - от n до m повторений

# 2.2 Классы символов:
# [abc]   - любой из a, b, c
# [a-z]   - любая буква от a до z
# [^abc]  - любой символ кроме a,b,c
# \d      - цифра [0-9]
# \D      - не цифра
# \s      - пробельный символ
# \S      - не пробельный
# \w      - буква/цифра/подчёркивание [a-zA-Z0-9_]
# \W      - не \w
# \b      - граница слова

# 2.3 Группировка:
# ( )    - группировка и захват
# (?: )  - группировка без захвата
# |      - или

# Примеры:
pattern = r"\b(\d{3})-(\d{2})-(\d{4})\b"  # Номер типа 123-45-6789
text = "Мои номера: 123-45-6789 и 987-65-4321"
matches = re.findall(pattern, text)
print(matches)  # [('123', '45', '6789'), ('987', '65', '4321')]

# =============================================
# 3. Работа с группами
# =============================================

# 3.1 Доступ к группам
date_text = "2023-08-15"
date_match = re.match(r"(\d{4})-(\d{2})-(\d{2})", date_text)
if date_match:
    print(f"Год: {date_match.group(1)}, Месяц: {date_match.group(2)}, День: {date_match.group(3)}")
    # Год: 2023, Месяц: 08, День: 15

# 3.2 Именованные группы
pattern = r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})"
match = re.match(pattern, date_text)
if match:
    print(f"Месяц: {match.group('month')}")  # 08

# =============================================
# 4. Флаги компиляции
# =============================================

# 4.1 Основные флаги:
# re.IGNORECASE (re.I) - игнорировать регистр
# re.MULTILINE (re.M)  - ^ и $ для каждой строки
# re.DOTALL (re.S)     - . включает \n
# re.VERBOSE (re.X)    - игнорировать пробелы и комментарии

# Пример:
text = "Python\npython\nPYTHON"
matches = re.findall(r"^python", text, flags=re.I | re.M)
print(matches)  # ['Python', 'python', 'PYTHON']

# 4.2 Компиляция шаблонов
pattern = re.compile(r"\b\w{4}\b")  # Слова из 4 букв
matches = pattern.findall("This is a test string")
print(matches)  # ['This', 'test']

# =============================================
# 5. Практические примеры
# =============================================

# 5.1 Валидация email
def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.match(pattern, email))

print(is_valid_email("test@example.com"))  # True
print(is_valid_email("invalid.email@"))     # False

# 5.2 Поиск всех ссылок в тексте
html = '<a href="https://example.com">Example</a> <a href="http://test.org">Test</a>'
links = re.findall(r'href="(https?://[^"]+)"', html)
print(links)  # ['https://example.com', 'http://test.org']

# 5.3 Извлечение данных из логов
log = "2023-08-15 12:30:45 [ERROR] User not found: id=12345"
pattern = r"(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) \[(\w+)\] (.+): id=(\d+)"
match = re.match(pattern, log)
if match:
    print(f"Дата: {match.group(1)}, Время: {match.group(2)}, Тип: {match.group(3)}, Сообщение: {match.group(4)}, ID: {match.group(5)}")

# 5.4 Удаление HTML тегов
html_text = "<p>This is <b>bold</b> text</p>"
clean_text = re.sub(r"<[^>]+>", "", html_text)
print(clean_text)  # This is bold text

"""
КЛЮЧЕВЫЕ ТЕЗИСЫ:
1. Основные функции:
   - search(): первое совпадение в любом месте
   - match(): совпадение в начале строки
   - findall(): все совпадения
   - finditer(): итератор совпадений
   - sub(): замена по шаблону
   - split(): разделение по шаблону

2. Синтаксис:
   - Спецсимволы: . ^ $ * + ? { } [ ] \ | ( )
   - Классы символов: \d, \s, \w, \b
   - Группы: ( ) для захвата, (?: ) для группировки без захвата

3. Работа с совпадениями:
   - group(): получение текста совпадения
   - groups(): все захваченные группы
   - groupdict(): именованные группы

4. Флаги:
   - re.I: игнорирование регистра
   - re.M: многострочный режим
   - re.S: точка включает перенос строки
   - re.X: разрешение комментариев в шаблоне

5. Best practices:
   - Используйте r-строки для шаблонов (r"pattern")
   - Компилируйте часто используемые шаблоны
   - Проверяйте наличие совпадения перед вызовом group()
   - Для сложных шаблонов используйте re.X и комментарии
   - Тестируйте регулярки на краевых случаях

6. Применение:
   - Валидация ввода (email, телефоны, пароли)
   - Парсинг логов и данных
   - Очистка текста (HTML, форматирование)
   - Поиск и замена в текстах
   - Извлечение данных из строк

7. Инструменты для тестирования:
   - https://regex101.com/ (онлайн тестер)
   - re.DEBUG флаг для отладки
   - Встроенный модуль re в консоли Python
"""