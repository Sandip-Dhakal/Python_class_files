# class Fruit:
#     # class or static variable
#     name = "Fruit"

#     # method
#     def displayName(self):
#         "this method is fruity"
#         print("I am fruit")

#     def displayV(self):
#         "This method os random"
#         # instance variable
#         self.variety = "Apple"
#         print(self.variety)


# apple = Fruit()
# apple.displayName()
# apple.displayV()
# print(apple.name)
# print(Fruit.name)
# print(apple.variety)
# # print(Fruit.variety)

# class Fruit:
    
#     def __init__(self):
#         self.name = "Fruit"
#         self.size = 10
#         self.juicy = True
#         print("I am created")

#     def givesVitA(self):
#         print("I give vitA")


# orange = Fruit()
# apple = Fruit()
# print(orange.name)
# print(apple.name)
# orange.name = "Orange"
# apple.name = "Apple"
# print(orange.name)
# print(apple.name)




# class Hero:
    
#     #constructor
#     def __init__(self, name = "Sam", level=1, alive=True):
#         #initialize instance variables
#         self.name = name
#         self.level = level
#         self.alive = alive

#     def __str__(self):
#         return "Hero name: {} level: {}".format(self.name, self.level)    

#     def displayName(self):
#         print(self.name)

#     def setName(self, name):
#         self.name = name
        

# hero1 = Hero()
# print(hero1)
# hero1.displayName()

# Old method of Inheritence

# class Animal:
    
#     def __init__(self, name = "Animal", legs = 4):
#         self.name = name
#         self.legs = legs
        
#     def walk(self):
#         print(self.name, "is walking")
        

# hero = Animal('Sushil', 2)
# hero.walk()

# class Hero(Animal):
    
#     def __init__(self, name='Hero', legs=2,level=1):
#         Animal.__init__(self, name, legs)
#         self.level=level

#     def saveHeroine(self):
#         print('I can save life')
        
# hero = Hero()
# hero.saveHeroine()
# hero.walk()
# print(hero.name)

#New method
class Animal(object):
    
    def __init__(self, name = "Animal", legs = 4):
        self.name = name
        self.legs = legs
        
    def walk(self):
        print(self.name, "is walking")
        

hero = Animal('Sushil', 2)

class Hero(Animal):
    
    def __init__(self, name='Hero', legs=2,level=1):
        super(Hero,self).__init__(name, legs)
        self.level=level

    def saveHeroine(self):
        super(Hero,self).walk()
        print('I can save life')
 
        
hero = Hero()
hero.saveHeroine()
hero.walk()
print(hero.name)

# class Human:
    
#     def __init__(self, name, level=1):
#         self.name = name
#         self.level = level

#     def displayName(self):
#         print(self.name)

# class Hero(Human):
    
#     def __init__(self, name, alive=True):
#         self.alive = alive
#         Human.__init__(self,name)

#     def displayAlive(self):
#         print(self.alive)

#     # Override method
#     def displayName(self):
#         Human.displayName(self)
#         print("I am also a Hero")

# hero2 = Hero("Sandy")
# hero2.displayName()
# hero2.displayAlive()

# New method of Inheritence using super() method
# class Human(object):
    
#     def __init__(self, name, level=1):
#         self.name = name
#         self.level = level

#     def displayName(self):
#         print(self.name)

# class Hero(Human):
#     'This is the class for Hero'
    
#     def __init__(self, name, alive=True):
#         self.alive = alive
#         super(Hero, self).__init__(name)

#     def displayAlive(self):
#         print(self.alive)

#     # Override method
#     def displayName(self):
#         super(Hero , self).displayName()
#         print("I am also a Hero")

# hero2 = Hero("Sandy")
# print(hero2.level)
# hero2.displayName()
# hero2.displayAlive()

# print(Hero.__dict__)
# print(hero2.__dict__)
# print(hero2.__doc__)
# print(Hero.__name__)
# print(Hero.__bases__)
# print(dir(hero2))

