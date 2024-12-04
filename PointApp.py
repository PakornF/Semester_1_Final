class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_on_x_axis(self):
        return True if self.y == 0 else False

    def is_on_y_axis(self):
        return True if self.x == 0 else False

    def translate(self, distX, distY):
        self.x += distX
        self.y += distY

    def __str__(self):
        return f"({self.x}, {self.y})"

    def get_x(self):
        return self.x

    def set_x(self, new_x):
        self.x = new_x

    def get_y(self):
        return self.y

    def set_y(self, new_y):
        self.y = new_y

class PointApp:
    p1 = Point(20, 100)
    p2 = Point(-40, 50)
    print(Point.is_on_x_axis(p1))
    print(Point.is_on_y_axis(p2))
    Point.translate(p1, -60, -50)
    print(p1==p2)
    print(p1)
    print(p2)