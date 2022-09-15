def func():
    return a + 1

def func():
    # "b" is local
    b = 200
    return a + b

def func():
    a = 100
    b = 200
    return a + b

# global variables
a = 10
b = 20

def func():
    # "a" and "b" are local variables
    # trying to get the local value of "a", add 1 to the local value of "a" and re-assign 
    # back to local "a"
    a = a + 1
    b = b + 1
    return a + b

def func():
    # "a" and "b" are local varaiables
    result = a + b
    a = 100
    b = 200
    result = a + b
    return result

# LEGB rule
def func():
    # "a" is enclosing scope for wrapper func and local scope for "func"
    # a = 20
    def wrapper():
        return a + 1
    return wrapper

def func():
    a = 100
    def wrapper():
        result= a + 1
        a = 1.5
        return result
    return wrapper

def func():
    a = a + 1
    a = 10
    def wrapper():
        return a + 1
    return wrapper

a = 100
def func():
    a = 1000
    print(a)

print(a)
func()
print(a)


a = 100
def func():
    global a
    # a = 1000
    a = a + 1
    print(a)

print(a)
func()
print(a)

# len is global
len = "hello global"

def func():
    # len is local for func and enclosing for wrapper
    # len = "hello func"
    def wrapper():
        # len is local for wrapper
        # len = "hello wrapper"
        print(len)
    print(len)
    return wrapper

number = -5

# numbers = [ number  for number in [1, 2, 3, 4] ]

for number in [1, 2, 3, 4]: # number = 1, 2, 3, 4
    print(number)

x = 10

# at the time of function defnition, the value of "x" is 10  which is assigned to some_number
def spam(some_number=x):
    result = some_number + 1
    return result

# we are changing the value of "x" but that does not affect some_number. some_number will always
# be 10 ONLY (the value at the time of function defnition)
x = 100