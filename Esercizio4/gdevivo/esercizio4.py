import math

class Point():
    def __init__(self, x, y, z=0.0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        
    def reset(self):
        self.x = 0
        self.y = 0
        self.z = 0
    
    def distance(self, p2):
        if isinstance(p2, Point):
            return math.sqrt( (self.x - p2.x )**2 + (self.y - p2.y)**2 + (self.z - p2.z)**2)
        else:
            raise Exception("Not point.")
    
    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+","+str(self.z)+")"

p1=Point(2,5)
print(p1)
p2=Point(4,-9)
print(p2)
print(p1.distance(p2))
p3=Point(7,2,-3)
print(p3)
print(p1.distance(p3))
print(p2.distance(p3))
