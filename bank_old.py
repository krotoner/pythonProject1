class Client:

    def __init__(self, code, full_name, data, deposit_amount, percentage):
        self.code = code
        self.full_name = ""
        self.data = ""
        self.deposit_amount = deposit_amount
        self.proc_amount = percentage


class Bank(Client):
    def __init__(self, code, full_name, data, deposit_amount, percentage):
        super().__init__(code, full_name, data, deposit_amount, percentage)
        self.full_name = full_name
        self.clientBase = []

    def addClient(self, client):
        self.clientBase.append(client)

    def showByMoney(self, money):
        for i in range(len(self.clientBase)):
            if self.clientBase[i].deposit_amount > money:
                print(self.clientBase[i].full_name)
        return

    def showByCode(self, cod):
        return

    def showByProc(self, proc):
        return


bank = Bank(2386, "Danil", "18.11.2005", 15, 4)

client1 = Bank(2386, "Danil", "18.11.2005", 15, 4)
client2 = Bank(2386, "D", "18.11.2005", 15, 4)

bank.addClient(client1)
bank.addClient(client2)

bank.showByMoney(10)

