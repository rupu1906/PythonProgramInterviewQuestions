# Static polymorphism
class Calculator:
    def add(self, a, b=0):
        return a + b

calc = Calculator()
result1 = calc.add(5)
result2 = calc.add(5, 3)


# Dynamic polymorphism
class Animal:
    def speak(self):
        return "BOOOO"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

dog = Dog()
cat = Cat()
animal = Animal()
print(dog.speak())  # Output: "Woof!"
print(cat.speak())  # Output: "Meow!"

print(animal.speak())