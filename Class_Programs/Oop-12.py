# t = (1, 2)
# d1 = {"a": 1, "b": 2}
# d2 = {"x": 4, "y": 5}

a = [1, 2]
b = [3, 4]

# low-level operations (indexing)
# total = a[0] + a[1]
# a[0] = a[0] + 0.5
# a[1] = a[1] + 0.5

# # want to swap the co-ordinates
# x = a[0]
# y = a[1]
# a[0] = y
# a[1] = x

# reset the co-ordinates to [0, 0]
a[0] = 0
a[1] = 0


class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def move(self, dx, dy):
        self.a = self.a + dx
        self.b = self.b + dy
    
    def reset(self):
        self.a = 0
        self.b = 0
    
    def sort(self):
        if self.a > self.b:
            temp = self.a
            self.a = self.b
            self.b = temp
        
    def total(self):
        return self.a + self.b

# __init__ method is helping us to do that
# internally the data is stored inside the dict
# which will be created once the __init__ method is called
# __init__ is also called as constructor. It will be automatically called
# when you call the class to save the data or when you create an instance 
# of the class

# Saving the data inside the class
# p1 = Point(1, 2)
# p2 = Point(3, 4)
# p3 = Point(5, 6)

# # manuplating the data contained inside a dictionary
# p1.move(0.1, 0.1)       # Point.move(p1, 0.1, 0.1)
# p2.move(0.5, 0.5)       # Point.move(p2, 0.5, 0.5)
# p3.move(1, 2)       # Point.move(p3, 1, 1)

# # see the dictionary where the data is stored
# # instance dictionaries
# print(p1.__dict__)
# print(p2.__dict__)
# print(p3.__dict__)


class Calculator:
    def __init__(self, a, b):
        print(f"Calling __init__ method and saving {a} and {b}")
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

# saving the date inside calcualtor object (inside dict)
c1 = Calculator(10, 20)
c2 = Calculator(1, 2)
c3 = Calculator(15, 25)

e1 = {"fname": "steve", "lname": "jobs", "pay": 1000}
e2 = {"fname": "bill", "lname": "gates", "pay": 2000}

class Employee:
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay

    def email(self):
        return f"{self.fname}.{self.lname}@company.com"
    
    def pay_hike(self, percentage_hike):
        hike_amount = self.pay * percentage_hike
        self.pay = self.pay + hike_amount

e1 = Employee("steve", "jobs", 1000)
e2 = Employee('bill', 'gates', 2000)

e1.pay_hike(0.1)    # Employee.pay_hike(e1)
e2.pay_hike(0.05)   # Employee.pay_hike(e2)

class Point:
    def __init__(self, a=0, b=0, c=0):
        self.a = a
        self.b = b
        self.c = c

p1 = Point()
p2 = Point(1)
p3 = Point(1, 2)
p4 = Point(1, 2, 3)
p5 = Point(a=10, b=20, c=30)
p6 = Point(10, 20, c=30)

# class Point {
#     public void Point() {
#         this.Point(0, 0, 0)
#     }
    
#     public void Point(a) {
#         this.Point(a, 0, 0)
#     }

#     public void Point(a, b) {
#         this.Point(a, b, 0)
#     }

#     public void Point(a, b, c) {
#         this.a = a
#         this.b = b
#         this.c = c
#     }
# }

class Point:
    # overloaded constructor can be achieved by 
    # having default valules to the arguments
    def __init__(self, a=0, b=0, c=0):
        self.a = a
        self.b = b
        self.c = c
    
    def __init__(self, a, b):
        self.a = a
        self.b = b

def add(a, b):
    return a + b

def add(a, b, c):
    return a + b + c

p1=add(1,2)
print(p1.__dict__)



# Point p1 = new Point()
# Point p2 = new Point(1)
# Point p3 = new Point(1, 2)
# Point p4 = new Point(1, 2, 4) 