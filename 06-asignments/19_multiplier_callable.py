class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, number):
        return self.factor * number

# Example
m = Multiplier(5)
print(callable(m))
print(m(10))
