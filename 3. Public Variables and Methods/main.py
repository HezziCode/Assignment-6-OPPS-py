class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} is starting.")

    def stop(self):
        print(f"{self.brand} is stopping.")

my_car = Car("Civic")
my_car.start()
my_car = Car("Toyota")
my_car.start()
my_car.stop()