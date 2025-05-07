from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def __init__(self, area):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rect = Rectangle(17, 94)
print(rect.area())