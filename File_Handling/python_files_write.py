"""
КОНСПЕКТ ПО ЗАПИСИ В ФАЙЛЫ В PYTHON
Источник: https://www.w3schools.com/python/python_file_write.asp
"""

# =============================================
# 1. Основы записи в файлы
# =============================================

# 1.1 Открытие файла для записи
# Режимы:
#   'w' - перезапись файла (создает новый или очищает существующий)
#   'a' - добавление в конец файла (создает файл если не существует)
#   'x' - эксклюзивное создание (ошибка если файл существует)

# 1.2 Базовый пример записи
with open('example.txt', 'w') as file:
    file.write("Первая строка\n")
    file.write("Вторая строка\n")
    # После выхода из блока with файл автоматически закрывается

# =============================================
# 2. Методы записи
# =============================================

# 2.1 write() - запись строки
with open('output.txt', 'w') as file:
    file.write("Hello World!\n")
    file.write("Это тест записи в файл\n")
    
    # Запись чисел требует преобразования в строку
    number = 42
    file.write(f"Число: {number}\n")
    file.write("Число: " + str(number) + "\n")

# 2.2 writelines() - запись списка строк
lines = ["Первая строка\n", "Вторая строка\n", "Третья строка\n"]
with open('lines.txt', 'w') as file:
    file.writelines(lines)
    
    # Эквивалент с использованием write()
    for line in lines:
        file.write(line)

# 2.3 Запись с добавлением
with open('log.txt', 'a') as file:
    import datetime
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file.write(f"[{timestamp}] Запись в лог\n")

# =============================================
# 3. Форматирование данных перед записью
# =============================================

# 3.1 Запись табличных данных
data = [
    ["Имя", "Возраст", "Город"],
    ["Анна", 28, "Москва"],
    ["Иван", 35, "Санкт-Петербург"],
    ["Мария", 31, "Казань"]
]

with open('people.csv', 'w') as file:
    for row in data:
        # Преобразование всех элементов в строки
        line = ",".join(map(str, row)) + "\n"
        file.write(line)

# 3.2 Запись JSON
import json
user = {
    "name": "Алексей",
    "age": 30,
    "hobbies": ["чтение", "путешествия"],
    "is_student": False
}

with open('user.json', 'w', encoding='utf-8') as file:
    json.dump(user, file, ensure_ascii=False, indent=4)

# =============================================
# 4. Продвинутые техники
# =============================================

# 4.1 Буферизация записи
with open('buffered.txt', 'w', buffering=1) as file:  # Буферизация по строкам
    for i in range(5):
        file.write(f"Строка {i}\n")

# 4.2 Управление позицией записи
with open('position.txt', 'w+') as file:
    file.write("Начало файла\n")
    file.seek(10)  # Перемещение позиции записи
    file.write("Вставка в позицию 10\n")
    file.seek(0, 2)  # Перемещение в конец файла
    file.write("Конец файла\n")

# 4.3 Запись бинарных данных
binary_data = bytes(range(256))  # Создание байтового объекта
with open('binary.bin', 'wb') as file:
    file.write(binary_data)

# =============================================
# 5. Практические примеры
# =============================================

# 5.1 Логгер приложения
def log_message(message, filename="app.log"):
    with open(filename, 'a') as log_file:
        import time
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"[{timestamp}] {message}\n")

# log_message("Запуск приложения")
# log_message("Пользователь вошел в систему")
# log_message("Ошибка: файл не найден", "error.log")

# 5.2 Экспорт данных в CSV
def export_to_csv(data, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        # Запись заголовков
        headers = ",".join(data[0].keys())
        file.write(headers + "\n")
        
        # Запись данных
        for item in data:
            values = ",".join(str(v) for v in item.values())
            file.write(values + "\n")

# Данные для экспорта
users = [
    {"id": 1, "name": "Анна", "email": "anna@example.com"},
    {"id": 2, "name": "Иван", "email": "ivan@example.com"},
    {"id": 3, "name": "Мария", "email": "maria@example.com"}
]

# export_to_csv(users, "users.csv")

# 5.3 Резервное копирование файла
def backup_file(filename):
    import shutil
    import time
    backup_name = f"{filename}.bak_{time.strftime('%Y%m%d_%H%M%S')}"
    shutil.copy2(filename, backup_name)
    return backup_name

# Создаем тестовый файл для демонстрации
with open('important_data.txt', 'w') as f:
    f.write("Важные данные!\n")

# Создаем резервную копию
# backup = backup_file('important_data.txt')

# 5.4 Генератор конфигурационных файлов
def generate_config(settings, filename="config.ini"):
    with open(filename, 'w') as file:
        file.write("[Настройки]\n")
        for key, value in settings.items():
            file.write(f"{key} = {value}\n")

# config_settings = {
#     "debug_mode": "True",
#     "max_connections": "10",
#     "timeout": "30",
#     "admin_email": "admin@example.com"
# }
# generate_config(config_settings)

"""
КЛЮЧЕВЫЕ ТЕЗИСЫ:
1. Основные режимы записи:
   - 'w' - перезапись файла (создает новый или очищает существующий)
   - 'a' - добавление в конец файла
   - 'x' - эксклюзивное создание (ошибка если файл существует)
   - 'w+' - чтение и запись (перезаписывает файл)

2. Методы записи:
   - write(str) - запись строки в файл
   - writelines(sequence) - запись последовательности строк

3. Best practices:
   - Всегда используйте with open() для автоматического закрытия файлов
   - Указывайте кодировку явно (encoding='utf-8')
   - Для CSV используйте специализированный модуль csv
   - Для сложных структур данных используйте json.dump()
   - Разделяйте данные запятыми или табуляцией для табличных форматов

4. Особенности:
   - При использовании 'w' существующий файл будет перезаписан без предупреждения
   - В Windows символ новой строки ('\n') автоматически конвертируется в '\r\n'
   - Для отключения преобразования используйте режим 'wb' и ручное управление байтами

5. Производительность:
   - Используйте буферизацию для частых мелких записей
   - Для больших объемов данных собирайте строки в памяти перед записью
   - Избегайте частого открытия/закрытия файлов в циклах

6. Типичные ошибки:
   - Попытка записи в файл, открытый в режиме чтения
   - Забывание добавлять символы новой строки (\n)
   - Неправильная обработка кодировок (особенно не-ASCII символов)
   - Потеря данных при использовании 'w' вместо 'a'

7. Форматы данных:
   - CSV: простой табличный формат
   - JSON: для структурированных данных
   - INI: для конфигурационных файлов
   - XML: для сложных иерархических данных
   - YAML: для человеко-читаемых конфигов

8. Дополнительные возможности:
   - print() может использоваться для записи в файл
     with open('output.txt', 'w') as f:
         print("Hello file!", file=f)
   - Для больших файлов используйте асинхронную запись (asyncio)
   - Для параллельной записи используйте блокировки (threading.Lock)
"""