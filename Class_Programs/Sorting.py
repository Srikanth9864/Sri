names = ['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft', 'zomato']

numbers = (1, 2, 6, 7, 10, 3, 4, 5)

word = "hello"

items = ['bbbb', 'aaaaaa', 'yy', 'z', 'ccc']

def get_len(some_string):
    return len(some_string)

s_items = sorted(items, key=get_len)

items = ['bv', 'aw', 'dt', 'cu']

def get_last_chr(item):
    return item[-1]

s_items = sorted(items, key=get_last_chr)

s_items = sorted(items, key=lambda item: item[-1])

temperatures = [('Bangalore', 25), ('Delhi', 35), ('Chennai', 37), ('Mumbai', 32)]

def get_temp(item):
    return item[-1]

s_temperature = sorted(temperatures, key=get_temp)

prices = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75 }

# item = ('ACME', 45.23)
def get_share_price(item):
    return item[-1]

# key_value_pairs = prices.items()
items = prices.items()
s_prices = sorted(items, key=get_share_price)
# s_prices = sorted(value)

portfolio = [
                {'name': 'IBM', 'shares': 100, 'price': 91.1 },
                {'name': 'AAPL', 'shares': 50, 'price': 543.22 },
                {'name': 'FB', 'shares': 200, 'price': 21.09},
                {'name': 'HPQ', 'shares': 35, 'price': 31.75},
                {'name': 'YHOO', 'shares': 45, 'price': 16.35},
                {'name': 'ACME', 'shares': 75, 'price': 115.65}
            ]

def get_name(item):
    return item['name']

def get_shares(item):
    return item['shares']

def get_price(item):
    return item['price']

def get_total(item):
    return item['price'] * item['shares']

by_name = sorted(portfolio, key=get_name)
by_shares = sorted(portfolio, key=get_shares)
by_price = sorted(portfolio, key=get_price)
by_total_cost = sorted(portfolio, key=get_total)

by_name = sorted(portfolio, key=lambda item: item['name'])
by_shares = sorted(portfolio, key=lambda item: item['shares'])
by_price = sorted(portfolio, key=lambda item: item['price'])
by_total_cost = sorted(portfolio, key=lambda item: item['shares'] * item['price'])

students = [
    {"name": "john", "grade": "A", "age": 26},
    {"name": "jane", "grade": "B", "age": 28},
    {"name": "dave", "grade": "B", "age": 22}
]

by_name = sorted(students, key=lambda student: student['name'])
by_grade = sorted(students, key=lambda student: student['grade'])
by_age = sorted(students, key=lambda student: student['age'])

items = [[2, 7], [7, 3], [3, 8], [8, 7], [9, 7], [4, 9]]

by_first_item = sorted(items, key=lambda item: item[0])
by_last_item = sorted(items, key=lambda item: item[-1])

sentence = "This is a Programming language and Programming is fun"
words = sentence.split()
word_len_pair = {  word: len(word) for word in words }
key_value_pairs = word_len_pair.items()
by_len = sorted(key_value_pairs, key=lambda item: item[-1])

sentence = "This is a Programming language and Programming is fun"
words = sentence.lower().split()
word_len_pair = {  word: len(word) for word in words if words.count(word) == 1 }
d = sorted(word_len_pair.items(), key=lambda item: item[-1])

sentence = "hi hello hi hello world hi universe hi world hello world hi world"
words = sentence.split()
word_count_pair = { word: words.count(word) for word in words }
most_repeated_word = sorted(word_count_pair.items(), key=lambda item: item[-1])[-1]

sentence = 'hi hello hi hi hiiiiii'
char_count_pair = { letter: sentence.count(letter) for letter in sentence if letter.strip()}
by_letter_count = sorted(char_count_pair.items(), key=lambda item: item[-1])[-1]