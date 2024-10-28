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
# class Vector(list):
#     def __str__(self):
#         return " ".join(map(str, self))

# v = Vector([2,5,8,-3])
# print(v)

# ls2 = map(math.sqrt, range(10))
# v2 = Vector(ls2)
# print(v2[3:6])
#
# print(list.__class__)
# print(Vector.__class__)
# print(list.mro())
# print(Vector.mro())

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

# Decorators
# 1 - Function can be used as object and called by another name
# def func1(text):
#     return text.upper()
#
# print(func1("Hello"))
#
# name = func1
# print(name("World"))

# 2 - Passing the function as an argument

# def func1(text):
#     return text.upper()
#
# def func2(text):
#     return text.lower()
#
# def greet(name):
#     greeting = name("Hi, I am created by a function that passed as an argument")
#     print(greeting)
#
# greet(func1)
# greet(func2)

# def make_adder(x):
#     def adder(y):
#         return x + y
#     return adder
#
# add_45 = make_adder(45)
# print(add_45(35))
# print((make_adder(45))(35))

# def func():
#     print("How are you?")

# func()

# def mydecorator(fn):
#     def inner_func():
#         fn()
#         print("How are you?")
#     return inner_func
#
# @mydecorator
# def greet():
#     print("Hello! ", end='')
#
# greet()

# def hello_decorator(func):
#
#     # inner function is a wrapper function in which the argument is called
#     def inner():
#         print("Hello, this is before function execution")
#         # calling the actual function now
#         func()
#         print("This is after function execution")
#     return inner
#
# def function_to_be_used_outside():
#     print("This is inside the the function!!")
#
# function_to_be_used_outside = hello_decorator(function_to_be_used_outside)
#
# function_to_be_used_outside()

# Chaining Decorators

# def decor1(func):
#     def inner():
#         x = func()
#         return x * x
#     return inner
#
# def decor2(func):
#     def inner():
#         x = func()
#         return 2 * x
#     return inner
#
# @decor2
# @decor1
# def num():
#     return 10
# print(num())
# # print(decor1(decor2(num())))

# class Rectangle:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     @property
#     def area(self):
#         return self.a * self.b
#
# rect = Rectangle(4,5)
# print(rect.area)

# class Point:
#     MAX_COORD = 100
#     MIN_COORD = 0
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def set_coord(self, x, y):
#         if self.MIN_COORD <= x <= self.MAX_COORD:
#             self.x = x
#             self.y = y
#
#     @classmethod
#     def __set_bound(cls, left):
#         cls.MIN_COORD = left
#     @classmethod
#     def root_setter(cls, min):
#         cls.min = min
#         cls.MIN_COORD = cls.min
#
#     def __getattribute__(self, item):
#         # print("You tried to get some object attribute")
#         try:
#             if item == '__dict__':
#                 raise ValueError("no access")
#         except ValueError:
#             print("Sorry, this attribute is not accessible")
#         else:
#             return object.__getattribute__(self,item)
# pt1 = Point(10,20)
# pt2 = Point(50,70)
# pt1.root_setter(-50)
# print(pt1.MIN_COORD)
# pt1.set_coord(40,50)
# print(Point.MIN_COORD)
# print(pt1.__dict__)
# # print(Point.__dict__)
# print(pt2.MIN_COORD)

class FibonacciIterator:
    def __init__(self, stop=10):
        self.stop = stop
        self.index = 0
        self.current = 0
        self.next = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.stop:
            self.index += 1
            fib_num = self.current
            self.current, self.next = self.next, self.current + self.next
            return fib_num
        else:
            raise StopIteration
fi = FibonacciIterator(15)
for fib_num in fi:
    print(fib_num)
# print(type(fi))