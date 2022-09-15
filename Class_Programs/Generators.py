# Regular Function
def func():
    print("Entered Function")
    return 1
    return 2
    return 3

# Generator Function
def func():
    print("Generator Started...")
    yield 1 # Execution pauses
    print("Executing after first yiled statement")
    yield 2 # Execution pauses
    print("Executing after second yield statement")
    yield 3
    print("Executing after third yield statement")

# Regular function
def evens(some_list):
    e = [ ]
    # completely iterating over the list and building a new list
    for number in some_list:
        if number % 2 == 0:
            e.append(number)
    return e

# Generator Function
def g_evens(some_list):
    for number in some_list:
        if number % 2 == 0:
            yield number

# Regualr function
def evens():
    e = [ ]
    i = 0
    while True:
        if i % 2 == 0:
            e.append(i)
        i = i + 1
    return e

# Generator Function
def g_evens():
    i = 0
    while True:
        if i % 2 == 0:
            yield i 
        i = i + 1

def fibnoacci():
    a = 0
    b = 1
    while True:
        yield a
        result = a + b
        a = b
        b = result

# # Comprehension    
evens = [ item for item in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] if item % 2 == 0 ]

# regular function
def evens():
    e = [ ]
    for item in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        if item % 2 == 0:
            e.append(item)
    return e

# Generator Function
def evens():
    for item in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        if item % 2 == 0:
            yield item

# Generator Expression    
evens = ( item for item in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] if item % 2 == 0 )