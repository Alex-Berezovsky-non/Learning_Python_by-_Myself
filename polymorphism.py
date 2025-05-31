"""
КОНСПЕКТ ПО ПОЛИМОРФИЗМУ В PYTHON
Источник: https://www.w3schools.com/python/python_polymorphism.asp
"""

# =============================================
# 1. Основные концепции полиморфизма
# =============================================

# Полиморфизм = "множество форм" (греч.)
# Объекты разных классов могут использоваться через общий интерфейс

# 1.1 Встроенный полиморфизм
print(len("Hello"))  # 5 (строка)
print(len([1, 2, 3]))  # 3 (список)

# 1.2 Полиморфизм в операторах
print(3 + 5)  # 8 (сложение чисел)
print("Py" + "thon")  # Python (конкатенация строк)

# =============================================
# 2. Полиморфизм через наследование
# =============================================

class Animal:
    def speak(self) -> str:
        return "Звук животного"

class Dog(Animal):
    def speak(self) -> str:
        return "Гав!"

class Cat(Animal):
    def speak(self) -> str:
        return "Мяу!"

# 2.1 Функция, работающая с любым Animal
def animal_sound(animal: Animal) -> str:
    return animal.speak()

# Использование
dog = Dog()
cat = Cat()
print(animal_sound(dog))  # Гав!
print(animal_sound(cat))  # Мяу!

# =============================================
# 3. Утиная типизация (Duck Typing)
# =============================================

# "Если что-то выглядит как утка и крякает как утка, то это утка"
# Не важно какой класс, важно какие методы есть у объекта

class Car:
    def move(self) -> str:
        return "Машина едет"

class Boat:
    def move(self) -> str:
        return "Лодка плывет"

# 3.1 Общая функция для любых объектов с move()
def transport_action(vehicle):
    return vehicle.move()

# Использование
car = Car()
boat = Boat()
print(transport_action(car))   # Машина едет
print(transport_action(boat))  # Лодка плывет

# =============================================
# 4. Абстрактные базовые классы (ABC)
# =============================================

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius
    
    def area(self) -> float:
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side: float):
        self.side = side
    
    def area(self) -> float:
        return self.side ** 2

# 4.1 Полиморфная обработка фигур
shapes = [Circle(5), Square(4)]
for shape in shapes:
    print(f"Площадь: {shape.area():.2f}")
    # Площадь: 78.50
    # Площадь: 16.00

# =============================================
# 5. Полиморфизм в перегрузке операторов
# =============================================

class Vector:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
    def __add__(self, other: 'Vector') -> 'Vector':
        return Vector(self.x + other.x, self.y + other.y)
    
    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

# Использование
v1 = Vector(2, 3)
v2 = Vector(1, 4)
print(v1 + v2)  # (3, 7) - работает полиморфно для всех Vector

# =============================================
# 6. Практические примеры
# =============================================

# 6.1 Полиморфное чтение файлов
class TextReader:
    def read(self, filename: str) -> str:
        with open(filename, 'r') as f:
            return f.read()

class CSVReader:
    def read(self, filename: str) -> list:
        import csv
        with open(filename) as f:
            return list(csv.reader(f))

# Общий интерфейс
readers = [TextReader(), CSVReader()]
for reader in readers:
    data = reader.read("data.csv")
    print(type(data))  # str -> list

# 6.2 Плагинная архитектура
class PluginBase:
    def execute(self):
        pass

class LoggerPlugin(PluginBase):
    def execute(self):
        return "Логирование..."

class AnalyticsPlugin(PluginBase):
    def execute(self):
        return "Аналитика данных..."

# Загрузка плагинов
plugins = [LoggerPlugin(), AnalyticsPlugin()]
for plugin in plugins:
    print(plugin.execute())

"""
КЛЮЧЕВЫЕ ТЕЗИСЫ:
1. Формы полиморфизма в Python:
   - Переопределение методов в дочерних классах
   - Утиная типизация (Duck Typing)
   - Перегрузка операторов
   - Встроенные полиморфные функции (len(), + и т.д.)

2. Преимущества:
   - Унифицированный интерфейс для разных объектов
   - Гибкость и расширяемость кода
   - Снижение связанности компонентов

3. Основные техники:
   - Абстрактные базовые классы (ABC) для определения интерфейсов
   - Проверка типов через isinstance() или hasattr()
   - Единая обработка объектов через общие методы

4. Best practices:
   - Предпочитайте утиную типизацию строгой проверке типов
   - Используйте ABC для сложных иерархий
   - Документируйте ожидаемые методы и свойства

5. Отличия от статически типизированных языков:
   - Нет явных интерфейсов (кроме ABC)
   - Динамическая диспетчеризация методов
   - Возможность полиморфизма без общего родителя

6. Практическое применение:
   - Плагинные системы
   - Обработка разных форматов данных
   - Работа с API разных сервисов
   - Реализация паттернов проектирования (Стратегия, Адаптер)
"""