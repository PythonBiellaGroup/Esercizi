class CC():
    def __init__(self, owner):
        self.owner = owner
        self.__saldo = 0
        
    def versa(self, cash):
        self.__saldo += cash
    
    def preleva(self, cash):
        self.__saldo -= cash

    def getsaldo(self):
        return self.__saldo

    def setsaldo(self, cash):
        self.__saldo = cash

    def print_saldo(self):
        print (self.__saldo)
    
    def __str__(self):
        return "CC di "+self.owner+" ammonta a "+str(self.__saldo)

class Cheque():
    def __init__(self, amount):
        if amount <= 0:
            print ("Invalid amount"+amount)
        else:
            self.amount = amount

    def __int__(self):
        return self.amount

class SpecialCC(CC):
    def __init__(self, owner):
        super().__init__(owner)

    def preleva(self, cash):
        self.__cash = cash
        self.__saldo = super().getsaldo()
        if self.__cash > 250: 
            print("Somma richiesta invalida", self.__cash)
            return
        if (self.__saldo - self.__cash) < 0:
            print("Credito insufficiente", self.__saldo)
            return
        super().setsaldo(self.__saldo - self.__cash) 


c1=CC("Pippo")
print(c1)
c1.versa(100)
print(c1)
c1.preleva(150)
print(c1)
c2=SpecialCC("Pluto")
print(c2)
c2.versa(600)
print(c2)
c2.preleva(300)
print(c2)
a1=Cheque(100)
c2.versa(int(a1))
print(c2)
c2.preleva(200)
print(c2)
c2.preleva(200)
print(c2)
c2.preleva(200)
print(c2)
c2.preleva(200)
print (c2)
