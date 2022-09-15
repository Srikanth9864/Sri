class Point(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __setattr__(self, name, value):
        if not isinstance(value, (int, float)):
            raise Exception("Only Numbers are allowed")
        if value < 0:
            raise Exception(f"Cannot set negative value to {name}")
        super().__setattr__(name, value)
    
    def mul(self):
        return 2 * 3.14 * self.a * self.b

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __setattr__(self, name, value):
        super().__setattr__(name, value[::-1])

class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __setattr__(self, name, value):
        if not isinstance(value, (int, float)):
            raise Exception("Only Numbers are allowed")
        super().__setattr__(name, value)

    def mul(self):
        return self.a * self.b

class Employee:
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay

    def __setattr__(self, name, value):
        if name == "fname" or name == "lname":
            if len(value) > 5:
                raise Exception("Cannot set fname or lname to more than 5 characters")
            else:
                super().__setattr__(name, value)
        if name == "pay":
            if value < 500:
                raise Exception("Minimum Pay cannnot be less than $500")
            else:
                super().__setattr__(name, value)

class Employee:
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
    
    def __setattr__(self, name, value):
        if not name in ("fname", "lname", "pay"):
            raise AttributeError(f"No Attribute named {name}")
        super().__setattr__(name, value)


class Point:
    def __init__(self, a, b):
        super().__setattr__("a", a)
        super().__setattr__("b", b)
        
    def __setattr__(self, name, value):
        raise Exception("No NO")