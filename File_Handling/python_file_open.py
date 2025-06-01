"""
КОНСПЕКТ ПО РАБОТЕ С ФАЙЛАМИ В PYTHON
Источник: https://www.w3schools.com/python/python_file_handling.asp
"""

# =============================================
# 1. Основные операции с файлами
# =============================================

# 1.1 Открытие файлов
# Общий синтаксис: open(file, mode)
# Режимы:
#   'r' - чтение (по умолчанию)
#   'w' - запись (перезаписывает существующий)
#   'a' - добавление в конец
#   'x' - эксклюзивное создание (ошибка если файл существует)
#   't' - текстовый режим (по умолчанию)
#   'b' - бинарный режим

import datetime

# 1.2 Чтение файлов
try:
    # Открытие файла в контекстном менеджере (автоматическое закрытие)
    with open("example.txt", "r") as file:
        content = file.read()  # Чтение всего файла
        print(content)
        
        # Чтение построчно
        file.seek(0)  # Возврат в начало файла
        for line in file:
            print(line.strip())  # Удаление символов переноса
            
        # Чтение списка строк
        file.seek(0)
        lines = file.readlines()
        print(lines)
except FileNotFoundError:
    print("Файл не найден!")

# 1.3 Запись в файл
with open("output.txt", "w") as file:
    file.write("Hello World!\n")
    file.writelines(["Line 1\n", "Line 2\n"])

# 1.4 Добавление в файл
with open("output.txt", "a") as file:
    file.write("Appended line\n")

# =============================================
# 2. Работа с путями файлов
# =============================================

import os
from pathlib import Path

# 2.1 Получение текущей директории
current_dir = os.getcwd()
print(f"Текущая директория: {current_dir}")

# 2.2 Создание абсолютного пути
file_path = os.path.join(current_dir, "data", "file.txt")
print(f"Абсолютный путь: {file_path}")

# 2.3 Работа с pathlib (современный способ)
path = Path("data/file.txt")
print(f"Имя файла: {path.name}")
print(f"Родительская директория: {path.parent}")
print(f"Расширение: {path.suffix}")

# 2.4 Проверка существования
if path.exists():
    print("Файл существует")
else:
    print("Файл не найден")

# =============================================
# 3. Управление файлами и директориями
# =============================================

# 3.1 Создание директории
os.makedirs("data/docs", exist_ok=True)  # exist_ok=True предотвращает ошибку если директория существует

# 3.2 Переименование файла
os.rename("old.txt", "new.txt")

# 3.3 Удаление файла
os.remove("file_to_delete.txt")

# 3.4 Удаление директории
os.rmdir("empty_dir")  # Удаляет только пустые директории
import shutil
shutil.rmtree("dir_with_files")  # Удаляет директорию с содержимым

# 3.5 Копирование файлов
shutil.copy("source.txt", "destination.txt")
shutil.copy2("source.txt", "destination.txt")  # Сохраняет метаданные

# =============================================
# 4. Работа с бинарными файлами
# =============================================

# 4.1 Чтение изображения
with open("image.jpg", "rb") as img_file:
    image_data = img_file.read()
    # print(image_data[:10])  # Первые 10 байт

# 4.2 Запись бинарных данных
with open("copy.jpg", "wb") as copy_file:
    copy_file.write(image_data)

# =============================================
# 5. Продвинутые техники
# =============================================

# 5.1 Чтение больших файлов
def process_large_file(filename):
    with open(filename, "r") as file:
        while True:
            chunk = file.read(1024)  # Чтение по 1 КБ
            if not chunk:
                break
            # Обработка чанка данных
            print(chunk, end="")

# 5.2 Работа с CSV
import csv
with open("data.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        print(row)

# 5.3 Работа с JSON (см. предыдущий конспект)
import json
with open("data.json", "r") as json_file:
    data = json.load(json_file)

# =============================================
# 6. Практические примеры
# =============================================

# 6.1 Логгер
def log_message(message, filename="app.log"):
    with open(filename, "a") as log_file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"[{timestamp}] {message}\n")

# log_message("Запуск приложения")

# 6.2 Конфигурационный файл
def load_config(filename="config.json"):
    try:
        with open(filename, "r") as config_file:
            return json.load(config_file)
    except FileNotFoundError:
        return {"debug": False, "max_connections": 10}

# config = load_config()

# 6.3 Резервное копирование
def backup_file(filename):
    import time
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    backup_name = f"{filename}.bak_{timestamp}"
    shutil.copy2(filename, backup_name)
    return backup_name

# backup = backup_file("important.txt")

# 6.4 Поиск файлов
def find_files(extension, directory="."):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                yield os.path.join(root, file)

# for py_file in find_files(".py"):
#     print(py_file)

"""
КЛЮЧЕВЫЕ ТЕЗИСЫ:
1. Основные операции:
   - open() для открытия файлов (обязательно закрывайте файлы!)
   - with для автоматического закрытия (контекстный менеджер)
   - read()/readline()/readlines() для чтения
   - write()/writelines() для записи

2. Режимы работы:
   - 'r': чтение (по умолчанию)
   - 'w': запись (перезаписывает файл)
   - 'a': добавление в конец
   - 'x': эксклюзивное создание
   - 't': текстовый режим
   - 'b': бинарный режим

3. Пути файлов:
   - os.path для работы с путями (устаревший способ)
   - pathlib.Path (современный ООП подход)
   - os.getcwd() - текущая рабочая директория
   - os.path.join() - безопасное соединение путей

4. Управление файловой системой:
   - os.makedirs(): создание директорий
   - os.rename(): переименование
   - os.remove(): удаление файла
   - os.rmdir(): удаление пустой директории
   - shutil.rmtree(): удаление директории с содержимым
   - shutil.copy(): копирование файлов

5. Best practices:
   - Всегда используйте with для работы с файлами
   - Обрабатывайте исключения (FileNotFoundError, PermissionError)
   - Для больших файлов читайте по частям
   - Используйте кодировку UTF-8 (encoding='utf-8')
   - Закрывайте файлы вручную, если не используете with

6. Типичные ошибки:
   - Открытие несуществующего файла в режиме 'r'
   - Использование 'w' вместо 'a' для добавления данных
   - Незакрытие файла после работы
   - Путаница между абсолютными и относительными путями
   - Игнорирование ошибок кодировки

7. Работа с разными форматами:
   - CSV: модуль csv
   - JSON: модуль json
   - XML: модуль xml.etree.ElementTree
   - Excel: библиотеки openpyxl, pandas

8. Производительность:
   - Для больших файлов используйте буферизированное чтение
   - Для бинарных данных используйте режим 'b'
   - Для частых операций чтения/записи используйте mmap
   - Для высоконагруженных систем используйте асинхронные методы
"""