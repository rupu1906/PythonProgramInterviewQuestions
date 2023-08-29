# Composition and aggregation are mechanisms to combine objects to create more complex ones.
# Composition is a strong relationship where one object contains another, 
# while aggregation is a weaker relationship where one object is associated with another.

class Engine:
    def start(self):
        print("Engine started.")

class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        print("Car started.")
        self.engine.start()
car =Car()
car.start()