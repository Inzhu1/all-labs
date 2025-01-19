#1
print("Hello, World!")
#2
import sys
print(sys.version)
#3
if 5 > 2:
  print("Five is greater than two!")
#4
if 5 > 2:
 print("Five is greater than two!")  
if 5 > 2:
        print("Five is greater than two!") 
#5
x = 5
y = "Hello, World!"
print(x)
print(y)
#6
#This is a comment.
print("Hello, World!")
#7
print("Hello, World!") #This is a comment.
#8
#print("Hello, World!")
print("Cheers, Mate!")
#9
#This is a comment
#written in
#more than just one line
print("Hello, World!") 
#9
"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")
#10
x = 5
y = "John"
print(x)
print(y)
#11
x = 4
x = "Sally"
print(x)
#12
x = str(3)
y = int(3)
z = float(3)
print(x)
print(y)
print(z)
#13
x = 5
y = "John"
print(type(x))
print(type(y))
#14
x = "John"
print(x)
#double quotes are the same as single quotes:
x = 'John'
print(x)
#15
a = 4
A = "Sally"
print(a)
print(A)
#16
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)
#17
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
#18
x = y = z = "Orange"
print(x)
print(y)
print(z)
#19
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
#20
x = "Python is awesome"
print(x)
#21
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
#22
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
#23
x = 5
y = 10
print(x + y)
#24
x = 5
y = "John"
print(x, y)
#25
x = "awesome"
def myfunc():
  print("Python is " + x)
myfunc()
#26
x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)
myfunc()
print("Python is " + x)
#27
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)
#28
x = "awesome"
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)
#29
x = 5
print(type(x)) 
#30
x = 1
y = 2.8
z = 1j
print(type(x))
print(type(y))
print(type(z))
#31
x = 1
y = 35656222554887711
z = -3255522
print(type(x))
print(type(y))
print(type(z))
#32
x = 1.10
y = 1.0
z = -35.59
print(type(x))
print(type(y))
print(type(z))
#33
x = 35e3
y = 12E4
z = -87.7e100
print(type(x))
print(type(y))
print(type(z))
#34
x = 3+5j
y = 5j
z = -5j
print(type(x))
print(type(y))
print(type(z))
#35
#convert from int to float:
x = float(1)
#convert from float to int:
y = int(2.8)
#convert from int to complex:
z = complex(1)
print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))
#36
import random
print(random.randrange(1, 10))
#37
x = int(1)
y = int(2.8)
z = int("3")
print(x)
print(y)
print(z)
#38
x = float(1)
y = float(2.8)
z = float("3")
w = float("4.2")
print(x)
print(y)
print(z)
print(w)
#39
x = str("s1")
y = str(2)
z = str(3.0)
print(x)
print(y)
print(z)
#40
#You can use double or single quotes:
print("Hello")
print('Hello')
#41
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')
#42
a = "Hello"
print(a)
#43
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
#44
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
#45
a = "Hello, World!"
print(a[1])
#46
for x in "banana":
  print(x) 
#47
a = "Hello, World!"
print(len(a))
#48
txt = "The best things in life are free!"
print("free" in txt)
#49
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
#50
txt = "The best things in life are free!"
print("expensive" not in txt)
#51
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
#52
b = "Hello, World!"
print(b[2:5])
#53
b = "Hello, World!"
print(b[:5])
#54
b = "Hello, World!"
print(b[2:])
#55
b = "Hello, World!"
print(b[-5:-2])
#56
a = "Hello, World!"
print(a.upper())
#57
a = "Hello, World!"
print(a.lower())
#58
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
#59
a = "Hello, World!"
print(a.replace("H", "J"))
#60
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
#61
a = "Hello"
b = "World"
c = a + b
print(c)
#62
a = "Hello"
b = "World"
c = a + " " + b
print(c)
#63
age = 36
txt = f"My name is John, I am {age}"
print(txt)
#64
price = 59 
txt = f"The price is {price:.2f} dollars" 
print(txt)
#65
txt = f"The price is {20 * 59} dollars" 
print(txt)
#66
txt = "We are the so-called \"Vikings\" from the north."
