class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print( self.name + " says Woof!")
        print(self.breed)

my_dog = Dog("Buddy", "German Shepherd")

my_dog.bark()