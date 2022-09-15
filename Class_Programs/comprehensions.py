# [ expression   for item in iterable ]
numbers = [1, 2, 3, 4, 5]
squares = [ ]
for item in numbers:
    squares.append(item ** 2)

# List Comprehension
_squares = [  item ** 2 for item in numbers ]

numbers = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
evens = [ ]
for number in numbers:
    if number % 2 == 0:
        evens.append(number)
    
# Using comprehension
_evens = [ number for number in numbers if number % 2 == 0 ]

# List of even numbers from 1 to 50
evens = [ ]
for i in range(1, 51):
    if i % 2 == 0:
        evens.append(i)

_evens = [  i  for i in range(1, 51) if i % 2 == 0 ]

names = ['laura', 'steve', 'bill', 'james', 'bob', 'greig', 'scott', 'alex', 'ive']

vowel_names = [ ]
for name in names:
    if name[0] in "aeiou":
        vowel_names.append(name)

# using list comprehension
_vowel_names = [  name  for name in names if name[0] in 'aeiou' ]

languages = ['Python', 'Java', 'Perl', 'PHP', 'Python', 'JS', 'C++', 'JS', 'Python', 'Ruby']

p_languages = [ ]
for language in languages:
    if language[0] in 'P':
        p_languages.append(language)

# using comprehension
_p_languages = [  language  for language in languages if language[0] == 'P' ]

names = ['laura', 'steve', 'bill', 'james', 'bob', 'greig', 'scott', 'alex', 'ive']

consonents = [ ]
for name in names:
    if name[0] not in 'aeiou':
        consonents.append(name)

# Comprehension
_consonents = [  name  for name in names if name[0] not in 'aeiou' ]

names = ['apple', 'google', 'yahoo', 'gmail', 'flipkart', 'instagram', 'microsoft']

less_6_chars = [ ]
for name in names:
    if len(name) < 6:
        less_6_chars.append(name)

# using comprehension
_less_6_chars = [ name  for name in names if len(name) < 6 ]

numbers = [ 1, 2, 3, 4, 5 ]

# [1, 2, 9, 64, 625]
index = [ ]
for i, number in enumerate(numbers):
    index.append( number ** i )

_index = [  number ** i   for i, number in enumerate(numbers) ]

names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']

# [ ("apple", 5), ("google", 6), ('yahoo', 5)  ]

items = [ ]
for name in names:
    items.append((name, len(name)))

# using comprehension
_items = [ (name, len(name))  for name in names ]

names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']

even_len_string = [ ]
for name in names:
    if len(name) % 2 == 0:
        even_len_string.append(name)

# using comprehension
_even_len_string = [  name for name in names if len(name) % 2 == 0]

numbers = [1, 2, 3, 4, 5]

def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number -1)

fact_numbers = [ ]

for number in numbers:
    f = factorial(number)
    fact_numbers.append(f)

# using comprehension
_fact_numbers = [ factorial(item)  for item in numbers ]

from math import factorial, pi

fact = [ factorial(number) for number in numbers ]

pi_values = [  round(pi, i)  for i in range(1, 6) ]

names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']

reverse_odd_items = [ ]

for name in names:
    if len(name) % 2 == 1:
        reverse_odd_items.append(name[::-1])

# using comprehension
_reverse = [ name[::-1]  for name in names if len(name) % 2 == 1 ]

names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']

reverse_odd = [ ]
for name in names:
    if len(name) % 2 == 0:
        reverse_odd.append(name)
    else:
        reverse_odd.append(name[::-1])


_reverse_odd = [  name  if len(name) % 2 == 0 else name[::-1] for name in names  ]

def process_name(name):
    if len(name) % 2 == 0:
        return name
    else:
        return name[::-1]

_reverse_odd = [ process_name(name) for name in names ]

data = ['hello', 123, 1.2, 'world', True, 'python']

reverse_str = [ ]

for item in data:
    if isinstance(item, str):
        reverse_str.append(item[::-1])
    else:
        reverse_str.append(item)

# using comprehension

def reverse_string(item):
    if isinstance(item, str):
        return item[::-1]
    else:
        return item

_reverse_str = [  reverse_string(item) for item in data ]

r = [  item[::-1] if isinstance(item, str) else item for item in data ]

def is_prime(number):
    if number == 1:
        return False
    for i in range(2, number):
        if number % i == 0:
           return False
    return True

prime_numbers = [ ]

for i in range(1, 51):
    if is_prime(i):
        prime_numbers.append(i)

prime_numbers = [ i for i in range(2, 51) if is_prime(i) ]

a = [1, 2, 3, 4]
b = [5, 6, 7, 8]

c = [ ]

for x, y in zip(a, b):
    c.append(x + y)

# using comprehension
_c = [  x + y for x, y in zip(a, b) ]

items = [ [1, 2, 3], [4, 5, 6], [7, 8, 9]  ]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

a = [   number for item in items  for number in item ]
