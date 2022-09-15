class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __len__(self):
        print("executing __len__")
        return 2
    
    def __contains__(self, item):
        if item in self.__dict__.values():   # 10 in [10, 20].__contians__(1)
            return True
        return False
    
    def __getitem__(self, index):
        if index == 0:
            return self.a
        elif index == 1:
            return self.b
        else:
            raise Exception("Point Object is out of index")
        
    def __setitem__(self, index, value):
        if index == 0:
            self.a = value
        elif index == 1:
            self.b = value
        else:
            raise Exception("Point Object is out of index")


p = Point(1, 2)
p2 = Point(10, 20)