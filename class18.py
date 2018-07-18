# def is_date_valid(date_as_string):
#         day, month, year = map(int, date_as_string.split('-'))
#         return day <= 31 and month <= 12 and year <= 3999

# what = is_date_valid('41-11-2010')
# print(what)

list1 = ['Sandip', 'dhakal', 'Rambazar','Hello']
for id, val in enumerate(list1):
    print(id,val)

def mapper(x):
    return x**2

list1 = ['name','age']
list2 = ['sam',14]
list3 = zip(list1,list2)
for first, second in list3:
    print(first, second)
dic = dict(list3)
dic


#List comprehension vs map, filter and reduce

list1 = list(range(-10,10))
list2 = [x/10 for x in list1]
print(list2)

list3 = list(map(mapper, list2))
print(list3)

list1 = list(range(20))
list2 = [x for x in list1 if x%2 == 0]
print(list2)

list3 = list(filter(lambda x: x%2 == 0, list1))
print(list3)

