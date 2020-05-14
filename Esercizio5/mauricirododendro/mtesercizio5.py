class Conto_corrente:
    saldo=0
    def versa(self, somma):
        self.saldo +=somma
    def preleva(self, somma):
        self.saldo -=somma
    def setSaldo (self, somma):
        self.saldo=somma
    def stampaSaldo(self):
        print(str(self.saldo))
c= Conto_corrente()
c.setSaldo(100)
c.stampaSaldo()
c.preleva(20)
c.stampaSaldo()
c.versa(10)
c.stampaSaldo()

class Conto_speciale(Conto_corrente):
    limite=60
    def versa(self,assegno):
        self.saldo += assegno
    def preleva(self,somma):
        if somma <=self.limite:
            if somma <=self.saldo:
                self.saldo -=somma
            else:
                print("manca la copertura")
        else:
            print ("da questo conto puoi prelevare fino a :", self.limite)
s=Conto_speciale()
s.setSaldo(200)
s.stampaSaldo()
s.preleva(70)
#è un assegno ma tanto chi lo sa?
s.versa(10)
s.preleva(60)
s.stampaSaldo()
    
