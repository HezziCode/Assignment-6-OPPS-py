import time
class Countdown:
    def __init__(self, start):
        self.start = start
        self.current = start     

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        current = self.current
        self.current -= 1
        return current


for num in Countdown(3):
    print(num)
    time.sleep(0.7)
print("\nAssignment 6 Done...🥳 👀")