class Greeting:
    def __init__(self, name="world"):
        self.name = name
    
    def __call__(self):
        print("Calling __call__")
        print(self.name)

class Greeting:
    def __call__(self, name):
        print(f"Hello {name}")

class Squares:
    def __init__(self, numbers):
        self.numbers = numbers

    def __call__(self):
        squares = []
        for number in self.numbers:
            squares.append(number ** 2)
        return squares

class Squares:
    def __call__(self, numbers):
        squares = []
        for number in numbers:
            squares.append(number ** 2)
        return squares

# Function Version
def log(func):
    def wrapper(*args, **kwargs):
        print(f"You are calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

# Class Version
class Log:
    def __init__(self, func):
        self.func = func
    
    def __call__(self, *args, **kwargs):
        print(f"You are calling {self.func.__name__}")
        return self.func(*args, **kwargs)

from time import time, sleep
def _time(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        result =  func(*args, **kwargs)
        end_time = time()
        print(f"Execution time: {end_time - start_time}")
        # Return the result of original function
        return result
    return wrapper

class Time:
    def __init__(self, func):
        self.func = func

    # Equivalent to "wrapper" function
    def __call__(self, *args, **kwargs):
        start_time = time()
        result = self.func(*args, **kwargs)
        end_time = time()
        print(f"Execution time: {end_time - start_time}")
        return result

@Time
def add(a, b):
    sleep(2)
    return a + b


items = ['bv', 'aw', 'dt', 'cu']

def get_last_char(item):
    return item[-1]

class GetLastChar:
    def __call__(self, item):
        print(f"Calling __call__ {item}")
        return item[-1]

g = GetLastChar()

by = sorted(items, key=get_last_char)
by_ = sorted(items, key=lambda item: item[-1])
_by = sorted(items, key=g)  # g('bv'), g('aw'), g('dt')

# s = Simple(10)
# s.a, s['a'] s[0]
# Attribute Access as well as Subscripting
class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __getitem__(self, index):
        return self.__dict__[index]
    
    def __setitem__(self, item, value):
        self.__dict__[item] = value