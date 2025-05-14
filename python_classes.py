"""
КОНСПЕКТ ПО КЛАССАМ В PYTHON
Источник: https://www.w3schools.com/python/python_classes.asp
"""

# =============================================
# 1. Основы классов и объектов
# =============================================

# 1.1 Создание класса
class Person:
    # Конструктор (инициализатор)
    def __init__(self, name: str, age: int):
        self.name = name  # Атрибут экземпляра
        self.age = age
    
    # Метод экземпляра
    def greet(self) -> str:
        return f"Hello, my name is {self.name}"

# 1.2 Создание объекта
alice = Person("Alice", 30)
print(alice.greet())  # Hello, my name is Alice

# =============================================
# 2. Наследование и полиморфизм
# =============================================

# 2.1 Дочерний класс
class Student(Person):
    def __init__(self, name: str, age: int, student_id: str):
        super().__init__(name, age)  # Вызов родительского конструктора
        self.student_id = student_id
    
    # Переопределение метода
    def greet(self) -> str:
        return f"I'm student {self.name}, ID: {self.student_id}"

# 2.2 Использование
bob = Student("Bob", 20, "S12345")
print(bob.greet())  # I'm student Bob, ID: S12345

# =============================================
# 3. Инкапсуляция и свойства
# =============================================

class BankAccount:
    def __init__(self, balance: float):
        self.__balance = balance  # Приватный атрибут
    
    # Геттер
    @property
    def balance(self) -> float:
        return self.__balance
    
    # Сеттер
    @balance.setter
    def balance(self, value: float):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = value

account = BankAccount(1000)
account.balance = 1500  # Используем сеттер
print(account.balance)  # 1500 (используем геттер)

# =============================================
# 4. Классовые и статические методы
# =============================================

class MyClass:
    count = 0  # Атрибут класса
    
    def __init__(self):
        MyClass.count += 1
    
    @classmethod
    def get_count(cls) -> int:
        return cls.count
    
    @staticmethod
    def info() -> str:
        return "This is MyClass"

obj1 = MyClass()
obj2 = MyClass()
print(MyClass.get_count())  # 2
print(MyClass.info())       # This is MyClass

# =============================================
# 5. Специальные методы (магические методы)
# =============================================

class Vector:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
    # Перегрузка оператора сложения
    def __add__(self, other: 'Vector') -> 'Vector':
        return Vector(self.x + other.x, self.y + other.y)
    
    # Строковое представление
    def __str__(self) -> str:
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(1, 4)
print(v1 + v2)  # Vector(3, 7)

# =============================================
# 6. Практические примеры
# =============================================

# 6.1 Класс для работы с геометрическими фигурами
class Circle:
    PI = 3.14159  # Константа класса
    
    def __init__(self, radius: float):
        self.radius = radius
    
    @property
    def area(self) -> float:
        return self.PI * self.radius ** 2
    
    @classmethod
    def from_diameter(cls, diameter: float) -> 'Circle':
        return cls(diameter / 2)

circle = Circle.from_diameter(10)
print(f"Area: {circle.area:.2f}")  # Area: 78.54

# 6.2 Обработка исключений в классе
class Temperature:
    def __init__(self, celsius: float):
        self.celsius = celsius  # Использует сеттер
    
    @property
    def celsius(self) -> float:
        return self._celsius
    
    @celsius.setter
    def celsius(self, value: float):
        if value < -273.15:
            raise ValueError("Absolute zero violation")
        self._celsius = value
    
    @property
    def fahrenheit(self) -> float:
        return self._celsius * 9/5 + 32

try:
    temp = Temperature(-300)  # Вызовет ошибку
except ValueError as e:
    print(e)  # Absolute zero violation

"""
КЛЮЧЕВЫЕ ТЕЗИСЫ:
1. Классы создаются через ключевое слово class, конструктор через __init__
2. Наследование: class Child(Parent), super() для доступа к родительским методам
3. Инкапсуляция:
   - Приватные атрибуты через __name
   - Управление доступом через @property, @setter
4. Специальные методы:
   - __str__ для строкового представления
   - __add__ для перегрузки операторов
5. Классовые методы (@classmethod) работают с классом, статические (@staticmethod) - без доступа к экземпляру/классу
6. Полиморфизм: переопределение методов в дочерних классах
7. Best practices:
   - Используйте композицию вместо наследования где возможно
   - Документируйте публичные методы
   - Соблюдайте принцип единственной ответственности
8. Исключения:
   - Обрабатывайте ошибки в сеттерах
   - Используйте пользовательские исключения для бизнес-логики
"""