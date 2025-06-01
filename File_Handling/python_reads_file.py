"""
КОНСПЕКТ ПО ФУНКЦИИ OPEN() В PYTHON
Источник: https://www.w3schools.com/python/python_file_open.asp
"""

# =============================================
# 1. Основы функции open()
# =============================================

# Функция open() возвращает файловый объект и используется для работы с файлами
# Синтаксис: open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

# Основные параметры:
# - file: путь к файлу (строка или объект пути)
# - mode: режим открытия файла (строка)
# - encoding: кодировка файла (например, 'utf-8')

# =============================================
# 2. Режимы открытия файлов (mode)
# =============================================

# 2.1 Основные режимы:
#   'r' - чтение (по умолчанию)
#   'w' - запись (перезаписывает существующий файл)
#   'a' - добавление в конец файла
#   'x' - эксклюзивное создание (ошибка если файл существует)

# 2.2 Типы файлов:
#   't' - текстовый режим (по умолчанию)
#   'b' - бинарный режим

# 2.3 Комбинированные режимы:
#   'r+' - чтение и запись (указатель в начале)
#   'w+' - чтение и запись (перезаписывает файл)
#   'a+' - чтение и добавление (указатель в конце)

# =============================================
# 3. Примеры открытия файлов
# =============================================

# 3.1 Чтение файла (текстовый режим)
try:
    with open('example.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Файл не найден!")

# 3.2 Запись в файл
with open('output.txt', 'w') as file:
    file.write("Первая строка\n")
    file.write("Вторая строка\n")

# 3.3 Добавление в файл
with open('output.txt', 'a') as file:
    file.write("Добавленная строка\n")

# 3.4 Чтение и запись одновременно
with open('data.txt', 'r+') as file:
    content = file.read()
    file.write("\nНовые данные")

# 3.5 Бинарный режим (работа с изображениями)
with open('image.jpg', 'rb') as file:
    binary_data = file.read()

# =============================================
# 4. Методы работы с файловыми объектами
# =============================================

# 4.1 Чтение данных
with open('example.txt', 'r') as file:
    print(file.read(10))   # Чтение 10 символов
    print(file.readline()) # Чтение одной строки
    print(file.readlines()) # Чтение всех строк в список

# 4.2 Запись данных
with open('log.txt', 'a') as file:
    file.write("Новая запись\n")
    file.writelines(["line1\n", "line2\n"])

# 4.3 Позиционирование в файле
with open('data.bin', 'rb+') as file:
    file.seek(5)      # Перемещение на 5-й байт
    position = file.tell() # Текущая позиция (5)
    file.write(b'XYZ') # Запись данных
    file.seek(0)
    print(file.read()) # Просмотр изменений

# =============================================
# 5. Управление кодировкой
# =============================================

# 5.1 Работа с разными кодировками
try:
    with open('russian.txt', 'r', encoding='utf-8') as file:
        print(file.read())
except UnicodeDecodeError:
    print("Ошибка декодирования!")

# 5.2 Автоматическое определение кодировки
import chardet

def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        raw_data = file.read(1000)
        result = chardet.detect(raw_data)
        return result['encoding']

encoding = detect_encoding('unknown.txt')
with open('unknown.txt', 'r', encoding=encoding) as file:
    content = file.read()

# =============================================
# 6. Практические примеры
# =============================================

# 6.1 Копирование файла
def copy_file(source, destination):
    try:
        with open(source, 'rb') as src, open(destination, 'wb') as dest:
            dest.write(src.read())
        return True
    except Exception as e:
        print(f"Ошибка копирования: {e}")
        return False

# copy_file('source.txt', 'copy.txt')

# 6.2 Поиск и замена в файле
def replace_in_file(file_path, old_str, new_str):
    try:
        with open(file_path, 'r+') as file:
            content = file.read()
            new_content = content.replace(old_str, new_str)
            file.seek(0)
            file.write(new_content)
            file.truncate() # Обрезать остаток файла
        return True
    except Exception as e:
        print(f"Ошибка: {e}")
        return False

# replace_in_file('text.txt', 'старое', 'новое')

# 6.3 Чтение больших файлов по частям
def process_large_file(file_path, chunk_size=1024):
    try:
        with open(file_path, 'r') as file:
            while True:
                chunk = file.read(chunk_size)
                if not chunk:
                    break
                # Обработка чанка данных
                print(chunk, end='')
        return True
    except Exception as e:
        print(f"Ошибка: {e}")
        return False

# process_large_file('big_file.txt')

# 6.4 Работа с CSV файлами
import csv
def read_csv_file(file_path):
    with open(file_path, 'r', newline='', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row)

# read_csv_file('data.csv')

"""
КЛЮЧЕВЫЕ ТЕЗИСЫ:
1. Функция open():
   - Основной инструмент для работы с файлами
   - Всегда закрывайте файлы с помощью close() или контекстного менеджера (with)
   - Контекстный менеджер гарантирует закрытие файла даже при ошибке

2. Режимы работы:
   - 'r' - чтение (файл должен существовать)
   - 'w' - запись (создает или перезаписывает файл)
   - 'a' - добавление (создает файл если не существует)
   - 'x' - эксклюзивное создание (ошибка если файл существует)
   - 'b' - бинарный режим (для изображений, исполняемых файлов)
   - '+' - обновление (чтение + запись)

3. Методы файловых объектов:
   - read() - чтение всего файла или указанного количества символов/байт
   - readline() - чтение одной строки
   - readlines() - чтение всех строк в список
   - write() - запись строки
   - writelines() - запись списка строк
   - seek() - изменение позиции указателя
   - tell() - получение текущей позиции указателя
   - truncate() - обрезка файла до текущей позиции

4. Кодировки:
   - По умолчанию используется кодировка платформы
   - Всегда указывайте encoding='utf-8' для кросс-платформенной совместимости
   - Для определения кодировки используйте модуль chardet
   - Обрабатывайте UnicodeDecodeError при работе с неизвестными файлами

5. Best practices:
   - Всегда используйте контекстный менеджер (with open() as f)
   - Указывайте кодировку явно
   - Проверяйте существование файлов перед открытием
   - Для больших файлов используйте чтение по частям
   - Закрывайте файлы вручную, если не используете контекстный менеджер

6. Типичные ошибки:
   - FileNotFoundError при открытии несуществующего файла в режиме 'r'
   - PermissionError при отсутствии прав доступа
   - UnicodeDecodeError при неправильной кодировке
   - Оставить файл открытым (утечка ресурсов)
   - Попытка записи в файл, открытый в режиме чтения

7. Особенности работы:
   - В Windows используйте newline='' при работе с CSV
   - В текстовом режиме (\n) автоматически конвертируется в платформо-зависимый символ новой строки
   - В бинарном режиме данные возвращаются как байтовые объекты
   - При открытии в режиме 'w' или 'w+' файл немедленно обрезается до нулевой длины

8. Дополнительные параметры:
   - buffering: размер буфера (0 - без буферизации, 1 - построчная, >1 - размер буфера в байтах)
   - errors: обработка ошибок кодировки ('strict', 'ignore', 'replace')
   - newline: управление переводом строк (None, '', '\n', '\r\n')
"""