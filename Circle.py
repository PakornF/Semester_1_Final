import math

class Circle:
    def __init__(self, x = 0, y = 0, radius = 0) -> None:
        self.radius = radius
        self.x = x
        self.y = y
    def get_perimeter(self):
        return 2 * math.pi * self.radius
    def get_area(self):
        return math.pi * (self.radius ** 2)
    def __str__(self):
        return f"Center: ({self.x:.1f}, {self.y:.1f}), Radius: {self.radius:.1f}"
    def get_center_x(self):
        return self.x
    def get_center_y(self):
        return self.y
    def get_radius(self):
        return self.radius
    def set_center_x(self, new_x):
        self.x = new_x
    def set_center_y(self, new_y):
        self.y = new_y
    def set_radius(self, new_radius):
        self.radius = new_radius