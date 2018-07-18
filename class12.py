#Input arguments
# 1. Required Arguments
def sum1(x, y):
    return x+y

sum1(2,3)
# sum(4)

# 2. Default/Keyword Arguments
def sum2(x,y=1):
    return x+y

print(sum2(2,3))
print(sum2(2))
print(sum2(x=4,y=1))
print(sum2(y=4,x=7))

# Checking data type of input arguments
def repeater(x,y=2):
    if isinstance(x,str):
        return x*y
    
print(repeater("Sandip"))
print(repeater(5))
