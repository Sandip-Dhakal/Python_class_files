# Python class Exercises files repo
This is repository for the python class. You can access the contents as per the class date and compare with
the class notes. Feel free to add your knowledge and create a pull request

## Contents 

1. [Lines](#lines)	
2. [Comments](#comments)	
3. [Blocks and indentation](#blocks-and-indentation)	
4. Variables	
5. Expressions and Statements	
6. Interactive Mode Vs Script Mode	
7. Function call	
8. Variables and Values	
    * Number Values	
    * Number Type Conversion	
9. Basic Operators	
10. Types of Operator	
    * Python Arithmetic Operators	
    * Python Comparison Operators	
    * Python Assignment Operators	
    * Python Bitwise Operators	
    * Python Logical Operators	
    * Python Membership Operators	
    * Python Identity Operators	
    * Python Operators Precedence	
11. Decision Making	
    * If statement:	
    * if...else statement	
    * The elif Statement	
    * Nested IF Statements	
    * Single Statement Suites	
12. Loops	
    * Loop Control Statements 
    * for Loop Statements	
    * The range() function	
    * Nested loops	
    * Break Statement	
    * continue Statement	
    * pass Statement	
    * Iterator and Generator	
13. Strings	
    * Accessing Values in Strings	
    * Updating Strings	
    * Escape Characters	
    * String Special Operators	
    * String Slicing/SubString	
    * String Formatting Operator	
    * String format() method	
    * String Methods	
14. Lists	
    * Python Lists	
    * Accessing Values in Lists	
    * Updating Lists	
    * Delete List Elements	
    * Basic List Operations	
    * Indexing, Slicing and Matrixes	
    * Built-in List Functions and Methods	
15. Tuples	
    * Accessing Values in Tuples	
    * Updating Tuples	
    * Delete Tuple Elements	
    * Basic Tuples Operations	
    * Indexing, Slicing, and Matrixes	
    * No Enclosing Delimiters	
    * Built-in Tuple Functions	
16. Dictionary	
    * Accessing Values in Dictionary	
    * Updating Dictionary	
    * Delete Dictionary Elements	
    * Properties of Dictionary Keys	
    * Built-in Dictionary Functions and Methods
17. Functions	
    * Pass by Reference vs Value	
    * Function Arguments	
    * Required Arguments	
    * Keyword Arguments	
    * Default Arguments	
    * Variable-length Arguments	
    * Anonymous Functions	
    * return Statement	
    * Scope of Variables	
    * Global vs. Local variables	
    * Things to know about functions	
18. Iterators and generators	
19. Modules	
    * The import Statement	
    * Executing Modules as Scripts	
    * Locating Modules	
    * The PYTHONPATH Variable	
    * Namespaces and Scoping	
    * The dir( ) Function	
    * The globals() and locals() Functions	
    * The reload() Function	
    * Packages in Python	
20. Object Oriented	
    * Overview of OOP Terminology	
    * Creating Classes	
    * Creating Instance Objects	
    * Accessing Attributes	
    * Built-In Class Attributes	
    * Destroying Objects (Garbage Collection)	
    * Class Inheritance	
    * Overriding Methods	
    * Base Overloading Methods	
    * Overloading Operators	
    * Data Hiding	
21. Exceptions Handling	
    * Standard Exceptions	
    * Assertions in Python	
    * What is Exception?	
    * The except Clause with No Exceptions	
    * The except Clause with Multiple Exceptions	
    * The try-finally Clause	
    * Argument of an Exception	
    * Raising an Exception	
    * User-Defined Exceptions	
22. Files I/O	
    * Opening and Closing Files	    * 
    * The file Object Attributes	
    * Reading and Writing Files	
    * Reading and Writing using With Statement	
    * File Positions	
    * Renaming and Deleting Files	
    * Directories in Python	
    * File and Directory Related Methods	
    * File Methods	
23. Multithreaded Programming	
    * The Threading Module	
    * Creating Thread Using Threading Module	
    * Synchronizing Threads	


### Lines

1.	Python does what you want it to do most of the time so that you only have to add
    extra characters some of the time.
2.	Statement separator is a semicolon, but is only needed when there is more than 
    one statement on a line. And, writing more than one statement on the same line is
    considered bad form.
3.	Continuation lines -- A backslash as last character of the line makes the following line a continuation     of the current line. But, note that an opening "context" (parenthesis, square bracket, or curly bracket)    makes the backslash unnecessary.

### Comments
Everything after "#" on a line is ignored. No block comments, but doc strings are a
comment in quotes at the beginning of a module, class, method or function. Also, editors
with support for Python often provide the ability to comment out selected blocks of code,
usually with "##".

#### Names and tokens
* Allowed characters: az – AZ 09 underscore, and must begin with a letter or underscore.
* Names and identifiers are case sensitive.
* Identifiers can be of unlimited length.
* Special names, customizing, etc. Usually begin and end in double underscores.
* Special name classes Single and double underscores.
    * Single leading single underscore Suggests a "private" method or variable name. Not imported by "from module import *".
    * Single trailing underscore Use it to avoid conflicts with Python keywords.
    * Double leading underscores Used in a class definition to cause name mangling (weak hiding). But, not often used.
* Naming conventions Not rigid, but:
    * Modules and packages all lower case.
    * Globals and constants Upper case.
    * Classes Bumpy caps with initial upper.
    * Methods and functions All lower case with words separated by underscores.
    * Local variables Lower case (with underscore between words) or bumpy caps with initial lower or your choice.
    * Good advice Follow the conventions used in the code on which you are working.
* Names/variables in Python do not have a type. Values have types.

### Blocks and indentation
Python represents block structure and nested block structure with indentation, not with begin and end brackets. The empty block Use the pass noop statement. Benefits of the use of indentation to indicate structure:
* Reduces the need for a coding standard. Only need to specify that indentation is 4 spaces and no hard tabs.
* Reduces inconsistency. Code from different sources follow the same indentation style. It has to.
* Reduces work. Only need to get the indentation correct, not both indentation and brackets.
* Reduces clutter. Eliminates all the curly brackets.
* If it looks correct, it is correct. Indentation cannot fool the reader.

### Variables 
1.	Variables are memory allocated in RAM to store data/value;
2.	Variable names are usually meaningful — they document what the variable is used for.
3.	Variable names can be as long as you like.
    a.	They can contain both letters and numbers but they can’t begin with a number.
    b.	It is legal to use uppercase letters, but it is conventional to use only lowercase for variables names, Eg, myNameIs, myFirstVariable
    c.	The underscore character, _, can appear in a name. It is often used in names with multiple words, Eg. your_name or airspeed_of_unladen_swallow.	
4.	Variable names cannot be reserved words
    > **False 	class 	finally 	is 	return None 	continue 	for 	lambda 	try True 	def 	from 	nonlocal 	while and 	del	global 	not 	with as 	elif	if 	or 	yield assert 	else 	import 	pass break 	except 	in 	raise**  

### Expressions and Statements
An expression is a combination of values, variables, and operators. A value all by itself is considered an expression, and so is a variable, so the following are all legal expressions:
```python 
>>>42
42
# A statement is a unit of code that performs certain task.
>>> n = 17
>>> print(n)
#The first line is an assignment statement that gives a value to n. The second line is a print statement that displays the value of n.
```

### Interactive Mode Vs Script Mode
*	Writing in directly on python shell is interactive mode.
*	Simple way to use Interactive Mode is by running python in command prompt. (cmd)
*	We directly interact with python interpreter
```python
>>> a = 15
>>> print(a)
```
*	Save code in a file called a script. 
*	Python scripts have names that end with .py i.e. file extension.
*	Run the script file using “python file.py”.

### Function call
*	Function is like machine. It takes certain input variables and gives certain output.
*	It is common to say that a function “takes” an argument and “returns” a result. The result is also called the return value.
*	We can identify using () parenthesis.

Syntax: function_name(input arguments)
E.g.
```python
>>> print(“Hello World”)
```

### Variables and Values
#### Number Values
Python supports different numerical types:
*	**int** (signed integers) − They are often called just integers or ints. They are positive or negative whole numbers with no decimal point. Integers in Python 3 are of unlimited size. Python 2 has two integer types - int and long. There is no 'long integer' in Python 3 anymore.
*	__float__ (floating point real values) − Also called floats, they represent real numbers and are written with a decimal point dividing the integer and the fractional parts. Floats may also be in scientific notation, with E or e indicating the power of 10 (2.5e2 = 2.5 x 102 = 250).
*	__complex__ (complex numbers) − are of the form a + bJ, where a and b are floats and J (or j) represents the square root of -1 (which is an imaginary number). The real part of the number is a, and the imaginary part is b. Complex numbers are not used much in Python programming.
