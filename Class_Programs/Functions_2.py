from time import sleep
# Decorator is a callable or func which adds some extra functionality to the existing function
# without modifying the existing or original function

def log(func):
    # adding something extra to the original function or functionality or to the callback func
    def wrapper(*args, **kwargs):
        print(f"You are calling {func.__name__}")
        result = func(*args, **kwargs) # execting the callback function
        return result
    return wrapper

@log        # spam = log(spam)
def spam():
    return "hello world"

@log    # greet = log(greet)
def greet(name):
    return f"hello {name}"

@log    # add = log(add)
def add(a, b):
    return a+b

@log        # sub = log(sub)
def sub(a, b, c):
    return a - b - c

@log    # mul = log(mul)
def mul(a, b, c, d):
    return a * b * c * d
