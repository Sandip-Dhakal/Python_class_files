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
?<=         Lookbehind assertion
?!= or ?<!  Negative Lookbehind

'''

'''
Examples:
(199\d|20[01][0-8])

1991
1989
2001
2012
2013
2022
1992

Sand(i|e{2})p
Sandip Sandeep

'''