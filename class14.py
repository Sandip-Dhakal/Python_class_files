def display(*args):
    for x in args:
        print(x)

display("Sam")
display((2,4,5,6))
display(23)

def sum( *args):
    total=0
    print(len(args))
    for x in args:
        total += x
    return total

print(sum(23))
print(sum(23,34,12))
print(sum(23,34,12,45,65,89))

def average( *args):
    total= count=0
    print(len(args))
    for x in args:
        total += x
        count += 1
    return total/count

print(average(23))
print(average(23,34,12))
print(average(23,34,12,45,65,89))

def displayX( **kwargs):
    for k, v in kwargs.items():
        print(k)
        print(v)

# displayX(23)
# displayX({"Name" = 'Sam', 'Age'=13})
displayX(Name='Sam')

def order(x,y=0,*args, **kwargs):
    print("I am require:")
    print(x)
    print("I am default:")
    print(y)
    print("I am *args:")
    print(args)
    print("I am **kwargs:")
    print(kwargs)

order(34,12,23, Name='sam', Age=45)

name = 'Sam'
def disAge():
    age = 14
    print(name, age)

def disAddress():
    address = 'Amarsingh'
    print(name, address)
    # print(name, age)

disAge()
disAddress()
# print(age)
print(name)

def disName():
    # global name
    name = 'Sun'
    print(name)

disName()
print(name)


# Single line statements list comprehensions and function
std = 13
kim = "Sandip" if std>13 else 45
kim

std = {'Name':'Sam', 'Age':13}
kim = [k for k, v in std.items()]
kim
data = list(range(1,21))
data2 = [x**2 for x in data if x %2 == 0]
data2
rim = [k for k, v in std.items()] if len(std) >1 else [2,3,4] 
rim



# lambda function
fun1 = lambda x: x+1
print(fun1(3))

#Generator and Iterator
def gen(n=1):
    "Generates number from 1 to given number"
    assert (type(n) == int and n >=1 ), "The input should be int and greater than 1"
    x = 1
    while x <= n:
        yield x
        x+=1


# for i in gen(2):
#     print(i)
num = [i for i in gen(2)]
print(num)