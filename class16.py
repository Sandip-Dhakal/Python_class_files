# import calculate
# import calculate as cal
# from calculate import diff as df
# from calculate import *

# print(cal.pi)
# pi = 3.1415
# print(diff(5,2))
# print(pi)
# print(calculate.pi)
# print(calculate.sum(3))
# print(calculate.div(2,1))

# print(abs(-23.21))
# print(math.ceil(5.23))
# print(dir(math))
# # print(dir(calculate))
# print(calculate.area_peri.__doc__)

import random as rd 
# content = dir(rd)
# print(content)

def jumble(x):
    xplit = x.split()
    result = []
    check = []
    while(True):
        index = rd.randint(0, len(xplit)-1)
        if index not in check:
            check.append(index) 
            result.append(xplit[index])
        if len(check) == len(xplit):
            print(result)
            break

txt = "I am from Pokhara where my father was born"
jumble(txt)
