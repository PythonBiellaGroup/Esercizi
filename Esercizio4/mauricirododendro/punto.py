import math
class Punto:
    def __init__(self,initX,initY):
        self.x=initX
        self.y=initY
    #def setx(self,x):
     #   self.x=x
    #def sety(self,y):
    #    self.y=y
    #def getx(self,x):
     #   return self.x
    #def gety(self,y):
      #  return self.y    
    def distanzaDaOrigine(self):
        return math.sqrt(self.x**2+self.y**2)
    def __str__(self,d):
        print("il punto avente ascissa {} e ordinata {} ha distanza {}".format(str(self.getx()),str(self.gety()),str(d)))
class Punto3d(Punto):
    def __init__(self, initX,initY,initZ):
      Punto.__init__(self,initX,initY)
      self.z=initZ
    def distanzaDaOrigine(self):
        return math.sqrt(self.x**2+self.y**2+self.z**2)
p=Punto(3,4)
assert p.x==3
assert p.y==4
#p.setx(1)
#p.sety(2)
print (p.distanzaDaOrigine)
assert p.distanzaDaOrigine()==5.0

q=Punto3d(3,4,0)
assert q.x==3
assert q.y==4
assert q.z==0
print (q.distanzaDaOrigine)
assert q.distanzaDaOrigine()==5.0
