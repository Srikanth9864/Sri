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
