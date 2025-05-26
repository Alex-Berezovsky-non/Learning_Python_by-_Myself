"""
КОНСПЕКТ ПО ИТЕРАТОРАМ В PYTHON
Источник: https://www.w3schools.com/python/python_iterators.asp
"""

# =============================================
# 1. Основные понятия
# =============================================

# 1.1 Итерируемый объект (iterable) - объект, который можно перебрать
my_list = [1, 2, 3]          # list - итерируемый
my_dict = {"a": 1, "b": 2}   # dict - итерируемый

# 1.2 Итератор (iterator) - объект с состоянием, умеющий возвращать элементы
my_iter = iter(my_list)       # Получаем итератор
print(next(my_iter))          # 1
print(next(my_iter))          # 2

# =============================================
# 2. Создание кастомного итератора
# =============================================

class CountDown:
    def __init__(self, start: int):
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        num = self.current
        self.current -= 1
        return num

# Использование
counter = CountDown(3)
for num in counter:
    print(num)  # 3 2 1

# =============================================
# 3. Генераторы как итераторы
# =============================================

# 3.1 Функция-генератор
def fibonacci(limit: int):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

# Использование
fib = fibonacci(10)
print(list(fib))  # [0, 1, 1, 2, 3, 5, 8]

# 3.2 Генераторное выражение
squares = (x**2 for x in range(5))
print(next(squares))  # 0

# =============================================
# 4. Встроенные функции для работы с итераторами
# =============================================

# 4.1 enumerate() - добавляет счетчик
for idx, val in enumerate(["a", "b", "c"]):
    print(idx, val)  # 0 a → 1 b → 2 c

# 4.2 zip() - объединяет итерируемые объекты
names = ["Alice", "Bob"]
ages = [25, 30]
zipped = zip(names, ages)
print(dict(zipped))  # {'Alice': 25, 'Bob': 30}

# =============================================
# 5. Практические примеры
# =============================================

# 5.1 Чтение больших файлов
class FileReader:
    def __init__(self, filename: str):
        self.file = open(filename, "r")
    
    def __iter__(self):
        return self
    
    def __next__(self):
        line = self.file.readline()
        if not line:
            self.file.close()
            raise StopIteration
        return line.strip()

# Использование
# for line in FileReader("data.txt"):
#     print(line)

# 5.2 Бесконечный итератор
class InfiniteCounter:
    def __init__(self):
        self.num = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.num += 1
        return self.num

# counter = InfiniteCounter()
# print(next(counter))  # 1
# print(next(counter))  # 2...

"""
КЛЮЧЕВЫЕ ТЕЗИСЫ:
1. Итераторы:
   - Объекты с методами __iter__() и __next__()
   - Сохраняют состояние между вызовами
   - Вызывают StopIteration при завершении

2. Итерируемые объекты:
   - Могут быть преобразованы в итераторы через iter()
   - Примеры: списки, кортежи, строки, словари

3. Генераторы:
   - Специальный тип итераторов
   - Создаются через функции с yield
   - Автоматически реализуют протокол итератора

4. Основные методы:
   - iter(obj) - создает итератор
   - next(iter) - получает следующий элемент
   - enumerate() - добавляет счетчик
   - zip() - объединяет итераторы

5. Best practices:
   - Используйте итераторы для обработки больших данных
   - Для простых случаев предпочитайте генераторы
   - Закрывайте ресурсы (файлы) в StopIteration

6. Особенности:
   - Цикл for автоматически работает с итераторами
   - Итератор можно пройти только один раз
   - Бесконечные итераторы требуют ручного контроля

7. Паттерны использования:
   - Ленивая загрузка данных
   - Потоковая обработка
   - Генерация последовательностей
"""