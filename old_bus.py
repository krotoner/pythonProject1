class MyClass2():
    def __init__(self, speed, capacity, maxSpeed):
        self.speed = speed
        self.capacity = capacity
        self.maxSpeed = maxSpeed
        self.hasEmptySeats = capacity

    def addCapacity(self, count):
        while count <= self.capacity:
            self.hasEmptySeats -= count
            return self.capacity - self.hasEmptySeats

    def add2(self, speed):
        if self.speed < self.maxSpeed:
             self.speed += speed
             return self.speed
    
c1 = MyClass2(40, 30, 100)
print(c1.addCapacity(5))
print(c1.add2(5))
