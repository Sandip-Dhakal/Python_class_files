#this is module for regular expression and its implementation in python
'''
regex: to search or match regular expression
. any character
* wild card any number of data 
+ search multiple pattern as previous
() is used to group patterns and | is used for or

Single character                    quantity                position
\d 0-9          \D not numeric      *   0 or more           ^ start of line
\w [a-zA-Z0-9]  \W not character    +   1 or more           $ end of line
\s space        \S not space        ?   0 or 1              \b word boundary/ words between spaces
. any character                     {min, max}
[ ] match any char in [].            {n}
[^ ] match character not in [].

Look ahead Assertion

?=          Look ahead 
?!          Negative lookahead
'''

'''
Examples:
(199\d|20[01][0-8])
1991 1989 2001 2012 2013 2022 1992

Sand(i|e{2})p
Sandip Sandeep
'''

import re

## String to be scanned to find the pattern.
# line = "this color is not 123sd fsd23 and OK! colour colours"
# line = 'sandipdhakal@gmail.com'
# line = 'This is the this and at end is this' 
# line = "1234567890, 12345  and  9876543210"

# pattern = r'\d'
# pattern = r'.*\d{3}.*'
# pattern = r'[a-zA-z0-9]+'
# pattern = r'\S+@gmail.com'
# pattern = r'\w+@\w{5}.com'
# pattern = r'colou?rs?'
# pattern = r'^this'
# pattern = r'(t|T)his'
# pattern = r'this$'
# pattern = r'\b\d{10}\b'
# pattern = r'colou?rs?'

# matchObj = re.match(pattern, line)
# if matchObj:
#     print('Match:',matchObj.group())
# else:
#     print('No Match!')

# matchObj = re.search(pattern, line, re.M|re.I)
# if matchObj:
#     print('Search:',matchObj.group())
# else:
#     print('No Match!')

# matchObj = re.findall(pattern, line)
# if matchObj:
#     print('FindAll: ',matchObj)
# else:
#     print('No Match')

##Boundary \b in regex
# 

#Grouping in python 
line = "9834567890"
pattern = r'\b(\d{3})(\d{3})(\d{4})\b'
matchObj = re.search(pattern, line)
if matchObj:
    # print(matchObj.groups())
    print('Phone:', matchObj.group())
    print('Formatted:', "(",matchObj.group(1),')-',matchObj.group(2),'-',matchObj.group(3), sep='')
else:
    print('No Match')

##Greedy and Non Greedy matching
# pattern = "cookie"
# sequence = "Cake and cookie"

# #Greedy
# heading  = r'<h1>TITLE</h1>'
# print(re.match(r'<.*>', heading).group())
# #Non greedy
# print(re.match(r'<.*?>', heading).group())

##Assertion

# passwords = ('passwor','passwords','p4ssword','passw0rd','p45sword')

# print('-----No Assertion-----')
# for password in passwords:
#     match = re.match(r'^\w{8,12}$',password)
#     if match:
#         print(password,': matches')
#     else:
#         print(password,': does not match')

# print('-----Assertion-----')

# for password in passwords:
#     match = re.match(r'(?=.*\d.*)^\w{8,12}$',password)
#     if match:
#         print(password,': matches')
#     else:
#         print(password,': does not match')

# inputs = ("There was a crime incident","The incident involved a theft","The theft was a serious incident")
# for ins in inputs:
#     match = re.match(r'(?!.*theft).*incident.*',ins)
#     if match:
#         print(ins,': matches')
#     else:
#         print(ins,': does not match')


##Substituting regex pattern with new string

# pattern = r'\.com'
# replace = '.net.np'

# email = 'sandipdhakal9497@gmail.com helpme@hotmail.com'
# new_email = re.sub(pattern, replace, email)
# print(new_email)
