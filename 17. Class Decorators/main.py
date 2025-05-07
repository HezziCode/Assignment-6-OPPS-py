def add_greetings(cls):
    def greet(self):
        return"\nHello from Me!"
    cls.greet = greet
    return cls
    
@add_greetings
class Person():
    def __init__(self, name):
        self.name = name

p = Person("Huxaifa")
print(p.greet())
print(p.name)