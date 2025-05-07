class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, input_value):
        return input_value * self.factor

    def __str__(self):
        return f"Multiplier {self.factor}"


m = Multiplier(6)
print(m(10))
print(callable(m))