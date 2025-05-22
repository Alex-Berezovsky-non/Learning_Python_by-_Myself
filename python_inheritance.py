"""
КОНСПЕКТ ПО НАСЛЕДОВАНИЮ В PYTHON
Источник: https://www.w3schools.com/python/python_inheritance.asp
"""

# =============================================
# 1. Базовое наследование
# =============================================

class Animal:
    def __init__(self, name: str):
        self.name = name
    
    def speak(self) -> str:
        return "Звук животного"

class Dog(Animal):  # Наследование от Animal
    def speak(self) -> str:  # Переопределение метода
        return "Гав!"

# Использование
animal = Animal("Неизвестное")
dog = Dog("Бобик")
print(animal.speak())  # Звук животного
print(dog.speak())     # Гав!

# =============================================
# 2. Метод super() и расширение функциональности
# =============================================

class Cat(Animal):
    def __init__(self, name: str, breed: str):
        super().__init__(name)  # Вызов родительского конструктора
        self.breed = breed
    
    def speak(self) -> str:
        base_sound = super().speak()
        return f"{base_sound} Мяу!"

# Использование
cat = Cat("Мурка", "Дворняжка")
print(cat.speak())  # Звук животного Мяу!

# =============================================
# 3. Множественное наследование
# =============================================

class Flyable:
    def fly(self) -> str:
        return "Лечу!"

class Bird(Animal, Flyable):  # Множественное наследование
    def speak(self) -> str:
        return "Чирик!"

# Использование
bird = Bird("Кеша")
print(bird.speak())  # Чирик!
print(bird.fly())    # Лечу!

# =============================================
# 4. Порядок разрешения методов (MRO)
# =============================================

class A:
    def test(self):
        return "A"

class B(A):
    def test(self):
        return "B"

class C(A):
    def test(self):
        return "C"

class D(B, C):
    pass

# Определение порядка MRO
print(D.mro())  # [D, B, C, A, object]

# Использование
d = D()
print(d.test())  # B (следуем порядку D -> B -> C -> A

# =============================================
# 5. Абстрактные базовые классы (ABC)
# =============================================

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius
    
    def area(self) -> float:  # Реализация абстрактного метода
        return 3.14 * self.radius ** 2

# Использование
# shape = Shape()  # Ошибка: нельзя создать экземпляр абстрактного класса
circle = Circle(5)
print(circle.area())  # 78.5

# =============================================
# 6. Практические примеры
# =============================================

# 6.1 Иерархия сотрудников
class Employee:
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary
    
    def get_info(self) -> str:
        return f"{self.name}: {self.salary}"

class Manager(Employee):
    def __init__(self, name: str, salary: float, department: str):
        super().__init__(name, salary)
        self.department = department
    
    def get_info(self) -> str:
        return f"{super().get_info()}, отдел: {self.department}"

manager = Manager("Иван", 150000, "IT")
print(manager.get_info())  # Иван: 150000, отдел: IT

# 6.2 Миксины (Mixin-классы)
class JSONSerializableMixin:
    def to_json(self) -> str:
        import json
        return json.dumps(self.__dict__)

class Product(JSONSerializableMixin):
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

product = Product(1, "Ноутбук")
print(product.to_json())  # {"id": 1, "name": "Ноутбук"}

"""
КЛЮЧЕВЫЕ ТЕЗИСЫ:
1. Наследование позволяет повторно использовать код и создавать иерархии
2. Основные концепции:
   - Переопределение методов
   - Расширение функционала через super()
   - Множественное наследование
3. Порядок MRO определяется алгоритмом C3 (выводится через класс.mro())
4. Абстрактные классы (ABC) задают интерфейс для дочерних классов
5. Миксины - классы с дополнительной функциональностью для композиции
6. Best practices:
   - Избегайте глубоких иерархий наследования
   - Используйте композицию вместо наследования где возможно
   - Для общего поведения предпочитайте миксины множественному наследованию
   - Документируйте ожидаемые методы в абстрактных классах
7. Особенности Python:
   - Нет интерфейсов как в Java, но их можно имитировать через ABC
   - Множественное наследование требует аккуратного проектирования
   - super() динамически определяет родительский класс
8. Типичные ошибки:
   - Алмаз смерти (diamond problem) в множественном наследовании
   - Неполная реализация абстрактных методов
   - Неправильное использование MRO
"""