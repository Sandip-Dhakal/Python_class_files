count = 6
while count < 9:
    print(count)
    count +=1

print("Hello Sandip",23,14, sep = '')
print("Hello Sandip",23,14)

for  letter in 'Sandip':  #iterating variable letter
    print(letter,end = ' ')
print()

name = ""
for letter in name:
    print(letter, end=' ')

print(list(range(5)))
print(list(range(1,11)))
print(list(range(1,13,2)))

for var in range(5):
    print (var)

for i in range(2,11):
    for j in range(1,11):
        print(i,'X',j,"=",i*j)

var1 = 'Hello World!'
print ("Updated String :-"+ var1[:6] + 'Python')
print ("Updated String :-", var1[:6] + 'Python')
print ("Updated String :-\b", var1[:6] + 'Python')
print ("Updated String :-\n", var1[:6] + 'Python',sep = '')
print ("Updated String :-\t", var1[:6] + 'Python')
print ("Updated String :-", var1[:6] *2 )
print ('This is old method to add %d'%(2))
print ('My name is %s and age is %d'%('Sam',123))
print('This is old method to add %.2f'%(2.12312))
print('This is new method to add {0:.2f}'.format(2.12312))
print('This is new method to add {1:.2f}'.format(2.12312, 3.6546))

# def op1():
#     print('Hello')

# def op2():
#     print('There')

# func = {0:op1,1:op2}
# func[1]()