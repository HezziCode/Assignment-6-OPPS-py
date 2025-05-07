class Engine:
    
    def start (self):
        print("\nEngine started...🚗")

    def stop (self):
        print("\nEngine stopped🛑")

class Car():
    def __init__(self, engine):
        self.engine = engine


e1 = Engine()
c1 = Car(e1)
c1.engine.start()
c1.engine.stop()
