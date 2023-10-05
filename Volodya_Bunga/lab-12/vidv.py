
class Shape:
    def accept(self, visitor):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def accept(self, visitor):
        visitor.visit_circle(self)


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def accept(self, visitor):
        visitor.visit_rectangle(self)


class AreaCalculator:
    def visit_circle(self, circle):
        area = 3.14 * circle.radius ** 2
        print(f"Площа кола: {area}")

    def visit_rectangle(self, rectangle):
        area = rectangle.width * rectangle.height
        print(f"Площа прямокутника: {area}")


circle = Circle(5)
rectangle = Rectangle(4, 6)

calculator = AreaCalculator()

circle.accept(calculator)
rectangle.accept(calculator)
