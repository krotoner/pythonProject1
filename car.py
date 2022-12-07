class Car:
    def __init__(self, stamp, model, maxSpeed, prestige):
        self.stamp = stamp
        self.model = model
        self.maxSpeed = maxSpeed
        self.prestige = prestige
        self.user = "none"

    def newUser(self, user):
        self.user = user

    def clearUser(self):
        self.user = "none"

    def updatePrestige(self,newPrestige):
        self.prestige = newPrestige

    def informationOnCar(self):
        print("information on client:")
        print(self.stamp)
        print(self.model)
        print(self.maxSpeed)
        print(self.prestige)
        print(self.user)
        print("___________________")

client1 = Car("lada","kalina","120","VIP")
client1. informationOnCar()
