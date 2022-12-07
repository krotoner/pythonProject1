import math


class MyClass:
    def __init__(self, SideTriangleOne, SideTriangleTwo):
        self.SideTriangleOne = SideTriangleOne
        self.SideTriangleTwo = SideTriangleTwo
        self.SideTriangleThree = (SideTriangleOne ** 2 + SideTriangleTwo ** 2) ** 0.5

    def __iadd__(self, percent):
        self.SideTriangleOne + (self.SideTriangleOne * percent * 0.01)
        return percent

    def radius(self):
        return self.SideTriangleThree / 2

    def angle(self):
        AngleTriangleOne = math.asin(self.SideTriangleOne / self.SideTriangleThree)
        AngleTriangleTwo = math.asin(self.SideTriangleTwo / self.SideTriangleThree)
        AngleTriangleThree = 90
        return AngleTriangleOne, AngleTriangleTwo, AngleTriangleThree

    def perimeter(self):
        return self.SideTriangleOne + self.SideTriangleTwo + self.SideTriangleThree


c1 = MyClass(4, 3)
print("Увеличение на проценты: ", c1.__iadd__(100))
print("Радиус: ", c1.radius())
print("Периметр: ", c1.perimeter())
print("Углы треугольника: ", c1.angle())

