# String formating using % operator and format method
# name='Sam'
# age=20
# height=5.7
# txt='Name:\t'+name+"\nAge:\t"+str(age)+"\nHeight:\t"+str(height)
# print(txt)
# txt="Name: %s Age: %d Height: %f"%(name,age,height)
# print(txt)
# num=2.54
# txt="Numbers in different decimal places %f,%.1f,%.2f,%.3f"%(num,num,num,num)
# print(txt)

# #format method
# txt="My name is {}".format('Sam')
# print(txt)

# txt="My name is {name} {cast}".format(name='Sam', cast='Dhakal')
# print(txt)

# txt="Name: {0} Age: {1} Height: {2}".format(name,age,height)
# print(txt)

pi= 3.1415
radius = float(input("Enter a radius: "))
area = pi*radius**2
print("Area of circle with radius %.2f is %.2f"%(radius,area))

name = input("Enter your name: ")
age = input("Enter your age: ")
print('Your name is {} and age is {}'.format(name,age))