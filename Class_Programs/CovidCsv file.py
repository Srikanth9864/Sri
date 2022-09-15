from csv import reader, DictReader

def read_csv():
    # Context Manager
    with open("./data_files/covid-data.csv") as f:
        records = [ ]
        # creating object instance to reader class
        # and passing file object as a constructor argument
        # rows is iterator object
        rows = DictReader(f)
        # headers = next(rows)        # skipping the headerss
        for row in rows:
            records.append(row)
    return records

# total number of cases accross the word
def total_cases():
    total = 0
    data = read_csv()
    for item in data:
        total = total + int(item['new_cases'])
    return total

# total cases by country
# by_country = {"India": 43543675, "USA": 387538945, "France": 8733982}
def total_cases_by_country():
    by_country = { }
    data = read_csv()
    for item in data:
        country = item['location']
        cases = int(item['new_cases'])
        if country in by_country:
            by_country[country] += cases
        else:
            by_country[country] = cases
    return by_country

# list of countries affected by COVID-19
def countries():
    _countries = [ ]
    data = read_csv()
    # using list comprehension
    # _countries = [ item['location']  for item in data ]
    for item in data:
        _countries.append(item['location'])
    unique_countries = set(_countries)
    return unique_countries

# set comprehension 
def countries():
    data = read_csv()
    # set comprehension
    return { item['location']  for item in data }

def countries_less_10K():
    less_10K = { }
    by_country = total_cases_by_country()
    for country, cases in by_country.items():
        if cases <= 10000:
            less_10K[country] = cases
    return less_10K

# using comprehension (dictionary)
def countries_less_10K():
    by_country = total_cases_by_country()
    return { country: cases  for country, cases in by_country.items() if cases <= 10000 }