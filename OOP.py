import math
class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        c = (a ** 2 + b ** 2) ** 0.5
        self.c = c

    def percentage(self, p):
        self.a = self.a + (self.a * p * 0.01)
        return self.a

    def radius(self):
        return self.c / 2

    def angle(self):
        A = math.asin(self.a / self.c) * 180
        B = math.asin(self.b / self.c) * 180
        C = 90
        return A, B, C

    def perimeter(self):
        return self.a + self.b + self.c


cl = MyClass(3, 4)
print("Увеличение на проценты:", cl.percentage(35))
print("Радиус:", cl.radius())
print("Углы:", cl.angle())
print("Периметр:", cl.perimeter())
