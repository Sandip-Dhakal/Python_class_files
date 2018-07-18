list1 = ["Sam", "Rocky", 1989, 1890]
list2 = list1
list2
list2.clear()
list2
del list2
# list2
list1 = list(range(1,6))
list1
maxi = max(list1)
maxi
mini = min(list1)
mini
txt = "Sandip".upper()
list1 = list(txt)
list1
maxi = max(list1)
maxi
mini = min(list1)
mini
txt = "".join(list1)
txt

list2 = [1,2,3,1]
counter = list2.count("1")
counter
index = list2.index(1)
index
list2.insert(1,'a')
list2
list2 = [1,2,5,3,1,4,5,5,7]
set1 = set(list2)   #sorting and removing duplicates
set1
list2 = list(set1)
list2

# Tuple
tup1 = ("chemistry", "physics", 1989, 1999)
tup2 = (1,2,3,4,5)
tup3 = "a", "b", "c","d"
tup3
tup4=()
tup5=("a")
print(type(tup5))
tup5=("a",)
print(type(tup5))

#dictionary
dic={"Name":"Sam", "Age":15, "Name":"Susil"}
dic
dic2 = dic.keys()
dic2
dis4 = list(dic2)
dis4
dic_items = dic.items()
list2 = list(dic_items)
list2
dic_value = dic.values()
list2 = list(dic_value)
list2

for k in dic:
    print(k,dic[k])

for k, v in dic.items():
    print(k,v)

x= range(2,50,2)
y=list(x)
# for i in y:
#     if (i%4)==0:
#         print(i ,end=" " )
