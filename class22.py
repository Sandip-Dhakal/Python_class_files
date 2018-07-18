class Animal(object):
    
    def __init__(self, name = "Animal", legs = 4):
        self.name = name
        self.legs = legs
        
    def walk(self):
        print("I am walking")
        

hero = Animal('Sushil', 2)

class Hero(Animal):
    
    def __init__(self, name='Hero', legs=2,level=1):
        super(Hero,self).__init__(name, legs)
        self.level=level

    def saveHeroine(self):
        super(Hero,self).walk()
        print('I can save life')
    
    def walk(self):
        super(Hero,self).walk()
        print(self.name,'is walking')
        
        
hero = Hero(name = 'Sam')
hero.saveHeroine()
hero.walk()
print(hero.name)