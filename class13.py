num = 13
ty = type(num) == int
ty
isin = isinstance(num, int)
isin


def checker(x):
    if(type(x)== int or type(x)== float):
        print('{} is number'.format(x))
    elif(type(x) == str):
        print('{} is string'.format(x))
    else:
        print('{}'.format(x))
        print('This is not a number or string')

num = 12
name="sam"
x= [1,2,3]
y=(1,2,3)
checker(num)
checker(name)
checker(x)
checker(y)

def display(x):
    if(type(x) is list):
        for i in x:
            print(i, end=" ")
    else:
        print("This is not a list")

a = (12,13)
b=[1,3,5,7]
display(a)
display(b)

def area_peri(r, peri_required=True):
    area = 3.14*r**2
    if(peri_required):
        peri = 2*3.14*r
        return area, peri
    return area

ra = area_peri(5,False)
ra
print()

def average(y):
    if(type(y) != list):
        print("This is not a list")
        return 0
    avg = sum(y)/len(y)
    return avg

avg = average([1,5,10])
avg
xyz = average("Samip")

