# list1 = [1,2,3,4]
# print(list1[4])
# print(5/0)
# x= 'xyz'
# y= int(x)

# a1 = IndexError()
# a2 = ZeroDivisionError()
# a3 = ValueError()

#isinstance
# print(isinstance(a1, IndexError))
# print(isinstance(a1, Exception))
# print(type(a2))

#general exception handling

list1 = [1,2,3,4]
# try:    
#     print('I am inside try block')
#     print(list1[3])
# except:
#     print('There is error')

# print('I am below exception')

# a = input()
# try:
#     b=int(a)
#     print(100/b)
# except ValueError as val:
#     print(val)
# except ZeroDivisionError:
#     print('The number must not be zero')
# else:
#     print('I run if no exception created')
#     print(b+1)
# finally:
#     print('I run anyway but at last')

def div(x=1,y=1):
    if(x==1 and y==1):
        raise RuntimeError('This is due to x=1 and y=1')
    return x/y

try:
    print(div(3,2))
except RuntimeError as rte:
    print(rte)
except ZeroDivisionError:
    print('y must not be zero')
    
