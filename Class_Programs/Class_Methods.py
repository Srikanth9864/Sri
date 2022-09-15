from json import loads


class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def circumference(self):
        return 2 * 3.14 * self.radius
    
    @classmethod
    def from_diameter(cls, diameter):      # cls is a stand-in for "Cirlce"
        print(cls)  # print(Circle)
        radius = diameter/2
        # Circle(radius)
        return cls(radius)      # Creating an instance of Circle class


class Employee:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age
    
    @classmethod
    def from_string(cls, data):
        parts = data.split(",")
        fname, lname, age = parts       # fname = parts[0], lname = parts[1], age = parts[2]
        # return cls(parts[0], parts[1], parts[2])
        return cls(fname, lname, age)   # Employee("steve", "jobs", 26)
    
    @classmethod
    def from_json(cls, json_string):
        json_data = loads(json_string)
        fname = json_data['fname']
        lname = json_data['lname']
        age = json_data['age']
        return cls(fname, lname, age)


data = "steve,jobs,26"
json_string = """
{
    "fname": "bill",
    "lname": "gates",
    "age": 30
}
"""

c = Circle(5)
cir = c.circumference()
print(cir)
rad = c.from_diameter(8)
print(rad.__dict__)
e2 = Employee.from_string(data)
print(e2.__dict__)
e3 = Employee.from_json(json_string)
print(e3.__dict__)