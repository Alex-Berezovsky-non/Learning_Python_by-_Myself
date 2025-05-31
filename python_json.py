"""
КОНСПЕКТ ПО РАБОТЕ С JSON В PYTHON
Источник: https://www.w3schools.com/python/python_json.asp
"""

import json

# =============================================
# 1. Основные концепции JSON
# =============================================

# JSON (JavaScript Object Notation) - текстовый формат для хранения и передачи данных
# Основные структуры:
#   - Объекты: { "key": "value" }
#   - Массивы: [ "item1", "item2" ]
#   - Типы данных: строки, числа, булевы, null

# Соответствие Python ↔ JSON:
#   Python      →     JSON
#   dict        →     Object
#   list, tuple →     Array
#   str         →     String
#   int, float  →     Number
#   True        →     true
#   False       →     false
#   None        →     null

# =============================================
# 2. Кодирование (Python → JSON)
# =============================================

# 2.1 Преобразование Python объекта в JSON строку
data = {
    "name": "Alice",
    "age": 30,
    "is_student": False,
    "courses": ["Math", "CS"],
    "address": None
}

json_string = json.dumps(data)
print(json_string)
# {"name": "Alice", "age": 30, "is_student": false, "courses": ["Math", "CS"], "address": null}

# 2.2 Форматирование вывода
pretty_json = json.dumps(data, indent=4, sort_keys=True)
print(pretty_json)
"""
{
    "address": null,
    "age": 30,
    "courses": [
        "Math",
        "CS"
    ],
    "is_student": false,
    "name": "Alice"
}
"""

# 2.3 Запись в файл
with open("data.json", "w") as file:
    json.dump(data, file, indent=2)

# =============================================
# 3. Декодирование (JSON → Python)
# =============================================

# 3.1 Преобразование JSON строки в Python объект
json_data = '{"name": "Bob", "age": 25, "hobbies": ["gaming", "reading"]}'
python_obj = json.loads(json_data)
print(python_obj["name"])  # Bob

# 3.2 Чтение из файла
with open("data.json", "r") as file:
    loaded_data = json.load(file)
    print(loaded_data["courses"])  # ['Math', 'CS']

# =============================================
# 4. Обработка сложных объектов
# =============================================

# 4.1 Кастомное кодирование (для неподдерживаемых типов)
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

def custom_encoder(obj):
    if isinstance(obj, User):
        return {"name": obj.name, "email": obj.email}
    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")

user = User("Charlie", "charlie@example.com")
user_json = json.dumps(user, default=custom_encoder)
print(user_json)  # {"name": "Charlie", "email": "charlie@example.com"}

# 4.2 Кастомное декодирование
def custom_decoder(dct):
    if "name" in dct and "email" in dct:
        return User(dct["name"], dct["email"])
    return dct

decoded_user = json.loads(user_json, object_hook=custom_decoder)
print(decoded_user.name)  # Charlie

# =============================================
# 5. Обработка ошибок
# =============================================

# 5.1 Невалидный JSON
invalid_json = "{'name': 'Dave'}"  # Одинарные кавычки не разрешены в JSON

try:
    data = json.loads(invalid_json)
except json.JSONDecodeError as e:
    print(f"Ошибка декодирования: {e.msg} в позиции {e.pos}")

# 5.2 Несовместимые типы
try:
    json.dumps({1, 2, 3})  # Множество не поддерживается
except TypeError as e:
    print(f"Ошибка: {str(e)}")

# =============================================
# 6. Практические примеры
# =============================================

# 6.1 Конфигурация приложения
config = {
    "debug_mode": True,
    "max_connections": 10,
    "database": {
        "host": "localhost",
        "port": 5432
    }
}

with open("config.json", "w") as f:
    json.dump(config, f, indent=2)

# 6.2 Работа с API
import requests

response = requests.get("https://api.github.com/users/octocat")
user_data = response.json()
print(f"User: {user_data['login']}, Repos: {user_data['public_repos']}")

# 6.3 Сравнение данных
data1 = {"a": 1, "b": 2}
data2 = {"b": 2, "a": 1}
print(json.dumps(data1) == json.dumps(data2))  # False (разный порядок ключей)
print(json.dumps(data1, sort_keys=True) == json.dumps(data2, sort_keys=True))  # True

"""
КЛЮЧЕВЫЕ ТЕЗИСЫ:
1. Основные функции:
   - json.dumps() - Python объект → JSON строка
   - json.dump()  - Python объект → JSON файл
   - json.loads() - JSON строка → Python объект
   - json.load()  - JSON файл → Python объект

2. Параметры сериализации:
   - indent: форматирование с отступами
   - sort_keys: сортировка ключей
   - ensure_ascii: экранирование не-ASCII символов
   - separators: управление разделителями

3. Обработка ошибок:
   - JSONDecodeError: при невалидном JSON
   - TypeError: при попытке сериализации неподдерживаемых типов

4. Кастомная сериализация:
   - default: функция для обработки неподдерживаемых типов
   - object_hook: функция для кастомного декодирования

5. Best practices:
   - Всегда используйте UTF-8 для работы с JSON
   - Проверяйте данные при загрузке из ненадежных источников
   - Для сложных структур используйте pydantic или dataclasses
   - Для сохранения порядка ключей используйте OrderedDict

6. Применение:
   - Конфигурационные файлы
   - Обмен данными через API
   - Сериализация состояния приложения
   - Хранение данных NoSQL (MongoDB, Elasticsearch)
   - Логирование структурированных данных

7. Альтернативные форматы:
   - YAML: для конфигов с комментариями (PyYAML)
   - TOML: для простых конфигов (tomllib)
   - MessagePack: бинарная альтернатива JSON (msgpack)
   - BSON: бинарный JSON (используется в MongoDB)
"""