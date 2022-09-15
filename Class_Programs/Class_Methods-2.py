class Points:
    def __init__(self):
        self._points = [ ]
    
    @classmethod
    def from_file(cls):
        p = cls()
        with open("./data_files/points.txt") as f:
            for line in f:
                parts = line.split()
                p._points.append((parts[0], parts[1], parts[2]))
        return p
    
    @property
    def average(self):
        x_total = y_total = z_total = 0
        for item in self._points:
            x_total += float(item[0])
            y_total += float(item[1])
            z_total += float(item[2])
            return (x_total/len(self._points), y_total/len(self._points), z_total/len(self._points))
    
    @property
    def minimum(self):
        x_min = min([  item[0] for item in self._points ])
        y_min = min([  item[1] for item in self._points ])
        z_min = min([  item[2] for item in self._points ])
        return (x_min, y_min, z_min)
    
    @property
    def maximum(self):
        x_max = max([  item[0] for item in self._points ])
        y_max = max([  item[1] for item in self._points ])
        z_max = max([  item[2] for item in self._points ])
        return (x_max, y_max, z_max)