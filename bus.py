class MyClass2():

    def __init__(self, speed, capacity, maxSpeed):
        self.speed = speed
        self.capacity = capacity
        self.maxSpeed = maxSpeed

    def add(self, count):
        while count <= self.capacity:
            count += 1
            return count

    def add2(self):
        if self.speed < self.maxSpeed:
            self.speed += 20
            return self.speed


c1 = MyClass2(40, 30, 100)
print("Увеличение скорости:", c1.add(5))
