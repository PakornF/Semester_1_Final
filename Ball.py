import copy
from Vector import Vector

class Ball:
    """Maintains ball objects which can calculate their own movements."""

    def __init__(self, pos, vel, acc):
        self.pos = pos
        self.vel = vel
        self.acc = acc

    def __repr__(self):
        return f"Ball(pos={self.pos}, vel={self.vel}, acc={self.acc})"

ball1 = Ball(pos=Vector(1, 2), vel=Vector(3, 4), acc=Vector(5, 6))
ball2 = copy.deepcopy(ball1)
ball3 = copy.copy(ball1)
ball4 = ball1

print("-------------")
print("Before update")
print("-------------")
print(f"ball1 = {ball1}")
print(f"ball2 = {ball2}")
print(f"ball3 = {ball3}")
print(f"ball4 = {ball4}")

ball2.pos.x = 80
ball3.vel.x = 999
ball4.acc = Vector(0, 0)

print("------------")
print("After update")
print("------------")
print(f"ball1 = {ball1}")
print(f"ball2 = {ball2}")
print(f"ball3 = {ball3}")
print(f"ball4 = {ball4}")