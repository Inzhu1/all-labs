#1
print(10 > 9)
print(10 == 9)
print(10 < 9)
#2
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
#3
print(bool("Hello"))
print(bool(15))
#4
x = "Hello"
y = 15
print(bool(x))
print(bool(y))
#5
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
#6
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
#7
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))
#8
def myFunction() :
  return True

print(myFunction())
#9
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")
#10
print(10 + 5)
#11
print((6 + 3) - (6 + 3))
#12
print(100 + 5 * 3)
#13
print(5 + 4 - 7 + 3)
#14
mylist = ["apple", "banana", "cherry"]
#15
thislist = ["apple", "banana", "cherry"]
print(thislist)
#16
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
#17
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
#18
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
#19
list1 = ["abc", 34, True, 40, "male"]
#20
<class 'list'>
#21
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
#22
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
#23
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
#24
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
#25
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
#26
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
#27
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
#28
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
#29
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
#30
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
#31
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
#32
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
#33
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
#34
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
#35
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
#36
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
#37
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
#38
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
#39
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
#40
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)
#41
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
#42
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
#43
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
#44
thislist = ["apple", "banana", "cherry"]
del thislist
#45
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
#46
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
#47
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
#48
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
#49
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
#50
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)
#51
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
#52
newlist = [expression for item in iterable if condition == True]
#53
newlist = [x for x in fruits if x != "apple"]
#54
newlist = [x for x in fruits]
#55
newlist = [x for x in range(10)]
#56
newlist = [x for x in range(10) if x < 5]
#57
newlist = [x.upper() for x in fruits]
#58
newlist = ['hello' for x in fruits]
#59
newlist = [x if x != "banana" else "orange" for x in fruits]
#60
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
#61
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
#62
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
#63
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)
#64
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
#65
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
#66
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
#67
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
#68
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
#69
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
#70
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)
#71
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)
#72
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)
#73
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
#74
thistuple = ("apple", "banana", "cherry")
print(thistuple)
#75
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
#76
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
#77
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))
#78
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
#79
tuple1 = ("abc", 34, True, 40, "male")
#80
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))
#81
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
#82
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
#83
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])
#84
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
#85
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])
#86
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])
#87
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])
#88
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
#89
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
#90
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
#91
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)
#92
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
#93
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists
#94
fruits = ("apple", "banana", "cherry")
#95
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
#96
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
#97
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)
#98
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
#99
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
#100
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
#101
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
#102
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)
#103
thisset = {"apple", "banana", "cherry"}
print(thisset)
#104
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)
#105
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)
#106
thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)
#107
thisset = {"apple", "banana", "cherry"}

print(len(thisset))
#108
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
#109
set1 = {"abc", 34, True, 40, "male"}\
#110
myset = {"apple", "banana", "cherry"}
print(type(myset))
#111
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
#112
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
#113
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)
#114
thisset = {"apple", "banana", "cherry"}

print("banana" not in thisset)
#115
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)
#116
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)
#117
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)
#118
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)
#119
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)
#120
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)
#121
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)
#122
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)
#123
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
#124
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
#125
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)
#126
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)
#127
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset)
#128
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)
#129
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)
#130
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)
#131
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)
#132
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print(set1)
#133
set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)

print(set3)
#134
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)
#135
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3)
#136
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print(set1)
#137
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)
#138
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3)
#139
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1)
#140
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
#141
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
#142
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
#143
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
#144
print(len(thisdict))
#145
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
#147
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))
#148
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
#149
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
#150
x = thisdict.get("model")
#151
x = thisdict.keys()
#152
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change
#153
x = thisdict.values()
#154
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change
#155
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["color"] = "red"

print(x) #after the change
#156
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["year"] = 2020

print(x) #after the change
#157
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["color"] = "red"

print(x) #after the change
#158
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
#159
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
#160
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
#161
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)
#162
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})
#163
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)
#164
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)
#165
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)
#166
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)
#167
for x in thisdict:
  print(x)
#168
for x in thisdict:
  print(thisdict[x])
#169
for x in thisdict.values():
  print(x)
#170
for x in thisdict.keys():
  print(x)
#171
for x, y in thisdict.items():
  print(x, y)
#172
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)
#173
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)
#174
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
#175
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
#176
print(myfamily["child2"]["name"])
#177
for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])
#178
a = 33
b = 200
if b > a:
  print("b is greater than a")
#179
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
#180
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
#181
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
#182
if a > b: print("a is greater than b")
#183
a = 2
b = 330
print("A") if a > b else print("B")
#184
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
#185
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
#186
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
#187
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")
#188
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
#189
a = 33
b = 200

if b > a:
  pass
#190
i = 1
while i < 6:
  print(i)
  i +=1
#191
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
#192
i = 0
while i < 6:
  i += 1 
  if i == 3:
    continue
  print(i)
#193
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
#194
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
#195
for x in "banana":
  print(x)
#196
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 
  if x == "banana":
    break
#197
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
#198
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
#198
for x in range(6):
  print(x)
#199
for x in range(2, 6):
  print(x)
#200
for x in range(2, 30, 3):
  print(x)
#201
for x in range(6):
  print(x)
else:
  print("Finally finished!")
#202
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
#203
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
#204
for x in [0, 1, 2]:
  pass
  






  
