from re import findall

# returns a list of all the matches

result = findall(r"the", "the theory of relativity")

result = findall(r"cat", "The dragging belly indicates your cat is too fat")

result = findall(r"aeiou", "hello how are you doing anna")

result = findall(r"aeiou", "hello there it is aeiou aei hi")

# I want to match "Smith" or "smith"
# square brackets are called character set
result = findall(r"[Ss]mith", "hello smith how are you Smith")

# I want to match "seperate" or "saperate" or "separate"
result = findall(r"s[ea]p[ea]rate", "seperate")

# Matches only characters either "a" or "e" or "i" or "o" or "u"
result = findall(r"[aeiou]", "hello how are you doing anna")

# matches characters either "a" or "b" or "c" or "d"
result = findall(r"[abcd]", "hello world welcome to python")

result = findall(r"[0123456789]", "the cost of this book is Rs.100")

# I want to match all heading in a HMTL
"""
<h1>Hello<h1>
<h2>Hello<h2>
<h3>Hello<h3>
<h4>Hello<h4>
<h5>Hello<h5>
<h6>Hello<h6>
"""
result = findall(r'<h[123456]>', "<h4>Hello<h4>")

# "-" it is called range
result = findall(r"[0-9]", "the cost of this book is Rs.100 and the cost of mac is 967")

# Matches only lower case characters between a-z
result = findall(r"[a-z]", "hello HOW ARE YOU")


# Matches only upper case characters between A-Z
result = findall(r"[A-Za-z]", "hello HOW ARE YOU Rs.100")

# Matches any number between 1 and 6 (Inclusive)
result = findall(r'<h[1-6]>', "<h1>Hello<h1>")

sentence = "Hello World Welcome To Python"
# lower_count = 0
# upper_count = 0

# for letter in sentence:
#     if letter.islower():
#         lower_count += 1
#     elif letter.isupper():
#         upper_count += 1
lower_case_count = len(findall(r"[a-z]", sentence))
upper_case_count = len(findall(r"[A-Z]", sentence))


# Count the number of white spaces in the given string
sentence = "Hello World Welcome To Python     hello world"
# space_count = 0 
# for letter in sentence:
#     if letter == " ":
#         space_count += 1

# \s matches with white space
spaces_count = len(findall(r"\s", sentence))

# Write a program to count the number of occurrences of each lower case and upper case alphabets
sentence = 'hello@world! welcome!!! Python$ hi how are you & where are you?'
# d = {"h": 4, "e": 3, "P": 3, }
result = findall(r"[a-zA-Z]", sentence)

# using dict comprehension
d = { letter: result.count(letter)  for letter in result }

# using default dict
from collections import defaultdict
d = defaultdict(int)
for letter in result:
    d[letter] += 1

from collections import Counter
d = Counter(result)