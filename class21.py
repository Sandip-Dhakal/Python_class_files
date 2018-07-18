def checkArms(num):
    num2str = str(num)
    n = len(num2str)
    sum=0
    for x in num2str:
        sum += int(x)**n
    if(sum == num):
        return num
    else:
        return None

# arms = []
# for x in range(1001):
#     if(checkArms(x) != None):
#         arms.append(x)

# Composite for loop
arms  = [x for x in range(1001) if checkArms(x)!=None]

print(arms)
    