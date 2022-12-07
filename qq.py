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
        self.clientBase = []
        self.full_name = full_name

    def addClient(self):
        self.clientBase.append(self.full_name)
        return self.clientBase


client1 = Bank(2386, "Danil", "18.11.2005", 15, 4)
print(client1.addClient())
