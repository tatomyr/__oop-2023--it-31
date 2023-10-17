from abc import ABC, abstractmethod
import copy


class Shape(ABC):
    def __init__(self):
        self.x = None
        self.y = None

    @abstractmethod
    def clone(self):
        pass


class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def clone(self):
        return copy.deepcopy(self)


class Circle (Shape):
    def __init__(self, x, y, radius):
        super().__init__()
        self.x = x
        self.y = y
        self.radius = radius

    def clone(self):
        return copy.deepcopy(self)


# Код для первірки роботи патерну.

circle = Circle(0, 0, 7)
rectangle = Rectangle(10, 10, 8, 5)

shape_list = [circle, rectangle]
copy_shape_list = []

# Метод clone працює для будь якого об'єкту в даному списку, чи це Rectangle, чи Circle.
for shape in shape_list:
    copy_shape_list.append(shape.clone())

print(copy_shape_list[0].x, copy_shape_list[0].y, copy_shape_list[0].radius)
print(copy_shape_list[1].x, copy_shape_list[1].y, copy_shape_list[1].width, copy_shape_list[1].height)
