class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Person(metaclass=SingletonMeta):
    def __init__(self, name, surname, weight, salary):
        self.name = name
        self.surname = surname
        self.weight = weight
        self.salary = salary

# Приклад використання
person1 = Person("John", "Doe", 70, 50000)
person2 = Person("Alice", "Smith", 65, 60000)

print(person1.name, person1.surname, person1.weight, person1.salary)
# Виведе: John Doe 70 50000

print(person2.name, person2.surname, person2.weight, person2.salary)
# Виведе: John Doe 70 50000

print(person1 is person2)  # Виведе True, оскільки це один і той самий об'єкт Person
