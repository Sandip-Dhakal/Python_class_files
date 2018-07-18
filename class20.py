# Constructor with arguments or parameters default

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

p2 = Point(3,4)
p1 = Point()
distance = p1.distance(p2)
print(distance)