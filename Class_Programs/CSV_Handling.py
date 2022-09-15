from csv import reader, DictReader

def read_csv():
    # Context Manager
    with open("./data_files/employees.csv") as f:
        records = [ ]
        # creating object instance to reader class
        # and passing file object as a constructor argument
        # rows is iterator object
        rows = DictReader(f)
        # headers = next(rows)        # skipping the headerss
        for row in rows:
            records.append(row)
    return records

# i want to know the total pay that i am paying to all the employees as salary
def total_pay():
    data = read_csv()
    total = 0.00
    for item in data:
        total = total + float(item['pay'])
    return total

# by_gender = {"Male": 6, "Female": 5}
def get_count_by_gender():
    """This function returns a dictionary with gender and its count pair
        eg.  {"Male": 6, "Female": 5}
    """
    data = read_csv()
    by_gender = { }
    for item in data:
        gender = item['gender']
        if gender in by_gender:
            by_gender[gender] = by_gender[gender] + 1
        else:
            by_gender[gender] = 1
    return by_gender

def highest_pay():
    data = read_csv()
    by_pay = sorted(data, key=lambda item: float(item['pay']))
    return by_pay

def unique_teams():
    employees = read_csv()
    # using list comprehension
    # teams = [  employee['team']  for employee in employees ]
    teams = [ ]
    for employee in employees:
        teams.append(employee['team'])
    unique_teams = [ ]
    for item in teams:
        if item not in unique_teams:
            unique_teams.append(item)
    return unique_teams

def more_than_4500():
    # { "fname": "steve", "lname": "jobs", "pay": 4500 }
    employees = read_csv()
    more_4500 = [ ]
    for employee in employees:
        if float(employee['pay']) >= 4500:
            d = {"fname": employee['fname'],  "lname": employee['lname'], "pay": employee['pay']}
            more_4500.append(d)
    return more_4500