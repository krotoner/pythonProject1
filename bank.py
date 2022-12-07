class Bank():
    def __init__(self):
        self.clientBase=[]

    def addClient(self, client):
        self.clientBase.append(client)
        return self.clientBase
    
    def showByMoney(self, money):
        print("money")
        for i in self.clientBase :
           if (i.deposit_amount > money):
                print(i.full_name)

    def showByCode(self, cod):
        print("code")
        for i in self.clientBase:
            if (i.code == cod):
                print(i.full_name)

    def showByProc(self, proc):
        print("proc")
        for i in self.clientBase:
            if (i.proc_amount > proc):
                print(i.full_name)
obj6=Bank()
obj6.code=1234
obj6.full_name = "QWERTY"
obj6.data = "22.01.2007"
obj6.deposit_amount =10
obj6.proc_amount =15

obj7=Bank()
obj7.code=2222
obj7.full_name = "ASD"
obj7.data = "22.02.2017"
obj7.deposit_amount =100
obj7.proc_amount =150

obj8=Bank()
obj8.code=3333
obj8.full_name = "ZXC"
obj8.data = "22.03.2031"
obj8.deposit_amount =1000
obj8.proc_amount =151

obj9=Bank()
obj9.code=4444
obj9.full_name = "FGH"
obj9.data = "22.04.2010"
obj9.deposit_amount =10000
obj9.proc_amount =157

bank = Bank()
bank.addClient(obj6)
bank.addClient(obj7)
bank.addClient(obj8)
bank.addClient(obj9)
bank.showByMoney(70)
bank.showByProc(150)

bank.showByCode(1234)


