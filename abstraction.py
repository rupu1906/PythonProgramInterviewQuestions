# Abstraction is the concept of hiding the complex implementation details and 
# showing only the necessary features of an object.
# In Python, you can use abstract classes and methods from the abc module to achieve 
# abstraction.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
cir=Circle(10)
print(cir.area())