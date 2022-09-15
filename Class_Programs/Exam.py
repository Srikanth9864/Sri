
from collections import defaultdict,Counter
from re import findall,finditer
from itertools import chain

# 40. Program to print only the repeated characters and count of the same
sentence = "hello world welcome to python programming hi there"
d=defaultdict(int)
words=sentence.split()
for word in words:
    for char in word:
        if sentence.count(char) > 1:
            d[char] +=1
print(d)

# 39 Program to print the number of occurrences of characters in a String without using inbuilt functions.
names = ['apple', 'google', 'apple', 'yahoo', 'google', 'facebook', 'gmail', 'yahoo']
names_count = { }
for name in names:
    for char in name: 
        if char not in names_count:
            names_count[char] = 1
        else:
            names_count[char] += 1
print(names_count)

# 38 Print all the numbers in the below list**
a = ['abc', '123', 'hello', '23']
b = [ ]
for item in a:
    if item.isdigit :
        print(item)
# 37 Write a program to sum all the numbers in below string.**
s = "Sony12India567Pvt2ltd" # eg.12+567+2
from re import findall
result=findall(r"[0-9]+","Sony12India567Pvt2ltd")
print("+".join(result))

# 36 Sum all the numbers in the below string.**
s = "Sony12India567Pvt2ltd"
from re import findall
c = [ ]
result=findall(r"[0-9]+","Sony12India567Pvt2ltd")
for value in result:
    c.append(int(value))
print(sum(c))

# 35 Write a function to print the below output.**
# o/p=func("TRACXN", 0)  # Should print RCN
# o/p=func("TRACXN", 1)  # Should print TAX
def func(string,value):
    if value==0:
        print(string[1::2])
    elif value==1:
        print(string[::2])

# 34 Write a function to reverse any iterable without using reverse function
def reverse(string):
    str_ = " "
    for char in string:
        str_ = char + str_
    return str_
f= reverse("Python")
print(f)

# 33 Count the number of occurrences of "CRITICAL", "INFO" and "ERROR" lines in a log file.**
with open(r"K:/Python Notes/Java.log") as file:
    d = defaultdict(int)
    for line in file:
        line = line.split()
        if line[0] not in ("CRITICAL","INFO","ERROR") :
            d[line[0]] += 1
print(d)

# 32 A function takes variable number of positional arguments as input. How to check if the arguments that are passed are more than 5*
def func(*args,**kwargs):
    if len(args) + len(kwargs) > 5:
        return True
    else:
        return False
f = func(1,2,3,4)
print(f)
# 31 How to get the elements that are in list b but not in list a**
a = [1, 2, 3] 
b = [1, 2, 3, 4, 5]
print(set(b) - set(a))
for item in b:
    if item not in a:
        print(item)

# 30 write a program to get 1234
t = ('1', '2', '3', '4')
print("".join(t))
st = ""
for item in t:
    st = st + item
print(st)

# 29 write a program to reverse the values in the dictionary if the value is of type String**
d = {'a': 'hello', 'b': 100, 'c': 10.1, 'd': 'world'}
for key,value in d.items():
    if isinstance(value,str):
        print(value[::-1])
    else:
        print(key,value)

for item in d.items():
    if isinstance(item[1],str):
        d[item[0]]=(item[1][::-1])
print(d)

# 28 Find the longest word in the sentence**
sentence = "Python is  also an interpreted Language"
longest = ""
k1 = [ ]
for word in sentence.split():
    if len(word) > len(longest) :
        k1.append(word)
print(sorted(k1,key = lambda item: len(item))[-1])     

# 27 How to remove duplicates from the list without using inbuilt functions**
items = [1, 2, 3, 4, 1, 2, 3, 4, 5]
item_ = [ ]
for item in items:
    if item not in item_:
        item_.append(item)
print(item_)
#Using Default Dictionary
d=defaultdict(int)
for item in items:
    if item not in d:
        d[item] += 1
print(list(d))

# 26 What is the output of the following**
a = [1, 2, 3]
b = [4, 5, 6]
print([a, b])
print((a, b))
print(*a,*b)
# 25 Write a lambda function to add two numbers (a, b)**
_Add = lambda a,b : a+b
print(_Add(3,3))

# 24 Write a python program to get the below output**
sentence = "Hi How are you" 
# o/p should be "ouy era woH iH"
st = " "
for word in sentence.split() :
    for char in word:
        st = char + st
print(st,end = " ")
print()
print(sentence[::-1])

# 23 Write a python program to get the below output**
sentence = "Hi How are you" 
# o/p should be "iH woH era uoy"
for word in sentence.split():
    print(word[::-1],end = " ")
print()

# 22 Write a Custom class which can access the values of dictionaries using d['a'] and d.a**
class Point:
    def __init__(self,d):
       self.d = d
    def __getitem__(self,key):
       return self.d[key]
    def __getattr__(self,key) :
       return self.d[key]

p = Point({'a' : 1 , 'b': 2 })
# print(p.a)
# print(p['b'])
class Demo:
    def __init__(self,d) :
        self.__dict__.update(d)
    def __getitem__(self,key) :
        return self.__dict__[key]
d=Demo({'a' : 3 , 'b': 4 })
print(d.__dict__)
print(d['a'])
print(d.a)
# 21 Write a class named Simple and it should have iteration capability.*
class Simple:
    def __init__(self,iterable) : 
        self.iterable = iterable
    def __iter__(self) :
        return iter(self.iterable)

s = Simple("Python")
for char in s:
    print(char,end="")
print()
s1 = Simple([1,2,3,4,5])
for inti in s1:
    print(inti,end="")
print()

# 20 Write a function which takes a list of strings and integers.If the item is a string it should print as is and if the item is integer or float it should reverse it.
list_ = ["Hello",125,"hi",36,"how"]
def func(list_):
    for item in list_:
        if isinstance(item,(int,float)):
            item = str(item)
            print(item[::-1],end =" ")
        elif isinstance(item,str):
            print(item,end =" ")
        print()
func(list_)

# 19 How to get the count of the number of instances of a class that is being created.**
class Demo:
    count = 0
    def __init__(self) :
       Demo.count += 1
Demo()
Demo()
Demo()
Demo()
print(Demo.count)

# 18 write a decorator that returns only positive values of subtraction**
def positive(func):
    def wrapper(*args,**kwargs):
        result=func(*args,*kwargs)
        if result < 0:
           return result * -1
    return wrapper
@positive
def substraction(a,b):
    return a-b
s=substraction(2,3)
# print(s)
@positive
def add(a,b) :
    return a+b
_ad = add(3,-5)
print(_ad)

# 17 Write a to replace all the characters with - if the character occurs more than once in a string*
_string = 'hellohai' # O/P should be '-e--o-ai'
res = " "
for char in _string:
    if _string.count(char) > 1:
        res = res + "-"
    else:
        res = res + char
print(res)    

# 16 Write a program to get the below output
sentence1 = "hello world welcome to python programming hi there"
# d = {'h': ['hello', 'hi'], 'w': ['world', 'welcome'], 't': ['to', 'there'], 'p': ['python', 'programming'] }
d1 = {}
for word in sentence1.split():
    if word[0] not in d1:
        d1[word[0]] = [word]
    else:
        d1[word[0]].append(word)
print(d1)

# 15 Write a program to search for a character in a given string and return the corresponding index.
sentence = "hello world welcome to python programming hi there"
def character(value):
        for index,char in enumerate(sentence):
            if char == value:
                print(index,value)
                
c=character("e")
