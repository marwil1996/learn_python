#import os
#clear = lambda: os.system('cls')
#clear()

#Single Line Comment

'''
Multi
Line
Comment
'''
#print((10 + 34 * 3) / 2)
#a = 10 + 34 * 3
#b = 2
#print(a/b)

#Strings

'''
string = 'I am a string '
string1 = 'I am a string'

print(string[0])

#Reverse Indexing

print(string[-1])
print(len(string))
print(string[4:13])
print(5 * string)

'''
#Format

'''
print('I had {0} cups of {1}'.format(3, 'coffee'))
print('prices: ({x}, {y}, {z})'.format(x = 2.0, y = 1.5, z = 5))
print('The {vehicle} had {0} crashes in {1} months'.format(2,12, vehicle = 'F150'))

#{:character>}.format('string')

print('{:<20}'.format('text'))
print('{:>20}'.format('text'))
print('{:b}'.format(34)) #binary
print('{:x}'.format(75)) #hexadecimal
print('{:o}'.format(52)) #octal

'''
#Use both quotation types
#a = 'I\'m a string'
#print(a)

'''
print(5 == 3)
print(10 != 4)
print(3 < 8)
print(4 >= 18)
print(13 > 4) and (8 < 21)
'''

#If, if-else, if-elif Statements

'''
msg = 'hello'

if msg == 'hello':
	print('Hi')
else:
	print('?')

a = 7
b = 4

if a == b:
	print('True')
else:
	print('False')

msg1 = 'yo'

if msg1 == 'Hey':
	print('hi')
elif msg1 == 'yo':
	print('wassup')
else:
	print('?')

num = 40

if num > 42:
	print('true')
elif num >= 100:
	print('true')
else:
	print('err')
'''

#Ternary Operator

'''
msg = 'Hello'
me = 'Hi' if msg == 'Hello' or msg == 'Hi' else "Hey"
print(me)

a = 3
a = 7 if 3**2 > 9 else 14
print(a)
'''

#For Loop

#range(start,stop,step(increment))

'''
for i in range(1,10,2):
	print(i)

for i in range(1,100,25):
	print(i)


for i in range(0,11):
	print(i)
'''
'''
str = 'String Traversal'
for i in range(len(str)):
	print(str[i])
#OR

for char in str:
	print(char)

'''

#Nested For Loop
'''for i in range(3):
	for j in range(2):
		print(j)
'''
#10 x 10 Multiplication Table
'''
for i in range(1,11):
	print('{:<3}|'.format(i),end='') #print horizontally instead of vertically

	for j in range(1,11):
		print('{:>4}'.format(i*j),end='')

	if i == 1:
		print('\n{:#^44}'.format(''),end='')
'''

#While Loop

'''
condition = 10

while condition != 0:
	print(condition)
	condition = condition - 1

#Used for infinite loops, good to include break statements
#Can also use continue statements

'''
'''
while True:
	print('infinite')
	break

for i in range(1,11):
	if i ==5:
		continue
	print(i)
'''

#Functions
'''
def function():
	print('1st function')

function()

def returning():
	return 'I am a result'
'''
'''If function not returning correctly
assign it to variable and print it'''
'''
'''
'''
result = returning()
print(result)

def multival():
	return 'this is a result,' ,2

print(multival())
'''
'''
def parameters(a):
	print(a)

parameters('This is a parameter')

def add(a,b):
	c = a + b
	return c

result = add(12,5)
result2 = add('one', 'time')
print(result)
print(result2)
'''
'''

Default Parameters, Scope, Nested Functions

def default_param(a, b = 4, c =5):
	return a + b + c

result = default_param(3)
#3 assigned to variable not given value in function definition
print(result)

def scope(a):
	a = a + 1
	print(a)
	return a
'''
'''Keep in mind a is only defined WITHIN the function,
cant say print(a)'''

'''
scope(5)

def outer(a):

	def nested(b):
		return b * a; #Use semicolon w/ nested functions
	a = nested(a)
	return a

print(outer(4))

def f(a):

	def g(b):

		def h(c):
			return a * b * c
		return h
	return g

print(f(5)(2)(3))
'''

#Recursive Functions

'''def factorial(n):
	if n == 1:
		return 1
	else:
		return n * factorial(n - 1)

print(factorial(5))


#Two different recursion methods

#Regular Recursion
def sum(n):
	if n == 1:
		return 1
	else:
		return n + sum(n-1)

#Recursion w/ Repeating Parameter

def tail_sum(n, accumulator = 0):
	if n == 0:
		return accumulator
	else:
		return tail_sum(n-1, accumulator+n)

print(sum(10))
print(tail_sum(10))'''

#Lambda functions

'''
f = lambda x, y: x + y

print(f(2,3))

func = lambda a: lambda b: lambda c: a*b*c
print(func(3)(4)(5))

func2 = lambda c: lambda a, b: lambda d: (c * (a + b)) % d

print(func2(6)(2,2)(9))
'''

#Exceptions and Errors

'''try:
	a = 5/0
except Exception as e:
	print(e)'''

'''try:
	sum = 0
	file = open('numbers.txt', 'r')
	for number in file:
		sum = sum + 1.0/int(number)
	print(sum)
except ZeroDivisionError:
	print("number in file equal to zero")
except IOError:
	print('File DNE')

'''
'''try:
	n = int(input("Enter an integer: "))
except ValueError:
	print('Not an integer')'''

'''*******Got SublimeRepl installed and working*******
-Preferences > Package Control > Install Package > SublimeRepl 
-Create build system -- Tools > Build system > New build system
-Put this code within curly brackets:
	"target": "run_existing_window_command",
	"id": "repl_python_run",
	"file":"config/Python/Main.sublime-menu"

-Save as sublimerepl-python.sublime-build
-In tab w/ python code Tools > Build System > sublimerepl-python
'''
'''try:
	sum = 0
	file = open('numbers.txt', 'r')
	for number in file:
		sum = sum + 1.0/int(number)
	print(sum)
except ZeroDivisionError:
	print("number in file equal to zero")
except IOError:
	print('File DNE')
finally:
	print(sum)
	file.close()'''

'''
a = 'a'

def RaiseException(a):
	if type(a) != type('a'):
		raise ValueError('Not a string')
try:
	RaiseException(a)
except ValueError as e:
	print(e)

def TestCase(a, b):
	assert a < b, 'a is greater than b'
try:
	TestCase(2,1)
except AssertionError as e:
	print(e)
'''

#Data Input Function

'''
age = input('How old are you: ')
print(age)
'''

#File Managment - Reading

#open(filename, access, buffering)

#file = open("C:\\Users\\Custom PC\\Desktop\\file.txt", 'r')
'''
print(file.read())
print(file.read(3))
print(file.tell())
file.seek()
file.close()
'''
'''
for line in file:
	print(line)

file.close()
'''
'''
print('File Name: ' + file.name)
print('is closed: ' + str(file.closed))
print('Mode ' + file.mode)
'''
#File Management - Writing

'''
file = open('write.txt','w+') #Make file for reading/writing
file.write('Hello file. I am string')
file.seek(0)
print(file.read())
file.close
'''

#Data Structures - Tuples

'''tup = (1, 'abc', 2, 'cde')
tup1 = 3, 'efg', True'''

'''print(tup)
print(tup[1])'''

'''try:
	tup[3]=5
except Exception as e:
	print(e)
'''
#Add element to tuple
'''tup = tup[0:4] + (5,)
print(tup)
print(tup * 4)
print(3 in tup1)'''

'''For loop using tuples. Tuples are useful for returning
multiple results from a function'''
'''for x in ('a', 'b', 'c'):
	print(x)

def mult_results():
	return(1,2,'a')
print(mult_results())
print((1,2,3)==(1,2))'''

#Tuple Functions

'''tup = (2,3,4)
print(len(tup))
print(max(tup))
print(min(tup))'''

#Data Structures - Lists

'''list1 = [1, 'abc', (2,3)]
print(list1[2])
print(list1[2][1])
print('abc' in list1)
print(3 in list1)
print(list1 == [1])
print(list1[:2])
list1.append(6) #or list1[len(list1):] = [7]
print(list1)'''

#List Functions

'''import functools

print(list(map(lambda x: x**2 + 3*x + 1, [1,2,3,4])))
print(list(filter(lambda x: x < 4, [1,2,3,4,5])))
print(functools.reduce(lambda x, y: x*y, [1,2,3,4]))'''

#Data Structures - Dictionaries

#key, value

'''dict1 = {'Key' : 'Value', ('K', 'E', 'Y'):5}
dict2 = {x: x + 1 for x in range(10)}
print(dict1)
print(dict2)
print(dict1['Key'])

try:
	print(dict1[1])
except Exception as e:
	print(e)

print(dict1.keys())
print(dict1.values())
dict1[1] = 2
print(dict1)
del dict1[1]
print(dict1)
#dict1.clear() '''

#Shallow Copies w/ Dictionaries

'''two copies of a data structure
that share same set of elements'''

'''dict1 = {'Item': 'Shirt', 'Size': 'Medium', 'Price': 50}
dict2 = dict1
dict1['Size'] = 'Small'
print(dict1)
print(dict2)'''

#Data Structures - Sets
'''Objects that contain a collection
of unique elements. Used for removing duplicates, basic math'''

'''set1 = set(['one', 'two', 'three', 'one'])
print(set1) #removed duplicate

set2 = set(['two', 'three', 'four'])
print(set1 | set2) #joins them and removes duplicates
print(set1 ^ set2) #prints same items between the two
print(set1 - set2) #prints what's not in both, unique to one

#Can assign to variable as well

a = set1 - set2
print(a)
print(a != set2)
print(a >= set1)
set1.add('five')
print(set1)'''

#Set Functions

'''set1 = set(['one', 'two', 'three'])
set2 = set(['four', 'five', 'six'])
print(set.union(set1, set2)) #combine sets, can also use set.intersection
print(set.difference(set1, set2))
print(set.difference(set2,set1))'''

#Modules

#import prime #as pr - can import w/ alias

#import a function from module and not whole function

#from prime import PrimesTo
import prime
#prime.PrimesTo(100)
#PrimesTo(100)

print(dir(prime))