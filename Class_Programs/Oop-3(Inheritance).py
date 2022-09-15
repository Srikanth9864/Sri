class Parent:
    def __init__(self, value):
        self.value = value
    
    def apple(self):
        print(f"Executing Parent Apple {self.value}")
    
    def google(self):
        print("Executing Parent Google")
        self.apple()

# Case1: Child class having Independent Method
class Child1(Parent):
    def __init__(self, value):
        # calling parent class Constructor
        super().__init__(value)

    def yahoo(self):
        print("Child1 Yahoo")

# Case2: Child class overriding Parent class Method
class Child2(Parent):
    def __init__(self, value):
        super().__init__(value)
    
    # Method Overriding
    def apple(self):
        print(f"Executing Child2 Apple {self.value}")

# Case3: Child class overriding Parent, but re-using the Parent class Functionlity
class Child3(Parent):
    def __init__(self, value):
        super().__init__(value)
    
    def apple(self):
        # this is the extra functionality
        print("Executing Child3 Apple")
        # Re-using the parent class functionality
        super().apple()

# Case4: Child class having a separate attribute in __init__ method
class Child4(Parent):
    def __init__(self, value, extra_value):
        # super().__init__(value)
        Parent.__init__(self, value)
        self.extra_value = extra_value

# Case5: Child inheriting from Mutliple Parents
class Parent2:
    def __init__(self, a):
        self.a = a

    def facebook(self):
        print("Executing Parent2 Facebook")

class Child5(Parent, Parent2):
    def __init__(self, x, y):
        Parent.__init__(self, x)
        Parent2.__init__(self, y)

    def whatsapp(self):
        print("Executing Child5 Whatsapp")

# Multi-Level Inheritance
class A:
    def demo(self):
        print("A")

class B(A):
    def demo(self):
        print("B")
        # super().demo()
        A.demo(self)

class C(B):
    def demo(self):
        print("C")
        # super().demo()
        B.demo(self)


class Parent:
    def spam(self):
        print("Parent Spam")


class Child1(Parent):
    def spam(self):
        print("Child1 Spam")
        super().spam()

class Child2(Parent):
    def spam(self):
        print("Child2 spam")
        super().spam()

class Child3(Child1, Child2):
    pass

# __mro__ (Method Resolution Order) is the order in which python looks up for an attribute in inheritance hierarchy
# Child3.__mro__

class Spam:
    a = 10  # class Variable
    def apple(self):
        print(f"Spam Apple {self.__class__.a}")

class Demo(Spam):
    # overriding class variable
    a = 20 # class Variable
    def google(self):
        print("Google")