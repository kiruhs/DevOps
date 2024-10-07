# OOP Object Oriented Programming
a = list((1, 2, 3))
# a.append_something(4)

list.__dict__
# print(a)

# class Point:
#     "This class is very simple for learning only"
#
#     x = 100 # raersefs
#     lst = [1, 3, 45, 6, -5, 0]
#     y = 30
#     z = 450
#     a = "Hello, world"
#     color = 'red'

# Point.func = (lambda x: x**2 + 5) (5)
# print(Point.func)
# p1 = Point()
# p1.func = (lambda x: x**2 - 5) (5)
#
# print(p1.func)


# print(Point.__sizeof__(Point))

# print(Point)
# help(Point)
# p1.x = 4
# setattr(p1, 'x', 8)
# setattr(Point, 'x', 5)
# Point.x = 10
# print(p1.x)
# print(Point.x)
# p2 = Point()
# print(p1)
# print(p2)
# print(p1 == p2)

# Magic methods = dunder methods Double UNDERscope
# print(p1.__dict__)
# __doc__

# class Point:
#     "This class is very simple for learning only"
#
#     # x = 100
#     # y = 30
#     # z = 450
#     color = 'red'
#     def __init__(self, x, y, z, *args):
#         self.x = x
#         self.y = y
#         self.z = z
#         self.args = args
#
#     def ret(self):
#         return self.args
#
# p1 = Point(10, 30, 50, 45, 34, 123)
# print(p1.x)
# print(Point.color)
#
# p2 = Point(3, 5, -3)
# print(p2.x)
# print(p2.args)
#
# p2.z = 100500
# print(p2.z)

# class Vector:
#     MIN_COORD = 0
#     MAX_COORD = 100
#     @classmethod
#     def avg(MIN_COORD, MAX_COORD):
#         res = (MAX_COORD+MIN_COORD)//2
#         return res
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def get_coord(self):
#         return self.x, self.y
#
# d = Vector(100, 200)
# v = Vector(10, 20)
#
# print(dir(d.get_coord))
# print(d.get_coord())

import math
class Vector(list):
    def __str__(self):
        return " ".join(map(str, self))

v = Vector([2,5,8,-3])
print(v)

ls2 = map(math.sqrt, range(10))
v2 = Vector(ls2)
# print(v2[3:6])
#
# print(list.__class__)
# print(Vector.__class__)
print(list.mro())
print(Vector.mro())