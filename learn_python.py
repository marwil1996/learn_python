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

#*****************************For Loop*****************************

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

#****************************Nested For Loop***************************
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

#*************************While Loop*******************************

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

#************************Functions**********************************
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

******************Default Parameters, Scope, Nested Functions*****************************

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

'''
---------------------------------------------------------------------------------------------
*******Got SublimeRepl installed and working*******
-Preferences > Package Control > Install Package > SublimeRepl 
-Create build system -- Tools > Build system > New build system
-Put this code within curly brackets:
	"target": "run_existing_window_command",
	"id": "repl_python_run",
	"file":"config/Python/Main.sublime-menu"

-Save as sublimerepl-python.sublime-build
-In tab w/ python code Tools > Build System > sublimerepl-python
---------------------------------------------------------------------------------------------
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

#File Managment - Reading -------------------------------------------------------------------

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

#Data Structures - Tuples ------------------------------------------------------------------

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

#Data Structures - Lists ------------------------------------------------------------------

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

#Data Structures - Dictionaries ------------------------------------------------------------

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

#Shallow Copies w/ Dictionaries -------------------------------------------------------

'''two copies of a data structure
that share same set of elements'''

'''dict1 = {'Item': 'Shirt', 'Size': 'Medium', 'Price': 50}
dict2 = dict1
dict1['Size'] = 'Small'
print(dict1)
print(dict2)
'''

#Data Structures - Sets --------------------------------------------------------------
'''
Objects that contain a collection
of unique elements. Used for removing duplicates, basic math
'''

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

#Set Functions ----------------------------------------------------------------------------

'''set1 = set(['one', 'two', 'three'])
set2 = set(['four', 'five', 'six'])
print(set.union(set1, set2)) #combine sets, can also use set.intersection
print(set.difference(set1, set2))
print(set.difference(set2,set1))'''

#Modules

#import prime #as pr - can import w/ alias

#import a function from module and not whole function

#from prime import PrimesTo
#import prime
#prime.PrimesTo(100)
#PrimesTo(100)

#print(dir(prime))

#Packages

#import main.sub2.prime as sub2

'''Didn't work at first, needed copy of test.py
file in main folder as ___init__'''

#sub2.PrimesTo(100)

#from main.sub2.prime import PrimesTo

#PrimesTo(100)

#Built-in Modules --------------------------------------------------------------------------

'''
import copy

my_dict = {'Key': 'Values', ('K', 'E', 'Y'):5}
my_dict1 = copy.deepcopy(my_dict)
my_dict[1] = 1
print(my_dict)
print(my_dict1)
'''

'''
import math as m
import cmath as cm #complex number module
import random as ran
import sys

print(m.cos(m.pi))
print(m.exp(3))
print(m.ceil(1.6))
print(dir(cm)) #directory, shows all functions in module
print(cm.sqrt(36))
print(cm.polar(complex(0,1)))
print(dir(ran))
print(ran.sample([1,2,3,4], 2)) #number outside square bracket is # selected randomly
print(ran.random())
print(ran.randint(5,100))
print(dir(sys))
print(sys.getrecursionlimit())
print(sys.version)
print(sys.path)
'''

#Object Oriented Programming ---------------------------------------------------------------

'''
Basic Principles

-Hiding Info - only need to know methods defined in class and purpose, no need to show implementation of class instances
-Encapsulation - All variables and instances logically grouped together
-Inheritance 
-Polymorphism
'''

'''
Class - a collection of attributes that are defined 
for any object


class Name:
	'desc'
'''

#class Complex:
#	'this class sims complex numbers'
	#def __init__(self,real,imag):
	#Constructor Method

'''I think it's weird that type imag part works 
w/o same parenthesis like type real
This works also: if(type(real) not in (int, float)) or type(imag) not in (int,float):'''
	
#def __init__(self, real = 0, imag = 0): #Function for missing positional argument
#	if(type(real) not in (int, float)) or (type(imag) not in(int,float)):
#		raise Exception('Args are not numbers')
#	self.real = real
#	self.imag = imag
		#Instance variables = constructor argument

#c = Complex(1,1)

#print(c.real, c.imag)

'''
try:
	c = Complex(2)
	print(c.real, c.imag)
except Exception as e:
	print(e)
'''
'''try:
	#c = Complex((1,2,3),[1,2,3])
	c = Complex(2,4)
	print(c.real, c.imag)
except Exception as e:
	print(e)'''

#c = Complex(2,4)
#print(c.real, c.imag)

#Started getting TypeError: Complex() takes no arguments, don't know why

#Class Methods Part I ------------------------------------------------------------------

'''
import math

class Complex:
	
	def __init__(self, real = 0, imag = 0):
		if (type(real) not in (int, float)) or type(imag) not in(int, float):
			raise Exception('Args are not numbers')
		#self.__real = real
		#self.__imag = imag
		self.SetReal(real)
		self.SetImag(imag) #This uses the method to set these values in the initialization of the instance. Supposedly the same as self.___real

	def GetReal(self):
		return self.__real
	
	def GetImag(self):
		return self.__imag
	
	def GetModulus(self):
		return math.sqrt(self.GetReal() * self.GetReal() + self.GetImag() * self.GetImag())
	
	def GetPhi(self):
		return math.atan2(self.GetImag(), self.GetReal())
	
	def SetReal(self, val):
		if type(val) not in (int, float):
			raise Exception('real part must be a number')
		self.__real = val
	
	def SetImag(self, val):
		if type(val) not in (int, float):
			raise Exception('imag part must be a number')
		self.__imag = val
'''

#Added two underscores to variables to make them private

#c = Complex(2.5, 5.2)
#print(c.GetReal(), c.GetImag())

'''c = Complex()
c.SetImag(1)
c.SetReal(2)'''

#print(c.GetReal(), c.GetImag())

'''With OOP take care to control access to data. 
User shouldn't mess with what's in the class'''

'''Define variables as private, have restrictions on what can be input'''
#c = Complex()

#try:
#	c.SetReal((1,2,3))
#except Exception as e:
#	print(e)

#This shows you can't access private values

#try:
#	c.__real
#except Exception as e:
#	print(e)

#Get this - 'Complex' object has no attribute '__real'

#c = Complex(-3,4)

#print(c.GetModulus(), c.GetPhi())

'''What's been done is calling methods from other methods'''

'''
import cmath

class Complex():
	'This class simulates complex numbers'

	def __init__(self, real = 0, imag = 0):
		self.__real = real
		self.__imag = imag

	def GetReal(self):
		return self.__real

	def GetImag(self):
		return self.__imag

	def GetModulus(self):
		return math.sqrt(self.GetReal()*self.GetReal() + self.GetImag()*self.GetImag())

	def GetPhi(self):
		return math.atan2(self.GetReal(), self.GetImag())

	def SetReal(self, val):
		if type(real) not in (int, float):
			raise Exception ('Real part must be a number')
		self.__real = val

	def SetImag(self, val):
		if type(imag) not in (int, float):
			raise Exception('Imag part must be a number')
		self.__imag = val

	def __str__(self):
		return str(self.GetReal()) + '+' + (self.GetImag()) + 'i';

	def __add__(self, other):
		return Complex(self.GetReal() + other.GetReal(), self.GetImag() + other.GetImag())

	def __mul__(self, other):
		if type(other) in (int, float):
			return Complex(self.GetReal() * other, self.GetImag() * other)
		else:
			return Complex(self.GetReal() * other.GetReal() - self.GetImag() * other.GetImag(), self.GetImag() * other.GetImag() + self.GetReal() * other.GetReal())

	def __truediv__(self, other):
		if type(other) in (int, float):
			return Complex(self.GetReal() / float(other), self.GetImag() / float(other))
		else:
			a, b, c, d = self.GetReal(), self.GetImag(), other.GetReal(), other.GetImag()
			#Nominator needed for dividing complex numbers
			nominator = c * c + d * d
			return Complex((a * c + b * d) / nominator, (b * c - a * d) / nominator)

	a = Complex(5, 0.3)
	b = Complex(-3, 4)

	print(a + b)
	print(a * b)
	print(a / b)

	#Get error saying class not defined
	'''

#Class Inheritance --------------------------------------------------------------------

#polymorphism - ability of an object to adapt to the type of data its processing
'''
Define Constructer Method
Define Getters 
Define setters if you have them
'''
'''
class Vehicle:

	def __init__(self, VIN, weight, manufacturer):
		self.vin_number = VIN
		self.weight = weight
		self.manufacturer = manufacturer

	def GetWeight(self):
		return self.weight

	def GetManufacturer(self):
		return self.manufacturer

	def VehicleType(self):
		pass

class Car(Vehicle):
	def __init__(self, VIN, weight, manufacturer, seats):
		self.vin_number = VIN
		self.weight = weight
		self.manufacturer = manufacturer
		self.seats = seats

	def NumberOfSeats(self):
		return self.seats

	def VehicleType(self):
		return 'CAR' 


class Truck(Vehicle):
	def __init__(self, VIN, weight, manufacturer, capacity):
		self.vin_number = VIN
		self.weight = weight
		self.manufacturer = manufacturer
		self.capacity = capacity

	def TransportCapacity(self):
		return self.capacity

	def VehicleType(self):
		return 'TRUCK' 

a = Car('ABC1', 1000, 'BMW', 4)
b = Truck('BCD2', 1600, 'RAM', 4)
c = Car('DEF3', 1100, 'Chevrolet', 2 )
d = Truck('WE74GH5B3C', 2000, 'GMC', 8)

print(a.GetWeight(), b.GetManufacturer(), c.NumberOfSeats(), d.TransportCapacity())

for v in [a,b,c,d]:
	print(v.GetManufacturer(), v.VehicleType())

'''

#Class object is base class of all objects and used to modify the property
'''
Also possible to use property as a decorator, sticking with Python philosophy of
having one clear way to do something
'''

#Class Inheritance Part II --------------------------------------------------------------

'''
class Complex(object):

	def __init__(self, real = 0, imag = 0):
		self._real = real
		self._imag = imag

	def GetReal(self):
		return self._real

	def GetImag(self):
		return self._imag

	def SetReal(self, real):
		if type(real) not in (int, float):
			raise Exception ('Real part must be a number!')
		self._real = real

	def SetImag(self):
		if type(imag) not in (int, float):
			raise Exception('Imag part must be a number!')
		self._imag = imag

	real = property(GetReal, SetReal)
	imag = property(GetImag, SetImag)

c = Complex()

try:
	c.real = (1,2,3)
except Exception as e:
	print(e)

print(c.real, c._imag)
'''
'''
class Student(object):

	#Student
	number_of_students = 0

	def __init__(self, name, index):
		self.name = name
		self.index = index
		Student.number_of_students += 1

	def __del__(self):
		Student.number_of_students -= 1

s1 = Student('John Doe', 1)
s2 = Student('Anne Smith', 2)

#del s1

print(Student.number_of_students, s1.number_of_students, s2.number_of_students)
'''

'''Destructors important for memory management'''

#Data Visualization ----------------------------------------------------------------

'''
Matplotlib module basic library for data viz
others include vispy, bokeh, seaborne, pygal, folium, pandas
'''
'''
import matplotlib.pyplot as plt

fig = plt.figure('Histogram')

ax = fig.add_subplot(1,1,1)

'''
#With histograms 1st param is list of numbers 
#within certain range
#2nd is # of bins to be created

'''
ax.hist([21,12,23,35,45,60,33,22,56,64,13,86,78], bins = 7, facecolor = 'b')

plt.title('Distribution')
plt.xlabel('Range')
plt.ylabel('Amount')
plt.show()

'''
'''
Two other params with histogram 

normed - True or False (false by default. If set to true the data is normalized, meaning all data set from 0-1
face color - set color of histogram
'''

'''fig2 = plt.figure('Box-plot')
ax1 = fig2.add_subplot(1,1,1)
ax1.boxplot([21,12,18,23,35,45,86,32,56,24,96,64,71])
plt.show()

fig3 = plt.figure('Bar')
ax2 = fig3.add_subplot(1,1,1)
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_title('Bars')

'''
'''
1st param - list for x-axis
2nd param - list for y-axis
3rd param - width of graph
4th param - list of colors
'''
'''
ax2.bar([0,1,2,3,], [5,10,15,20],[0.5,1,1.5,2], color = ['b','r'])
plt.show()

fig4 = plt.figure('Line')
ax3 = fig4.add_subplot(1,1,1)
ax3.set_xlim([-2,10])
ax3.set_ylim([0,6])
ax3.set_xlabel('X')
ax3.set_ylabel('Y')
ax3.plot([-1,2,4,7,8],[5,2,3,8,6], 'b')
plt.show()
'''

#Data Visualization Part III ---------------------------------------------------------

'''
import matplotlib.pyplot as plt

#Stacked Bar Graph

#Dictionary
data = {'Player' : ['Dwayne Wade', 'LeBron James', 'Kobe Bryant', 'Stephen Curry'],
		'First': [10,10,8,12],
		'Second':[12,8,14,11],
		'Third': [6,9,12,7],
		'Fourth':[16,20,24,18]}

fig = plt.figure('Stacked Bar')
ax = fig.add_subplot(1,1,1)
bar_width = 0.5
bars = [i + 1 for i in range(len(data['First']))]
ticks = [i + (bar_width/2) for i in bars]
ax.bar(bars,
		data["First"],
		width = bar_width,
		label = 'First Quarter',
		color = 'g')

ax.bar(bars,
		data['Second'],
		width = bar_width,
		bottom = data['First'],
		label = 'Second Quarter',
		color = 'y')

ax.bar(bars,
		data['Third'],
		width = bar_width,
		bottom = [i + j for i, j in zip(data['First'], data['Second'])], #for loop to make starting point of 2nd bar layer
		label = 'Third Quarter',
		color = 'b'
		), 
		
ax.bar(bars,
		data['Fourth'],
		width = bar_width,
		bottom = [i + j + k for i,j,k in zip(data['First'], data['Second'], data['Third'])],
		label = 'Fourth Quarter',
		color = 'r')

#Set player name variables on place ticks in the middle

plt.xticks(ticks, data['Player'])
ax.set_xlabel('Total')
ax.set_ylabel('Player')
plt.legend(loc = 'upper right')
plt.xlim([min(ticks) - bar_width, max(ticks) + bar_width])
plt.show()
'''

'''
Errors Corrected
1) Needed .pyplot with matplotlib
2) Used simpler color setters, ex. b instead hexadecimal
3) Wrongly had 'Fourth Quarter' in line 1029 when
the key is just 'Fourth'
'''

#Data Visualization Part III ------------------------------------------------------------------

'''
import matplotlib.pyplot as plt

fig = plt.figure('Scatter')
ax = fig.add_subplot(1,1,1)
ax.scatter([-1,0,2,3,5], [2,1,3,0.5,4])
plt.show()

#Bubble Graph

fig = plt.figure('Bubble')
ax = fig.add_subplot(1,1,1)
ax.scatter([-1,0,2,3,5], [2,1,3,0.5,4], [120,200,300,150,300], ['r', 'b', 'y', 'g', 'r'])
plt.show()
'''

'''
Got this error by missing a color, needed 5 and only had 4
ValueError: 'c' argument has 4 elements, which is inconsistent with 'x' and 'y' with size 5.
I see hexadecimal color labels are useful for using many different colors when you run out of
the simple 'r', 'b', 'y' etc labels
'''
'''
fig = plt.figure('Pie')
sizes = [50,55,44,36]
labels = ['Kings', 'Heat', 'Lakers', 'Jazz']
explode = (0.1,0,0,0)
color = ['red', 'purple', 'yellow', 'blue']
plt.pie(sizes, explode = explode, labels = labels, colors = color, autopct = '%1.1f%%', shadow = True, startangle = 140)
plt.axis('equal')
plt.show()
'''

#import matplotlib.pyplot as plt
#print(dir(plt))

#Pandas Library ---------------------------------------------------------------------------



import pandas as pd

#Download and read data from CSV file

'''
df = pd.read_csv('CASchools.csv')
#print(df['CASchools'])
#print(df['school']['grades'])
print(df['read'])
print(df['grades'])
print(df['computer'])
print(df['calworks'])

#print(dir(pd))
'''

'''
Had to use different CSV file, couldn't find one in lesson
Works if I just use print(df), don't need df[CASchools]
Also gotta remember quotes for string in list bracket
'''

#Make CSV file
'''
teams = ['Celtics', 'Bulls', 'Lakers', 'Heat']

total_chips = [18, 6, 18, 3]

data_set = list(zip(teams, total_chips))

data_frame = pd.DataFrame(data = data_set, columns = ['Teams', '# of Championships'])
data_frame.to_csv('NBA Titles.csv', index = True, header = True)
'''

#NumPy Objects---------------------------------------------------------------------------------------

#import numpy as np
'''
a1 = np.array([1,2,3,4])
print(a1)

a2 = np.array([[1,2,3],[3,4,5],[6,7,8]])
print(a2)

a3 = np.array([[[12,55,70,],[68,95,32]],[[32,46,38],[73,21,65]],[[92,58,53],[29,87,51]]])
print(a3)
'''

'''
Get this message if I have lists(arrays) with different lengths

C:\\Users\\Custom PC\\Dropbox\\My PC (DESKTOP-G0TP0QK)\\Desktop\test.py:1142: 
VisibleDeprecationWarning: Creating an ndarray from ragged nested sequences 
(which is a list-or-tuple of lists-or-tuples-or ndarrays with different lengths or shapes) 
is deprecated. If you meant to do this, 
you must specify 'dtype=object' when creating the ndarray.

Get this with different types of numbers(0.5, 2234, 4 etc.)

[[[1.230e+02 5.500e+01 7.000e+00]
  [6.800e+01 9.000e+00 3.256e+03]]

 [[6.400e-01 4.600e+01 3.840e+02]
  [7.300e+01 2.100e+01 6.500e+01]]

 [[9.200e+01 5.000e+00 5.200e+00]
  [2.900e+01 8.000e+00 5.134e+03]]]

*Also have to add a backslash for each part of a path to fully comment it out
'''

#a4 = np.arange(10, 50, 10)
'''
1st param - starting value
2nd param - ending value
3rd param - increment
'''
'''
print(a4)

a5 = np.arange(15)
print(a5)

a6 = np.arange(10, 20)
print(a6)

a7 = np.arange(0.3, 2, 0.2)
print(a7)

a8 = np.linspace(3, 8, 9)

#Instead of defined increment this is # of steps

print(a8)

o1 = np.ones((2,2,2))
print(o1)

o2 = np.zeros((2, 2, 2, 2))
print(o2)

e1 = np.empty((3,4))
print(e1)

e2 = np.eye(5)
#Makes a matrix with # of rows and columns of the number used. 1 also shows up diagonally
print(e2)

e3 = np.random.random((5,5))
#Matrix of random numbers from 0-1
print(e3)

#Useful NumPy Functions --------------------------------------------------------------------

print(a3.ndim)
print(a2.shape)
print(a3.size)
print(a6.dtype)
print(a7.dtype)
print(a3.itemsize) #memory size in bytes
print(a1.reshape(2,2)) #Change dimensions of array to 2x2
print(a1.reshape(1, -1)) #Take away or revert back to single dimension

try:
	print(a3.reshape(3, 6))
except(Exception) as e:
	print(e)

a3.resize(3,2,3)

#Slicing the array
print(a3[1:3])
print('---------------------------------')
print(a3[1:3, 0, 1:3])

c1 = np.arange(15)
b1 = c1 > 9

print(c1)
print('---------------------------------')
print(b1)

c1[b1] = 1 #Makes every value greater than 9 into 1
print(c1)

c2 = np.arange(25).reshape(5,5)
print(c2)
print(c2.min())
print(c2.max())
print(c2.sum())
print(c2.cumsum()) #add numbers in array
print(c2.max(axis=0)) #row
print(c2.max(axis=1)) #column
print(c2.cumsum(axis=0))

#Make shallow copy
c3 = c2

c3[0,0] = 16

print(c2) #changes first num in array to 16

#Can also use c3 = c2.copy()
'''

#Stack arrays on top of each other

'''
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])
print(np.vstack((v1, v2))) #vertical
print('--------------------------------')
print(np.hstack((v1, v2))) #horizontal
'''

#Basic NumPy Operations-----------------------------------------------------------------------

'''
x = np.linspace(0, 6.28, 20)
print(np.sin(x))
print(np.cos(x))
print(np.tan(x))

x1 = np.arange(9).reshape(3,3)
print(x1 ** 4)

print(np.exp(x1))
print(x1 * 4)
print(x1 / 4)
print(x1 + 4)
print(x1 - 4)

y = np.arange(10,19).reshape(3,3) #arange - range of numbers, reshape - dimension of matrix
print(y)

#Multiply Matrices

print(x1 * y)

a = np.array([[1,1],[2,2],[3,3]])

b = np.array([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]])
print(a.dot(b))
'''

'''
Think instructor said num of columns from 1st matrix
needs to = # of rows in 2nd
'''
#print(np.dot(a, b)) Another way

#Debugging - pdb Module ---------------------------------------------------------------------

#import pdb

'''
Followed along using GitBash
-Saved debug function to desktop
-changed directory in GB to desktop
-Entered code '-m pdb test.py'
'''

#Debug in Sublime Text
'''
print('Statement 1')

for i in range(5):
	print('Statement ' + str(i + 2))

pdb.set_trace()
print('Statement 7')

#Another way
pdb.run('pdb_test.Test(2,5)')
'''

'''
Had gotten PDB to come up in GitBash but wouldn't 
run debug. Now I can't get pdb to come back up
Of course still able to follow along 
with console commmands in REPL console
'''

#Call debugger after execution of program has stopped

#pdb.pm()

#Commands for Debugging -------------------------------------------------------------------

import pdb

#where or w
#list
'''
print('Statement 1')

for i in range(5):
	print('Statement ' + str(i + 2))

pdb.set_trace()
print('Statement 7')

Console Output ---------------------------------------------------------------------------

> c:\\users\\custom pc\\dropbox\\my pc (desktop-g0tp0qk)\\desktop\test.py(1358)<module>()
-> print('Statement 7')
(Pdb) w
> c:\\users\\custom pc\\dropbox\\my pc (desktop-g0tp0qk)\\desktop\test.py(1358)<module>()
-> print('Statement 7')
(Pdb) list
1353 	
1354 	for i in range(5):
1355 		print('Statement ' + str(i + 2))
1356 	
1357 	pdb.set_trace()
1358 ->	print('Statement 7')
1359 	
1360 	
1361
1362 	(Pdb) w - where
1363 	(Pdb) list
(Pdb) list 1354, 1355
1354 	for i in range(5):
1355 		print('Statement ' + str(i + 2))
(Pdb) 
'''

'''
(Pdb) w - where
(Pdb) list
(Pdb) list 1352, 1353
'''

'''
def fun1(a):
	if a % 2:
		return True
	else:
		return False

def fun2(x):
	if type(x) is int:
		pdb.set_trace()
		print(fun1(x))
	else:
		print('Not defined')

fun2(3)
'''

'''
Console Output
> c:\\users\\custom pc\\dropbox\\my pc (desktop-g0tp0qk)\\desktop\test.py(1376)fun2()
-> print(fun1(x))
(Pdb) up
> c:\\users\\custom pc\\dropbox\\my pc (desktop-g0tp0qk)\\desktop\test.py(1380)<module>()
-> fun2(3)
(Pdb) down
> c:\\users\\custom pc\\dropbox\\my pc (desktop-g0tp0qk)\\desktop\test.py(1376)fun2()
-> print(fun1(x))
(Pdb) args
x = 3
(Pdb) !x = 4
(Pdb) args
x = 4
(Pdb) step
--Call--
> c:\\users\\custom pc\\dropbox\\my pc (desktop-g0tp0qk)\\desktop\test.py(1367)fun1()
-> def fun1(a):
(Pdb) next
> c:\\users\\custom pc\\dropbox\\my pc (desktop-g0tp0qk)\\desktop\test.py(1368)fun1()
-> if a % 2:

(Pdb) until 

-Continues until execution reaches a line in code higher than current value, used to skip loops

> c:\\users\\custom pc\\dropbox\\my pc (desktop-g0tp0qk)\\desktop\test.py(1371)fun1()
-> return False

(Pdb) return #Continues execution until it runs into return statement
--Return-- 
> c:\\users\\custom pc\\dropbox\\my pc (desktop-g0tp0qk)\\desktop\test.py(1371)fun1()->False
-> return False
(Pdb) return
False
--Return--
> c:\\users\\custom pc\\dropbox\\my pc (desktop-g0tp0qk)\\desktop\test.py(1376)fun2()->None
-> print(fun1(x))
(Pdb) 
'''

#Commands for Debugging Part II -------------------------------------------------------------
'''
def IsPrime(n):
	for x in range(2, n // 2 + 1):
		if not n % x:
			pdb.set_trace()
			return False;
	return True;

def PrimesTo(n):
	for x in range(2, n):
		if IsPrime(x):
			pdb.set_trace()
			print(x)
'''
#IsPrime(50)
#PrimesTo(50)

'''
Console Output -------------------------------------------------------------------------------

> c:\\users\\custom pc\\dropbox\\my pc (desktop-g0tp0qk)\\desktop\test.py(1456)IsPrime()
-> return False;
(Pdb) up
> c:\\users\\custom pc\\dropbox\\my pc (desktop-g0tp0qk)\\desktop\test.py(1465)<module>()
-> IsPrime(50)
(Pdb) break IsPrime
Breakpoint 1 at c:\\users\\custom pc\\dropbox\\my pc (desktop-g0tp0qk)\\desktop\test.py:1452
(Pdb) disable 1
Disabled breakpoint 1 at c:\\users\\custom pc\\dropbox\\my pc (desktop-g0tp0qk)\\desktop\test.py:1452
(Pdb) enable 1
Enabled breakpoint 1 at c:\\users\\custom pc\\dropbox\\my pc (desktop-g0tp0qk)\\desktop\test.py:1452
(Pdb) l
1460 		for x in range(2, n):
1461 			if IsPrime(x):
1462 				pdb.set_trace()
1463 				print(x)
1464 	
1465 ->	IsPrime(50)
1466 	#PrimesTo(50)
1467 	
[EOF]
(Pdb) tbreak 1460
Breakpoint 2 at c:\\users\\custom pc\\dropbox\\my pc (desktop-g0tp0qk)\\desktop\test.py:1460
(Pdb) list break
*** Error in argument: 'break'
(Pdb) break 1460, n > 1463
Breakpoint 3 at c:\\users\\custom pc\\dropbox\\my pc (desktop-g0tp0qk)\\desktop\test.py:1460
(Pdb) break
Num Type         Disp Enb   Where
1   breakpoint   keep yes   at c:\\users\\custom pc\\dropbox\\my pc (desktop-g0tp0qk)\\desktop\test.py:1452
2   breakpoint   del  yes   at c:\\users\\custom pc\\dropbox\\my pc (desktop-g0tp0qk)\\desktop\test.py:1460
3   breakpoint   keep yes   at c:\\users\\custom pc\\dropbox\\my pc (desktop-g0tp0qk)\\desktop\test.py:1460
	stop only if n > 1463
(Pdb) clear 3
Deleted breakpoint 3 at c:\\users\\custom pc\\dropbox\\my pc (desktop-g0tp0qk)\\desktop\test.py:1460
(Pdb) ignore 2 2
Will ignore next 2 crossings of breakpoint 2.
(Pdb) commands 2
(com) print('n = ' + str(n))
(com) end
(Pdb) jump 1461
*** You can only jump within the bottom frame
(Pdb) jump
'''

#Regular Expressions ----------------------------------------------------------------------

import re

'''
match = re.search('pattern', 'Searching pattern in text')

print(match)
print(match.re.pattern)
print(match.string)
print(match.start())
print(match.end())

regex = re.compile('pattern')
print(regex.search('Searching pattern in text...').start())
print(regex.findall('Searching pattern in text pattern'))
print(re.match('Match', 'Match function test'))
print(re.match('test', 'Match function test.'))
'''

#Patterns -------------------------------------------------------------------------------------

# * + ? {} 
'''
def all_matches(text, pattern):
	print(pattern)
	regobj = re.compile(pattern)
	for m in regobj.finditer(text):
		print(str(m.start()) + '-' + str(m.end()) + ':' + text[m.start() : m.end()])

#This is considered 'greedy parsing'
all_matches('xyyxxxxxyyyyxxxxyy', 'xy*')

all_matches('xyyxxxxxyyyyxxxxyy', 'xy+') #returns samples w/ x and one or more y's

all_matches('xyyxxxxxyyyyxxxxyy', 'xy?') #returns samples w/ x followed by 0 or 1 y

all_matches('xyyxxxxxyyyyxxxxyy', 'xy{2}') #returns samples w/ x followed by the number of chars in the curly brackets

all_matches('xyyxxxxxyyyyxxxxyy', 'xy{3,4}') #returns samples w/ x followed by at least 3, no more than 4

all_matches('xyyxxxxxyyyyxxxxyy', 'xy{2,')

#The following considered is considered 'non-greedy parsing'

all_matches('xyyxxxxxyyyyxxxxyy', 'xy*?')

all_matches('xyyxxxxxyyyyxxxxyy', 'xy+?')

all_matches('xyyxxxxxyyyyxxxxyy', 'xy??')

#One number in the curly bracket will return all terms that have a repeat of that number

all_matches('xyyxxxxxyyyyxxxxyy', 'xy{3,}?')

all_matches('xyyxxxxxyyyyxxxxyy', 'x[xy]+') #Return x or y

all_matches('xx..  ..yyxxx..  ', '[^. ]+') #Returns samples w/o space or '.'

all_matches('A94B2c4 xyz08', '[A-Z][0-9]') #Returns instances of upper case followed by digits

all_matches('A94B2c4 xyz08', '[A-Za-z][0-9]') #returns upper & lower followed by digits

all_matches('Silk Road', 'S.+k') #returns characters starting with 'S' and ending with 'k'
'''

'''
KEEP IN MIND IT'S SUPPOSED TO BE ONE BACKSLASH!!!
JUST USING TWO FOR COMMENTING OUT
\\d - finds digits
\\D - anything except digits
\\s - wide spaces, tabs
\\S - anything except spaces, tabs
\\w - alphanumeric chars
\\W - anything but alphanumeric chars
'''
'''
all_matches('This is 1st example', r'\\d+')

all_matches('This is 1st example', r'\\D+')

all_matches('This is 1st example', r'\\s+')

all_matches('This is 1st example', r'\\S+')

all_matches('This is 1st example', r'\\w+')

all_matches('This is 1st example', r'\\W+')

all_matches('Relative positioning in regular expression', r'^\\w+') #returns word at start of string. Can also use r'\A\w+'

all_matches('Relative positioning in regular expression', r'\\w+$') #last word in string, same as r'\w\Z'

all_matches('Relative positioning in regular expression', r'\br|w+')#r'\b(n)|w+' will return whatever's in place of n at start of a word

all_matches('Relative positioning in regular expression', r'\bp|w+')

all_matches('Relative positioning in regular expression', r'\\Bg\\B') #r'\\B(n)\\B returns whatever replaces n within middle of a word'
'''

#Division & Grouping Results ----------------------------------------------------------------

#regex = re.compile('x([xy]+)(y)')
#match = regex.search('xyxxxyxxxyxyxy')
'''
print(match.group())
print(match.group(0))
print(match.group(1))
print(match.group(2))
'''
'''
regex = re.compile('x(?P<first>[xy]+)(?P<second>y)')

match = regex.search('xyxxxyxxxyxyxy')

print(match.groups())
print(match.group('first'))
print(match.group('second'))
print(match.groupdict())
'''
'''
regex = re.compile('y((x|y)+)')

match = regex.search('yxxyyxyxy')

print(match.group(1))
print(match.group(2))
'''

#Setting Search Parameters --------------------------------------------------------------------
'''
print(re.findall('x*y', 'XXXYYYXXXY'), re.IGNORECASE)

print(re.findall('(^xy{2}) | (yx{2}$)', 'xyxyxxxyxx\nxyyxxxxx'), re.MULTILINE)

print(re.findall('z.x' , 'xyyyyz\nxyyxx'), re.DOTALL)
'''
'''
regex = re.compile('''
                            #This is comment
     #   \w+                #aplhanumeric
   # @               #at
    #\w+             #alphanumeric
    #.               #dot
    #(com|net|org)   #com or org or net
	''', re.VERBOSE)

print(regex.search('johndoe@email.com').start())
re._compile('pattern', re.IGNORECASE | re.VERBOSE | re.DOTALL)
'''
'''
Instead of this at the beginning of the pattern you can use:
(?i) - ignore case
(?u) - unicode
(?x) - verbose
(?m) - multiline
'''
'''
print(re.findall('(?i)x*y', 'XXXYYYXYXYxyyxxy',))

print(re.findall('(?u)x*y', 'XXXYYYXYXYxyyxxy',))

print(re.findall('(?uxi)x*y', 'XXXYYYXYXYxyyxxy',))
'''
