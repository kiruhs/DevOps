# a = 3
# b = "Hello "
# c = "World"
# # print(a)
# print(a, a*2, a**3, -a, "a", sep=", ")
# print(a*3)
# print(3*b*3)
# print(b / c)

# name = input("Input your name: ")
# name = "Hello, hanny world"
# print(name)
# print(name.upper())
# # print(name.lower())
# # print(name.capitalize())
# print(name.replace("hanny", "wonderful"))
# print(name)

txt = "The best things in life are free!"
# print(txt.count(" "))
# print(txt.lower().count("th"))
# print(type(txt.lower().count("th")))
# x = txt.split()
# print(x)
# y = txt.split("i")
# print(y)

# x, y = 5, 10
# print(y, x)
# x, y = y, x
# print(y)


# if x > 0:
#     print("The number is positive")
# elif x< 0:
#     print("The number is negative")
# else:
#     print("Zero")
x = 0
y = 5
# if x == 0 or y == 0:
#     print("A least one of numbers is zero")

# print("The number is positive") if x > 0 \
#     else print("the number is negative") \
#     if x < 0 \
#     else print("Zero")

# for loop

# for x in range(10):
#     print(x)

# for x in (1, 2, 3, 7, 9):
#     print(x)

# for x in range(2,10):
#     print(x)
# y = 2
# for x in range(11, 2, -2):
#     print(x)
#
# print(x)

# for x in "Hello":
#     print(5, end="")

# for x in range(len(y)-1):
#     print(y[x], end=" ")
# print()
# print(y[1])

# [print(i, end=' ') for i in y]

# for i in y:
#     if i != " ":
#         print(i, end='')

y = "welcome to the jungle"
x = "The life is wonderful"


# for i in y:
#     if i in x:
#         if i == " ":
#             continue
#         print(i, end="")

# y = "Welcome to the jungle"
# x = "The life is Wonderful"
#
# for i in y:
#     if i in x:
#         if i == " " or i.isupper():
#             continue
#         print(i, end="")

# *
# size = 5
# for i in range(size+1):
#     print(" "* (size - i) * 2 ,"* " * i,  end="")
#     print()

# price = float(input("Enter the price: "))
# quantity = 10
# print(f"Full price is:  {price * quantity:.2f}")
#
# print(f"The price is {price:.2f}")

# price = 59
# txt = f"It is very {'Expensive' if price > 50 else 'Cheap'}"
# print(txt)

# def myconverter(x):
#     return x * 0.3048
#
#
# txt = f"The plane is flying at a {myconverter(30000)} meter altitude"
# print(txt)

# lst = []
#lst = list([])
# lst = list((1, 4, 7))
# lst = [1, 4, 7]
# print(lst)
# print(id(lst))
# x = lst
# print(id(x))
# print(x)
# x[0] = 5
# print(lst)
# print(id(x))

fruit = ["apple", "banana", "cherry"]
# print(fruit)
fruit1 = ["apple", "cherry", "banana", "orange", "plum"]
# print(fruit == fruit1)

# fruit2 = ["apple", ["cherry", "banana"]]
# print(fruit2)
# print(fruit2[1][1])
# print(fruit1[-2])
# print(fruit1[1:4])
# print(fruit1[:4])
# print(fruit1[4:])
# print(fruit1)
# print(fruit1[::2])
fruit3 = fruit1[::1]
# print(fruit3 is fruit1)
# print(fruit3 == fruit1)
# print(id(fruit1))
# print(id(fruit3))

# fruit4 = fruit1[:]
# print(fruit4 is fruit1)
# print(fruit4 == fruit1)
# fruit5 = fruit1
# print(fruit5 is fruit1)
# print(fruit5 == fruit1)

# st = "Hello world"
# ls = list(st)
# print(ls)
# ls2 = st.split()
# print(ls2)

# sl = slice(2, -1)
# print(fruit1[sl])

# ws1 = "https://google.com"
# ws2 = "https://facebook.com"
# ws3 = "https://cnn.com"
# ws4 = "https://bbc.com"
# domain = slice(8, -4)
# print(ws1[domain])
# sites = [ws1, ws2, ws3, ws4]
# for i in sites:
#     print(i[domain])
#
# print(type(domain))
# print(domain)

# print(fruit1)
# print(id(fruit1))
# fruit1[2] = "melon"
# print(fruit1)
# print(id(fruit1))
# name = "Alexander"
# print(id(name))
# name = "alexander"
# print(id(name))

# print(fruit1)
#
# fruit1[1:3] = ["melon", "cherry"]
# print(fruit1)
#
# fruit1[1:2] = ["watermelon", "kiwi"]
# print(fruit1)

# fruit1[1:3] = ["banana"]
# print(fruit1)
#
# fruit1.insert(2, "kiwi")
# print(fruit1)

# fruit1.append("papaya")
# print(fruit1)

tropical = ["papaya", "pineapple", "kiwi", "mango"]
# fruit1.extend(tropical)
# print(fruit1)

tropical.extend(fruit1)
# print(tropical)
#
# tropical.remove("mango")
# print(tropical)

# tropical.pop(0)
# print(tropical)
# print(id(tropical))
# for i in tropical:
#     if "kiwi" == i:
#         tropical.remove("kiwi")
# print(tropical)

# del tropical[0]
# print(tropical)

#tropical.clear()
# print(tropical)
# print(id(tropical))
# tropical.append([1, 2, [3, 4]])
# print(tropical)
# # tropical[6][2].clear()
# del tropical[6][2]
# print(tropical)

# print(fruit1)
# newfruit = [] # put in this list all fruits from fruits1 that have "a" in the name
# for x in fruit1:
#     if "a" in x:
#         newfruit.append(x)
# print(newfruit)
#
# new = [x for x in fruit1 if "a" in x]
# print(new)
#
# new1 = [x for x in fruit1]
# print(new1)

# newlist = [x for x in range(50)]
# print(newlist)

# a = [x**2 for x in range(1,11)]
# print(a)

# b = [x for x in range(21) if x % 2 == 0]
# print(b)

print(fruit1)
# newfruit = [x.upper() for x in fruit1]
# print(newfruit)

# new1 = ["hello" for x in fruit1]
# print(new1)

# new2 = [("Hello "+x) for x in fruit1]
# new2 = [f"Hello {x}" for x in fruit1]
# print(new2)

# new2 = [x if x != "banana" else "melon" for x in fruit1]
# print(new2)

fruit1.sort(reverse=True)
# print(fruit1)
# print(sorted(fruit1))
# print(fruit1)
# fruit1.reverse()
# print(fruit1)
# print(fruit1[::-1])

fruit_copy = fruit1.copy()
# print(fruit_copy == fruit1)
# print(fruit_copy is fruit1)

# lst1 = ["a", "b", "c"]
# lst2 = [1, 2, 3]
# lst3 = lst1 + lst2
# print(lst3)
# lst4 = lst2 + lst1
# print(lst4)
# print(lst1)

# lst = fruit1 + tropical
# print(lst)
# cnt = lst.count("cherry")
# print(cnt)

# Pascal triangle

# x = int(input("enter the size of triangle, not to big: "))
# pascal = []
# for i in range(x):
#     pascal.append([1] + [0]*x)
# #print(pascal)
#
# for i in range(1,x):
#     for j in range(1, i + 1):
#         pascal [i][j] = pascal [i-1][j] + pascal [i-1][j-1]
# #    print(pascal)
# for i in range(x):
#     print(" " * (x-i), end="" )
#     for j in range(i+1):
#         print(pascal[i][j], end=" ")
#     print()
#
#
lst = [2, 3, 4, 5, 10, 13, 17, 18, 19, 6, 11, 23, 11, 9]


# def is_prime(n):
#     if n <= 1:
#         return False
#     if n <= 3:
#         return True
#     if n % 2 == 0 or n % 3 == 0:
#         return False
#     i = 5
#     while i**2 <= n:
#         if n % i == 0 or n % (i + 2) == 0:
#             return False
#         i += 6
#     return True

# for num in lst:
#     if is_prime(num):
#         print(num, end=", ")

# print([num for num in lst if is_prime(num)])

# print(lst)
# print(*lst)

# numbers = [2, 1, 3, 4, 7]
# more_num = [*numbers, 11, 16, 34]
# print(more_num)
# print(*numbers)

# import random
# ls = []
# n = 20
# for x in range(n):
#     ls.append(random.randint(1,100))
# print(ls)
#
# cnt = 0
# for i in range(1, len(ls) - 1):
#     if ls[i] < ls[i - 1] and ls[i] < ls[i + 1]:
#         cnt += 1
# print(cnt)

# print("hello")
# id()

# def hello():
#     print("Hello world")
#
# # for i in range(10):
# #     hello()
#
# f = hello
# f()
# print(type(f))
# print(f is hello)

# x2 = 5
# def greeting(x):
#     print(f"hello, {x}")
#     x2 = 3
#     #print(x2)
# greeting("Alexander")
# print(x2)

# def hello(name="Noname"):
#     if name == "Noname":
#         print(f"Hello, nobody")
#     else:
#         print(f"Hello, {name}")
#
# p = hello()
# print(p)

# def max2(x, y):
#     if x > y:
#         return x
#     return y
#
#
# print(max2(-3, 7))
#
#
# def max3(x, y, z):
#     return max2(y, max2(x, z))
#
# print(max3(0, -12, 1))

# def my_country(country="Israel"):
#     print("I am from " + country)
#
# my_country("Sweden")
# my_country("Norway")
# my_country()
# my_country("India")


# def myfun(x=5, y=50):
#     print(f"x = {x}")
#     print(f"y = {y}")
# myfun(3, 7)

# def call_child(*kids):
#     print(f"The youngest child is {kids[-1]}")
#     print("the list of the kids is: ")
#     for i in kids:
#         print(i)
#     print(kids)
# call_child("Emily", "Mary", "Sam", "Bob") # tuple

# def my_food(food):
#     for x in food:
#         if isinstance(food, str):
#             print(x, end="")
#         else:
#             print(x, end=", ")
#     print()
#
# fruits = ["apple", "banana", "cherry"]
# my_food(fruits)
# veg = ("tomato", "cucumber", "potato", "corn")
# my_food(veg)
#
# st = "The live is strawberry"
# my_food(st)
# #### 31.07.2024
# a, b, c = 1, 2, 3
# print(a, b, c)
#
# a, b, *c = 1, 2
# print(a, b, c)
# print(c)

# def test(a, b, c):
#     print(a)
#     print(b)
#     print(c)
#
# test(c=1, a=8, b=3)

# def greet(greeting, *names, **emotions):  # *args  **kwargs
#     for n in names:
#         message = f"{greeting}, {n}! "
#         if "mood" in emotions:
#             message += f"You fill {emotions["mood"]}. "
#         if "look" in emotions:
#             message += f"You is very {emotions["look"]}."
#         print(message)
#
# greet("Hello","Alexander", "Kate", "Viki", mood="happy", look="beautiful" )
# greet("Hello", "John", "Mary")
#
# for i in "Alex", "Michael", "Andrew":
#     print(i)

# lst = [-4, 0, 10, 4, 5, 13, 30,38, 59, 1, 21, 15]
#
# def avg(iter):
#     summ = 0
#     for i in iter:
#         summ += i
#     return summ / len(iter)
#
# print(avg(lst))


# number = 30000
# def prime_fast(num):
#     """Проверяет, является ли число простым."""
#     if num <= 1:
#         return False
#     if num <= 3:
#         return True
#     if num % 2 == 0 or num % 3 == 0:
#         return False
#     i = 5
#     while i * i <= num:
#         if num % i == 0 or num % (i + 2) == 0:
#             return False
#         i += 6
#     return True
#
# def list_of_primes_fast(num):
#     ls = []
#     for i in range(1,num+1):
#         if prime_fast(i):
#             ls.append(i)
#     return ls
#
# def prime_classic(num):
#     flag = False
#     if num == 1:
#         return False
#     elif num > 1:
#         for i in range(2, num):
#             if (num % i) == 0:
#                 flag = True
#                 break
#         if flag:
#             return False
#         return True
#
# def list_of_primes_classic(num):
#     ls = []
#     for i in range(1,num+1):
#         if prime_classic(i):
#             ls.append(i)
#     return ls
#
# import datetime
#
# start = datetime.datetime.now()
# list_of_primes_fast(number)
# stop = datetime.datetime.now()
# print(f" Fast algorithm: {stop - start}")
#
# start = datetime.datetime.now()
# list_of_primes_classic(number)
# stop = datetime.datetime.now()
# print(f" Classic algorithm: {stop - start}")

# import math
# from math import *
# from math import sqrt, pow
# #print(dir(math))
# print(sqrt(9))
# print(pow(2,3))

# import factorial
# print(factorial.fact(900))

# def greet():
#     print("Hello, world!")

# greet = lambda : print("Hello, world!")
# greet()

# greet_user = lambda name : print(f"Hi there,{name}")
#
# greet_user("Alexander")

# (lambda name:print(f"Hi there,{name}")) ("John")

# x = lambda x: x+1
# print(x(5))

# print((lambda x: x**2) (3))
# x = "Hello world"
# lst = [5, 14, (lambda x: x**2) (len(x)), "Hello"]
# print(lst)

lst = [2, 5, 6, 76, 45, 36, 32, 55, -3, 0]

# def get_filter(a, filter=None):
#     if filter is None:
#         return a
#     res = []
#     for x in a:
#         if filter(x):
#             res.append(x)
#     return res
#
# even = get_filter(lst, lambda x: x % 2 == 0)
# print(even)
# pos = get_filter(lst, lambda x: x > 0)
# print(pos)
# import sys, math
lst = [2, 5, 6, 76, -45, 36, 32, 55, -3, 0, 13, 43]
# n = map(lambda x: x*x, lst)
# print(list(map(lambda x: x*x, lst)))
# print(m)
# print(list(m))
# print(sys.getsizeof(m))
# print(sys.getsizeof(lst))
# lst = [2, 5, 6, 76, 45, 36, 32, 55, -3, 0]
# print(lst)
# mult3 = filter(lambda x: x % 2 == 0, lst)
# print(mult3)
# print(list(mult3))
# new_lst = (lambda x: x*x,)

# def func(var):
#     letter = ["a", "e", "i", "o", "u"]
#     if var in letter:
#         return True
#     return False
# letter = ["a", "e", "i", "o", "u"]
# txt = "Hello, world, you are beautiful"
#
# func = lambda var:var in letter
# filt = filter(func, txt)
# print(list(filt))

#================================

# seq = [0, 1, 2, 3, 4, 5, 8, 13]
#
# even = filter(lambda x: x % 2 == 0, seq)
# print(list(even))
# odd = filter(lambda x: x % 2 != 0, seq)
# print(list(odd))

# lst = [[1, 's', 2], [3, 'a', 1], [-2, 'W', 0]]
# print(sorted(lst))
# print(sorted(lst, key=lambda lst: lst[2]))

# str1 = "We very happy to meet the neighbours and congratulate them with a ne year"
# lst_str = str1.split()
# print(lst_str)
# # print(sorted(lst_str, key=lambda lst_str: len(lst_str)))
# print(int(sum(list(map(len, lst_str)))/len(lst_str)))

# t = (3,13,32,-3)
# print(type(t))
# print(len(t))
# print(t[2])

# t2 = (3, "Hello", [2, 5, True], 7)
# print(t2)
# print(id(t2))
# # print(type(t2))
# # print(len(t2))
# print(id(t2[2]))
# t2[2][2] = False
# print(t2)
# print(id(t2))
# t2[2].append(199)
# print(t2)
# t2[2].clear()
# print(t2)
# print(id(t2[2]))

# lst = [1, 2, 3]
# fruits = tuple(("apple", "banana", "lemon"))
# tp = tuple(lst)
# print(tp)
# print(fruits)

# n = "Hello Israel"
# n = tuple(n)
# print(n)
# print(n[3:8:2])

# fruits = ("apple", "banana", "cherry")
# print(type(fruits))
# (green, yellow, red) = fruits
# print(green, red)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
# print(type(fruits))
# (green, yellow, *red) = fruits

# for x in fruits:
#     print(x)

# for i in range(len(fruits)):
#     print(fruits[i])
#
# tpl1 = ('a', 'b', 'c')
# tpl2 = (1, 3, 6, 9)
# tpl3 = tpl1 + tpl2
# tpl1 *= 2
# print(tpl1)

# tpl = (1, 3, 4, 7, 8 ,5, 4, 6, 8, 5)
# x = tpl[6:].index(4)
# print(x)
#
# x = tpl.count(9)
# print(x)

# lst = [x**2 for x in range(1,11)]
# print(lst)
# print(lst.__sizeof__())
# tup = tuple(x**2 for x in range(1,11))
# print(tup)
# print(tup.__sizeof__())

# lst = [(4, 5), (2, 3), (6, 7), (2, 8)]
# print(lst)
# ln = len(lst)
# for i in range(ln):
#     for j in range(ln -i -1):
#         if lst[j][0] + lst[j][1] > lst[j+1][0] + lst[j+1][1]:
#             lst[j], lst[j+1] = lst[j+1], lst[j]
#
# print("\nThe answer is ")
# print(lst)

# import datetime
#
# l = list(range(80_000_001))
# t = tuple(range(80_000_001))
# # print(l)
# # print(t)
# # print(l.__sizeof__())
# # print(t.__sizeof__())
#
# start = datetime.datetime.now()
# for i in range(len(t)):
#     a = t[i]
# end = datetime.datetime.now()
# print(end - start)
#
# start = datetime.datetime.now()
# for i in range(len(l)):
#     a = l[i]
# end = datetime.datetime.now()
# print(end - start)

set1 = {2, 3, 2, 3, 4, 3, 3, 2, True, 4.3 , 5, 1, 0, 0, 0, "Hello", (1, 3, 5), [3, 4,5]}
print(set1)
# print(set1[2])
