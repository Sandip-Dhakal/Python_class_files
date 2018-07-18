#static or class variables as global scope

class TempConverter:
    # for global nature we have created static variable
    globalStatic = 5

    def __init__(self):
        self.check = TempConverter.globalStatic

    #temperature converter methods
    @staticmethod
    def farehToCel(fahren=0):
        return 5/9*(fahren - 32)

# #global nature through object
# h1 = TempConverter()
# print(h1.check)
# TempConverter.globalStatic = 10
# h2 = TempConverter()
# print(h2.check)

# print('%.2f'%(TempConverter.farehToCel(108)))

#hiding data Access Modifier
class Volume:
    pi = 3.14159265
    _pi = 3.141592
    __pi = 3.1415    #private static variable
    
    def __init__(self, r=1):
        self.r = r
        self.__random = 2   #private instance variable

    def _area(self):
        area = 3*Volume.pi*self.r*self.__random
        _area = 3*Volume._pi*self.r
        __area = 3*Volume.__pi*self.r
        return area,_area,__area

    def __area(self):   # private method
        area = 2*Volume.pi*self.r
        _area = 2*Volume._pi*self.r
        __area = 2*Volume.__pi*self.r*self.__random
        return area,_area,__area

    def volume(self, h=1):
        area,_,_ = self.__area()
        return area*h


v1 = Volume(r=2)
# print(v1.r)
# print(v1.__random)

print(dir(Volume))
print()
print()
print(dir(v1))

# vol = v1.volume()
# print(vol)
# print(v1._area())
# v1.__area()
# Volume.__pi
# print(dir(v1))


#Exception and how to handle
#Exception class is base class of all exception
#try except else and finally

txt = 'xfe'
# num = int(txt)

# try:
#     num = int(txt)
# except:
#     print('The value in txt should be numbers')

# try:
#     num = int(txt)
# except ValueError:
#     print('The value in txt should be numbers')

# try:
#     num = int(txt)
# except ValueError as ve:
#     print(ve)

# txt = '23'
# try:
#     num = int(txt)
# except ValueError:
#     print('There is value error exception')
# else:                                       #executes if there is no exception
#     print('There was no exception')
# finally:                                    #finally block executes if there is exception or not
#     print('I run no matter what!!')

def display(name, value):
    if value == 0:
        raise LookupError('The value should not be 0')
    elif value < 0:
        raise RuntimeError('The value should not be less than 0')
    else:
        print('My name is', name)

# display('Rocky',-1)
# display('Rocky',0)
# display('Rocky',12)

# try:
#     display('Rocky',0)
# except LookupError:
#     print('The value is zero')
# except RuntimeError as rte:
#     print(rte)

#user defined exception

class MyException(Exception):
    
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return self.msg

    def display(self):
        print('Error:',self.msg)

def display2(name, value):
    if value == 0:
        raise MyException('The value should not be 0')
    print('My name is', name)
        
# display2('Rocky',0)
# try:
#     display2('Rocky',0)
# except MyException as id:
#     id.display()