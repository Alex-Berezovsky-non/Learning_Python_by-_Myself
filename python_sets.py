"""
ПОЛНЫЙ КОНСПЕКТ ПО МНОЖЕСТВАМ (SETS) В PYTHON
Источник: https://www.w3schools.com/python/python_sets.asp
"""

# =============================================
# 1. Создание и базовые операции
# =============================================

# 1.1 Создание множеств
set1 = {"apple", "banana", "cherry"}  # Инициализация с элементами
set2 = set()                          # Пустое множество (не используйте {})
set3 = set("hello")                   # {'h', 'e', 'l', 'o'} (уникальные символы)

# Элементы должны быть НЕИЗМЕНЯЕМЫМИ (числа, строки, кортежи)
valid_set = {1, 2.5, "text", (1, 2)}
# invalid_set = {[1, 2]}  # Ошибка: список изменяемый

print(set3)  # {'o', 'e', 'h', 'l'}

# 1.2 Основные свойства:
# - Неупорядоченные
# - Уникальные элементы
# - Быстрые проверки наличия элемента

# =============================================
# 2. Основные методы множеств
# =============================================

# 2.1 Добавление/удаление
numbers = {1, 2, 3}
numbers.add(4)             # {1, 2, 3, 4}
numbers.remove(3)          # Удаляет элемент (KeyError если нет)
numbers.discard(10)        # Удаляет без ошибки если нет
popped = numbers.pop()     # Удаляет случайный элемент

# 2.2 Очистка и копирование
numbers.clear()            # Очистка множества
copy_set = set3.copy()     # Поверхностная копия

# =============================================
# 3. Операции с множествами
# =============================================

a = {1, 2, 3}
b = {3, 4, 5}

# 3.1 Объединение (union)
print(a | b)           # {1, 2, 3, 4, 5}
print(a.union(b))      # Аналогично

# 3.2 Пересечение (intersection)
print(a & b)           # {3}
print(a.intersection(b))

# 3.3 Разность (difference)
print(a - b)           # {1, 2}
print(a.difference(b))

# 3.4 Симметричная разность (symmetric difference)
print(a ^ b)           # {1, 2, 4, 5}
print(a.symmetric_difference(b))

# =============================================
# 4. Неизменяемые множества (frozenset)
# =============================================

frozen = frozenset([1, 2, 3])
# frozen.add(4)  # Ошибка: frozenset неизменяем

# Использование как ключи словаря:
dict_with_frozenset = {frozen: "value"}

# =============================================
# 5. Практические примеры
# =============================================

# 5.1 Удаление дубликатов из списка
duplicates = [1, 2, 2, 3, 3, 3]
unique = list(set(duplicates))  # [1, 2, 3]

# 5.2 Проверка подмножества
set_a = {1, 2}
set_b = {1, 2, 3}
print(set_a.issubset(set_b))  # True

# 5.3 Поиск общих элементов
tags1 = {"python", "coding", "tutorial"}
tags2 = {"tutorial", "development", "python"}
common = tags1 & tags2  # {'python', 'tutorial'}

# 5.4 Фильтрация уникальных гласных в строке
text = "programming is awesome"
vowels = {c for c in text if c in "aeiou"}  # {'a', 'o', 'i', 'e'}

"""
КЛЮЧЕВЫЕ ТЕЗИСЫ:
1. Множества хранят уникальные неупорядоченные элементы
2. Элементы должны быть хешируемыми (неизменяемыми типами)
3. Основные операции: объединение (|), пересечение (&), разность (-), симметричная разность (^)
4. Методы: add(), remove(), discard(), union(), intersection(), difference()
5. frozenset — неизменяемая версия множества
6. Быстрые операции проверки наличия: O(1) в среднем случае
7. Используйте множества для:
   - Удаления дубликатов
   - Проверки принадлежности
   - Математических операций с наборами данных
8. Не поддерживают индексацию (для доступа используйте циклы)
9. Генераторы множеств: {x for x in iterable}
10. Пустое множество создается через set(), а не {}
"""