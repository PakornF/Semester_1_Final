import math

class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.m = (y2 - y1) / (x2 - x1)
        self.y_intercept = y1 - self.m * x1

    def contains(self, x, y):
        if y == self.m * x + self.y_intercept:
            return (min(self.x1, self.x2) <= x <= max(self.x1, self.x2)
                    and min(self.y1, self.y2) <= y <= max(self.y1, self.y2))
        else:
            return False

    def get_distance(self):
        return math.sqrt((self.x1 - self.x2) ** 2 + (self.y1 - self.y2) ** 2)

    def get_x1(self):
        return self.x1

    def get_y1(self):
        return self.y1

    def get_x2(self):
        return self.x2

    def get_y2(self):
        return self.y2

    def get_y(self, x):
        y = self.m * x + self.y_intercept
        if self.contains(x, y):
            return y
        else:
            return -999.999

class LineApp:
    x1 = float(input("Enter x1 : "))
    y1 = float(input("Enter y1 : "))
    x2 = float(input("Enter x2 : "))
    y2 = float(input("Enter y2 : "))

    print(f"value of x1 on this line is {x1:.3f}")
    print(f"value of x2 on this line is {x2:.3f}")
    print(f"value of y1 on this line is {y1:.3f}")
    print(f"value of y2 on this line is {y2:.3f}")

    line = Line(x1, y1, x2, y2)

    print("==========")
    print(f"Check x and y are on this line ?")
    x = float(input("Enter x : "))
    y = float(input("Enter y : "))

    if line.contains(x, y):
        print(f"x = {x:.3f} and y = {y:.3f} are on this line")
    else:
        print(f"x = {x:.3f} and y = {y:.3f} are not on this line")

    distance = line.get_distance()
    print(f"Distance between startPoint and endPoint is {distance:.3f}")
    print(f"==========")
    print(f"Find value of y that gives( x , y ) on this line")
    x = float(input("Enter x : "))
    y = line.get_y(x)
    print(f"value of y is {y:.3f}")
    if y != -999.999:
        print(f"( x , y ) = ( {x:.3f} , {y:.3f} ) on this line")
    else:
        print(f"( x , y ) = ( {x:.3f} , {y:.3f} ) is not on this line")