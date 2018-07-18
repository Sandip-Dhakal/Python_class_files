"This module is used to built simple calculator"
import math
pi =math.pi

def sum(x,y=1):
    "This method calculates sum of two numbers"
    return x+y

def diff(x,y=1):
    return x-y

def mul(x,y):
    return x*y

def div(x,y=1):
    assert ( y != 0), "Cannot be divided by zero"
    return x/y

def area_peri(r=1):
    "Calculates area and perimeter for given radius of circle"
    return pi*r**2, 2*pi*r

# print(__name__)