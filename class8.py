''' Quize question

print('Please choose the correct option')
print('1. Which of the following is keyword?')
print('\t1. in\t2. on','\t3. into\t4. off',sep='\n')
op1 = int(input('Enter your option: '))
print('2. Which of the following is string operator?')
print('\t1. *\t2. \\','\t3. /\t4. ^',sep='\n')
op2 = int(input('Enter your option: '))
if(op1==1 and op2==1):
    print("Wow you are the winner")
else:
    print("Sorry try again")

'''
txt = "Lorem aliquip ad adipisicing deserunt minim officia anim velit."
print(txt.capitalize())
print(txt.title())   
# txt = 'Susil'  
# print(txt.center(10,'a'))
print(txt.count('i',6,11))  
print(txt.find('z'))

