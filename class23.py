class Circle:
    pi = 3.14159265

    def __init__(self):
        self.angle = 360*Circle.pi/3.14159265

    @staticmethod
    def area_peri(r=1):
        area = Circle.pi*r**2
        peri = 2*Circle.pi*r
        return area, peri

    @classmethod
    def volume(cls, r=1, h=1):
        area, _ = cls.area_peri(r)
        vol = area * h
        return vol

# area, peri = Circle.area_peri(2)
# vol = Circle.volume(2,1)
# print(area)
# print(peri)
# print(vol)
# h1 = Circle()
# Circle.pi = 3
# h2 = Circle()
# print(h1.angle)
# print(h2.angle)



class Animal(object):
    
    def __init__(self, name = "Animal", legs = 4):
        self.name = name
        self.legs = legs
        
    def walk(self):
        print(self.name, "is walking")
        

# hero = Animal('Sushil', 2)

class Hero(Animal):
    "This is hero class"
    
    def __init__(self, name='Hero', legs=2,level=1):
        super(Hero,self).__init__(name, legs)
        self.level=level

    def saveHeroine(self):
        super(Hero,self).walk()
        print('I can save life')

    def __str__(self):
        return "My name is {} with {} legs".format(self.name, self.legs)
 
    def __del__(self):
        print(self.name, "am dead ")
        
# hero2 = Hero()
# hero2.name = "Sushil"
# print(hero2.name)
# print(Hero.__dict__)
# print(hero2.__dict__)
# print(hero2.__doc__)
# print(Hero.__bases__)
# print(dir(hero2))

# print(hero2)
# del hero2

class Point:
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance(self, point2):
        "Calculates distance between current point to given point2"
        x = point2.x - self.x
        y = point2.y - self.y
        d = x**2 + y**2
        return d**0.5

    def __str__(self):
        return "x: %d, y: %d"%(self.x,self.y) 

    def __add__(self , other):
        return Point(self.x+other.x, self.y+other.y )

    def __sub__(self , other):
        return Point(self.x-other.x, self.y-other.y )

    def __ge__(self, other):
        if(self.x > other.x):
            return 0
        else: 
            return -1

# p2 = Point(3,4)
# p1 = Point(1,4)
# p3 = p1 + p2
# p4 = p2 - p1
# print(p3)
# print(p4)
# xm = p1 >= p2
# print(xm)
