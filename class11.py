# methods and functions

# def displayName(str):
#     # '''

#     # '''
#     "THis is used to display program name" 
    
#     print("Hello", str)

# print(displayName.__doc__)
# print(type.__doc__)

# def printinfo(*args, **kwargs):
#     for x in args:
#         if(isinstance(x,(list, dict, tuple))):
#             for y in x:
#                 print(y)
#         else:
#             print(x)
            
#         print(kwargs)
    
#     for k,v in kwargs.items():
#         print(k,v)

# dic = {"Name":"Sam", "Age":19}   
# tup = (1,2,4,5)
# printinfo(70,50,10,Name="Sam", Age=47)
# printinfo(tup, dic)

# # global vs local scope
# x=5
# def test1():
#     print(x)

# def test2():
#     x=2
#     print(x)

# def test3():
#     global x
#     x=4
#     print(x)

# test1()
# test2()
# print(x)
# test3()
# print(x)

# #iterator and generator
# list1 = [1,2,3,4]
# iterator = iter(list1)
# for x in iterator:
#     print(x) 

# def function(count = 5):
#     sum = 0
#     for x in range(count):
#         yield x
#         sum += x
    

# sums = function()
# # while True:
# #     try:
# #         print(next(sum))
# #     except StopIteration as si:
# #         break

# for x in sums:
#     print(x)


# Creating methods
def sum(x,y):
    "This method gives sum of x and y"
    return x+y

def printsum(x,y):
    z=x+y
    print(z)

def namer(a):
    "Takes a string a and splits into list of string values"
    z= a.split()
    return z

# using methods
print(sum(2,3))
printsum(4,7)

name = namer("Sandip Dhakal")
name