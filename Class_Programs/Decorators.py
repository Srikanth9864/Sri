from time import sleep, time

# Decorator is a callable or func which adds some extra functionality to the existing function
# without modifying the existing or original function

def log(func):
    # adding something extra to the original function or functionality or to the callback func
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} function")
        result = func(*args, **kwargs) # executing the callback function
        return result
    return wrapper

def exe_time(func):
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f"Execution time: {end-start} seconds")
        return result
    return wrapper

def delay(func):
    def wrapper(*args, **kwargs):
        sleep(1)        # extra functionality
        result = func(*args, **kwargs)
        return result
    return wrapper

def reverse(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str):
            return result[::-1]
        else:
            return result
    return wrapper

def positive(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result < 0:
            return result * -1
        return result
    return wrapper

def positive(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return abs(result)
    return wrapper

_cache = { }

def cache(func):
    def wrapper(*args, **kwargs):
        if args in _cache:      # if (1, 2) is present in dict as a key args = (1, 2)
            return _cache[args]
        else:
            result = func(*args, **kwargs)
            # register that argument pair in dictionary
            _cache[args] = result       # _cache[(1, 2)] = 3
            return result
    return wrapper

# count = {'add': 10, 'sub': 3, 'mul': 2, 'greet': 1}
count = { }
def func_count(func):
    def wrapper(*args, **kwargs):
        function_name = func.__name__
        if function_name in count:
           count[function_name]  += 1
        else:
            count[function_name] = 1
        result = func(*args, **kwargs)
        return result
    return wrapper

count = { }
def max_count(func):
    def wrapper(*args, **kwargs):
        function_name = func.__name__
        if function_name in count:
           count[function_name]  += 1
        else:
            count[function_name] = 1
        if count[function_name] > 5:
            raise Exception("Max function call limit exceeded 5 times!!!")
        result = func(*args, **kwargs)
        return result
    return wrapper

def prefix_91(func):
    def wrapper(*args, **kwargs):
        # get that list out of the tuple
        temp = args[0]
        # check if each item of the list if prefixed with +91 or not
        # call the orginal func print_numbers and pass the updated list
        # new tuple with +91 prefixed
        args = (temp, )
        result = func(*args, **kwargs)      # args = ([12345, 343,45435], )
        return result
    return wrapper

@prefix_91
def print_numbers(numbers):
    for number in numbers:
        print(number)

@max_count
def add(a, b):
    return a+b

@max_count
def sub(a, b):
    return a-b

@reverse
def greet():
    return "hello world"
