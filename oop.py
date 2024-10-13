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

# 09.10.2024

# Vector([2])
# # v2(ls2)
# print(callable(Vector))
# print(callable(v2))

# class Base1:
#     b = "Public"
#     def __init__(self):
#         self.a = "It is public"
#         self._b = "It is protected"
#         self.__c = "It is private"
        # self.d = self.__c
        # print(self.__c)
# class Derived(Base1):
#     def __init__(self):
#         super().__init__()
#         print(self._Base1__c)
# #         # print()
#
# d1 = Derived()
# b1 = Base1()
# # print(b1.d)
# # b1.d = "Kuku"
# print(b1._b)
# # print(d1.a)
# b1._b = "And now it is fully public"
# print(b1._b)

# print(b1.__c)

# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return f"it is {self.name}"
#
#     def __repr__(self):  # for debugging mode
#         return f"{self.__class__}"
#
# cat = Cat('Micky')
# print(cat)
# print(cat.__dict__)
# print(repr(cat))

# class Point:
#     def __init__(self, *args):
#         self.__args = args
#
#     def __len__(self):
#         return len(self.__args)
#
#     def __abs__(self):
#         return list(map(abs, self.__args))
#
# it = [1, -2, 5, True, -100.5]
# p = Point(*it)
# print(len(p))
# print(abs(p))

# s = 'five'
# print(s*5) # '4five5'

# class Letnum:
#     "This class should be able to concatenate strings to integer and vice versa by + operator"
#     def __init__(self, symbol):
#         self.symbol = symbol
#
#     def __str__(self):
#         return f"{self.symbol}"
#
#     def __add__(self, other):  # +
#         let = str(self.symbol) + str(other)
#         return Letnum(let)
#
#     def __radd__(self, other):
#         let = str(other) + str(self.symbol)
#         return Letnum(let)
#
# st = Letnum(s) # 'five' + 5  4+5=45
#
# st2 = st+5
# print(st2)
# st3 = 4+st2+7+4+4+"hello"+[3,4,5,6]+{3:5}+True
# print(st3)
# help(Letnum)

# ================================================================================================
# lst = {3, 8, -8,"hello", 0, -17, 5, 'a'} # <<3, 8, -8, 0, -17, 5>>
#
# class My_arr(list):
#     "This class inherits from list and sorts all elements and more.."
#
#     def __init__(self, it):
#         a = []
#         for i in it:
#             if isinstance(i, (int,float,bool)):
#                 a.append(i)
#         it = a
#         super().__init__(sorted(it))
#         self.index = 0
#
#     def __str__(self):
#         return f"<<{', '.join(str(item) for item in self)}>>"
#
#     def append(self, __object):
#         super().append(__object)
#         self.sort()
#
#
#
#     def __getitem__(self, item):
#         it = super().__getitem__(item)
#         if isinstance(item, slice):
#             return f"<<{', '.join(str(i) for i in it)}>>"
#         return it
#
# new_list = My_arr(lst)
# new_list2 = My_arr(lst)
# print(new_list == new_list2)
# print(new_list)
# # print(My_arr.mro())
# new_list.append(-100)
# print(new_list)
# print(new_list[2:4])
