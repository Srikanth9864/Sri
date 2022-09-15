def greeting():
     print("hello world")
     print('hello there')
     print("hello spam")

def greet():
    return "hello world"

def _greet(name):
    """ This function greets the user """
    return f"hello {name}"

def add(a, b):
    return a + b

def greeting(name, age, pay):
    print(f"hello {name} you are {age} years of age and you get ${pay}")

# name, age and pay are optional arguments
def greeting(name="sandeep", age=26, pay=1000):
    print(f"hello {name} you are {age} years of age and you get ${pay}")


def greet(name, debug=False):
    if debug:   # debug == True
        print("You called greet function")
    return f"hello {name}"

def greet(name, /,*, reverse=False, debug=False):
    if debug:
        print("You called greet function ")
    if reverse:
        return f"hello {name[::-1]}"
    return f"hello {name}"


def greeting(*, name, age, pay):
    print(f"hello {name} you are {age} years of age and you get ${pay}")


def greeting(name, /, *, age, pay):
    print(f"hello {name} you are {age} years of age and you get ${pay}")

# add func can take any number of positional arguments from 0 to n
# * represents any number of positional arguments
# all the values will get collected inside a tuple
# * denotes variable number of positional arguments
def add(*args):
    total = 0
    for item in args:
        total = total + item
    return total

def greet(*names):
    for name in names:
        print(f"Hello {name}")


def spam(*args, **kwargs):
    print(args)
    print(kwargs)

def greet(name, **info):
    print(f" Hello {name}")
    print(info)
    # for key, value in info.items():
    #     print(key, value)

def demo(**info):
    print(info)

def func(a, *args):
    print(a)
    print(args)

# Incorrect syntax
def func(*args, a):
    print(a)
    print(args)

def greeting(name, age, pay):
    print(f"hello {name} you are {age} years of age and you get ${pay}")

data = ("sandeep", 26, 1000)

# indexing
greeting(data[0], data[1], data[2])     # greeting("sandeep", 26, 1000)

# unpacking
_name, _age, _pay = data
greeting(_name, _age, _pay)

# pythonic approach
greeting(*data)     # unpacking greeting("sandeep", 26, 1000)

d = {"name": "sandeep", "age": 26, "pay": 1000}
greeting(d['name'], d['age'], d['pay'])
greeting(**d)       # greeting(name="sandeep", age=26, pay=1000)
# greeting(fname="sandeep", age=26, pay=1000)
