class Client:

    def __init__(self, userName):
        self.userName = userName
        self.rating = 4.62
        self.status = ""
        self.updateStatus(self.rating)

    def updateStatus(self, newRating):
        self.rating = newRating

        regular = "regular"
        intermediate = "intermediate"
        revoked = "revoked"
        VIP = "VIP"

        if newRating >= 4 and newRating < 4.5:
            self.status = regular
            return
        elif newRating >= 4.5 and newRating < 4.75:
            self.status = intermediate
            return
        elif newRating >= 4.75 and newRating <= 5:
            self.status = VIP
            return
        elif newRating >= 0 and newRating < 4:
            self.status = revoked
            return

    def informationOnClient(self):
        print("information on client:")
        print(self.userName)
        print(self.rating)
        print(self.status)
        print("___________________")


client1 = Client("ivan")
client1.informationOnClient()
client1.updateStatus(5)
client1.informationOnClient()
