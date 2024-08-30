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

# 07/07/2024

# set2 = {3,7, *[5,6, 1]}
# print(set2)
# set3 = {3,7, *[5,6], *{7, True, "abc"}}
# print(set3)
#
# set4 = {*["a","b","c","d","e"]}
# print(set4)

# string1 = "abracadabra"
# set1 = set(string1)
# print(set1)
# string2 = "/".join(set1)
# print(string2)

# thisset = {"apple", "banana", "cherry"}
# # print(len(thisset))
# print("apple" in thisset)
#
# print(thisset)
# for x in thisset:
#     print(x)

# s = {4, 3, 7, True, -6, 23, 6, 5, print(5)}
# print(max(s))
# print(min(s))
# print(sum(s))
# print(all(s))
# print(any(s))
# print(s)
# print(id(s))
# s.add(10)
# print(id(s))
# print(s)
# for i in range(1,11):
#     s.add(i)
# {s.add(i) for i in range(1,15)}
# print(s)
# {lambda s: s.add(i) for i in range(100,105)}
# print(s)
# s2 = {4, 5, 7, -100, -200, -300}
# s3 = {4, 5, 7, 5, 7, 7, 0, -4, -45}
# print(s2.issubset(s3))
# print(s2.issuperset(s3))
# print(s2 <= s3 <= s2)
# print(s3)
# print(sorted(s3))
# s3.update(s2)
# print(s3)
# s3.update(list(range(30,40)))
# print(s3)
# s3 |= s2
# print(s3)

# s3.remove(-300)
# print(s3)
# s3.discard(-300)
# print(s3)
# s3.discard(-200)
# print(s3)
# print(s3.pop())
# print(s3)
# print(s3.pop())
# print(s3)

# print(id(s3))
#print(s3.clear())
# print(s3)
#del s3
#print(s3)
# print(f"s2= {s2}")
#s5 = s3.union(s2)
# print(s5)

#s5 = s2.intersection(s3)
# s5 = s2 & s3
# print(s5)
# s6 = s2.difference(s3)
# print(s6)
# s7 = s3.difference(s2)
#s7 = s3 - s2
#print(s7)
# print(s3)
# s3.difference_update(s2)
# s3.intersection_update(s2)
# print(s3)
# s5 = s3.symmetric_difference(s2)
# s5 = s3 ^ s2
# print(s5)
# s3.symmetric_difference_update(s2)
# print(f"s3= {s3}")
# s3 ^= s2
# print(s3)
# s3 = frozenset(s3)
# print(s3)
# s5 = s3.difference(s2)
# print(s5)
# s3 = set(s3)

from time import perf_counter_ns
# number = 20_000_000
# search = 19_999_000
# from factorial import measure
#
# st = set(range(1, number+1))
# ls = list(range(1, number+1))
#
# print(measure(st,search))
# print(measure(ls,search))

size =1
# for i in range(size + 1):
#     print(" "*(size-i), "* " * i, end="")
#     print()

# for i in range(1, size+1):
#     if i == 1:
#         print(" "* (size-i-1), "* ", end="")
#     elif i == size:
#         print("* "*i, end="")
#     elif i == 2:
#         print(" "*(size-i-1), "* *", end="")
#     else:
#         print(" "*(size-i-1), "*"," "*(2*i-5), "* ", end="")
#     print()

# 11.07.2024

# Dictionaries -

mydict = {'brand': 'Ford', 'color': 'blue'}
# print(type(mydict))
mydict['model'] = 'Mustang'
# print(mydict)
# print(id(mydict))
# mydict['color'] = 'red'
# print(mydict)
# mydict.update({'year': 1980})
# mydict.update({True: True})
# print(mydict)
# mydict.update({(1,2,3): [1, 2,[3,[4,{5,6,(6,9, True)}]]]})
# print(mydict)

# person = dict(name='John', age=40, country='Ireland')
# print(person)
# prs = dict([(2, 4), (6, 8)])
# print(prs)
# print(len(person))

# print(person['age'])
# print(person.keys())
#
# print(person.values())
#
# print(person.items())
#
# for i,j in person.items():
#     print(j, i, sep= ' = ')

# print(person.pop('age'))
# print(person)
#
# print(person.popitem())
# print(person)

# del person['name']
# print(person)

# lst = [1,2,3,4]
# del lst[1]
# print(lst)

# person.clear()
# del person
# print(person)
# print(id(person))
# person2 = person.copy()
# print(id(person2))
# person4 = person
# print(id(person4))
# x = tuple("str")
# y = tuple(x)
# print(x is y)
#
# person2 = dict(person)
# print(person2 is person)

# family = {
#     'child1': {
#         'name': 'John',
#         'age': 10
#     },
#     'child2': {
#         'name': 'Mary',
#         'age': 7
#     },
#     'child3': {
#         'name': 'David',
#         'age': 3,
#         'isYounger': True
#     }
# }
# import pprint

# pprint.pprint(family)
# family['child3']['name'] = 33
# print(family['child3']['name'])

# x = {'day1', 'day2', 'day3'}
# newdict = dict.fromkeys(x)
# print(newdict)
# newdict['day1'] = 1000
# print(newdict)

# print(mydict)
#
# x = mydict.setdefault("year", 1965)
# print(x)
# mydict.setdefault("year", 1985)
# print(mydict)

# keys = ('a', 'b', 'c', 'd')
# values = (1, 2, 3, 4, 5)
#
# # method 1: zip - function
# new_dict = dict(zip(keys, values))
# print(new_dict)
#
# # Method 2 dictionary comprehension
#
# dict2 = {keys[i] : values[i+1] for i in range(len(keys)) }
# print(dict2)

# st = "12 31 4 53 6 7 4 90 8 7 56 3 42 0"
# dictionary = {int(x)*3: int(x)**2 for x in st.split() if int(x) % 2 == 0}
# print(dictionary)

# string2 = "Hello, dear friends. How are you today? Hope you enjoy our lesson, have a good evening"
#
# def create_symbols_dict(str2):
#     symbol_dict = {}
#     for symbol in str2:
#         if symbol == ' ':
#             continue
#         if symbol in symbol_dict:
#             symbol_dict[symbol] += 1
#         else:
#             symbol_dict[symbol] = 1
#     return symbol_dict
#
# result = create_symbols_dict(string2.lower())
# print(result)

# x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# print(x)
# print(sorted(x))
# print(sorted(x.items()))
# print(sorted(x.values()))
# print({k: v for k, v in sorted(x.items(), key=lambda it: it[1])})
#
# print(dict(sorted(x.items(), key=lambda it: it[1])))

my_dict = {'a': 2, 'b': 3}
def func(a, b):
    return a + b
print(my_dict)
print(*my_dict)
print(*my_dict.values())
print(func(**my_dict))

# 14.08.2024
# 1-5
# mark = input("choose your mark (1-5): ")
#
# d_mark = {'1': 'Very bad!',
#           '2': 'Not good!',
#           '3': 'May be better',
#           '4': 'Good work',
#           '5': 'Perfect! You are the best!'}
# if mark in d_mark:
#     print(d_mark[mark])
# else:
#     print('Invalid choice')

# words = {}
# print("this is the dictionary that you create yourself, just enter a word")
# print('for exit press "q" and "enter"')
# while True:
#     s = input("your word: ")
#     if s == 'q':
#         break
#     if s in words:
#         print(f"word {s} is translated as {words[s]}")
#     else:
#         print("type the translation in russian ",s)
#         words[s] = input()

# translate
# table = {119: 103, 121: 102, 117: None} # 119 - 'w', 103 - 'g' ,121 - 'y', 102 - 'f', 117 - 'u'
#
# target = "weeksyourweeks"
#
# print("the string before translation is: ", target)
# print("the string after translation is: ", target.translate({}))

# student_list = {'S  001': ['Ma th', 'Scie nce'], 'S   002': ['Math', 'Eng lish']} # ASCII code of " " is 32
# print(student_list)
# print(id(student_list))
# student_list = {x.translate({32: None}):[y[0].translate({32: None}), y[1].translate({32: None})]
#                 for x, y in student_list.items()}
# print(student_list)
# print(id(student_list))

# fruits = ["apple", "orange", "avocado", "kiwi", "banana"]
# basket = ["apple", "apricot", "avocado", "kiwi", "melon"]
#
# new = [i for i in fruits if i in basket if i.startswith('a')]
# print(new.__sizeof__())
# new2 = []
# for x in fruits:
#     if x.startswith('a'):
#        if x in basket:
#            new2.append(x)
# print(new2.__sizeof__())
# print(new)
# print(new2)
# for i in fruits:
#     for y in basket:
#         if i == y :
#             if i[0]=='a':
#                 print(i)

# tuple comprehension - does not exist
# () in range from 1 to 10

# lst = [i**0.5 for i in range (100000)]
# print(lst.__sizeof__())
#
# gnr = tuple(float(f'{i**0.5:.3f}') if i**0.5 % 1 != 0 else int(i**0.5) for i in range (10))
# print(gnr.__sizeof__())
# print(gnr)
# print(tuple(gnr).__sizeof__())
# import pprint
# apple_names = ['apple', 'green apple', 'pineapple']
# pprint.pprint({i:{i: len(i) for i in apple_names} for i in apple_names})

# 18.08.2024

# [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# {'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}
# colors = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# def grouping(col):
#     result = {}
#     for k, v in col:
#         result.setdefault(k, []).append(v)
#     return result
#
#
# dct_grp = grouping(colors)
# print(dct_grp)

# dictionary = {'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
# # {'C1': [], 'C2': [], 'C3': []}
# #
# def clr(dct):
#     for key in dct:
#         # print(key)
#         dct[key].clear()
#     return dct

# print(clr(dictionary))
# original_dict = {'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
# dict = {x: y.clear() for x,y in original_dict.items()}
# print(dict)

# dct = {'a': 1, 'b': {'c': {'d': {}}}}

# map
# dep = 1
# def dict_depth(d):
#     global dep
#     for v in d.values():
#         if isinstance(v, dict):
#             dep += 1
#             return dict_depth(v)
#     return dep
#
#
# print(dict_depth(dct))



# Homework3
# print()
# print('Homework 3')
# original_dict = {'a': 1, 'b': {'c': {'d': {}}}}
# count_dict = original_dict.copy()
# count = 0
#
# while count_dict != {}:
#     count += len(count_dict.keys())
#     for key in count_dict.keys():
#
#         if isinstance(count_dict[key], dict):
#             count_dict = count_dict[key]
# print('The deep of the dictionary is: ', count)

#lst = [30, 10, 15, 20, 30, 40, 50, 30, 30, 20, 1, 2, 3, 4, 5, 0, 20]
# lst = [30, 20, 80, 40, 50, 30, 30, 20, 1, 2, 3, 4, 5, 10, 20]
#
# def count_increase(a):
#     count = 1
#     countlist = []
#     for i in range(len(a) - 1):
#         if a[i] < a[i + 1]:
#             count = count + 1
#         else:
#             countlist.append(count)
#             count = 1
#     return max(countlist)
#
#
# print('Length of the longest increasing sub-sequence:-', count_increase(lst))

# def myFish(guppies, zebras, bettas):
#     print(f"I have {guppies} guppy fish")
#     print(f"I have {zebras} zebra fish")
#     print(f"I have {bettas} betta fish")


# fish = {'guppies': 2, 'zebras': 5, 'bettas': 10, 'salmon': 12, 'tuna': 8, 'shark': 2}
#
# def myFish(**fish):
#     for key, value in fish.items():
#         print(f"I have {value} {key}")
#
# myFish(**fish)

# st = {i*i for i in range(1,11) if i != 5 and i*i % 10 in (1, 4, 9)}
# print(st)
# orig = 'aeiou'
# crypto = '12345'
# table = str.maketrans(orig,crypto)
# # print(table)
# text = "this is a test"
# encrypted_text = text.translate(table)
# print(encrypted_text)
# table2 = str.maketrans(crypto, orig)
# decrypted_text = text.translate(table2)
# print(decrypted_text)

dict1 = {'a': 10, 'b': 20, 'c': 30, 'w': 120}
dict2 = {'a': 5, 'b': 15, 'd': 25, 'Hello': 5}
# # dict3 = {}
# # {k: v for k,v in dict1 if k}
# # for k,v in dict1.items():
# #     dict3[k] = v
# dict3 = dict1.copy()
# for k, v in dict2.items():
#     if k in dict3:
#         dict3[k] += v
#     else:
#         dict3[k] = v
#

# from collections import Counter
# dict3 = Counter(dict1) + Counter(dict2)
# print(dict(dict3))

# coord = {'x': 2, 'y': 0, 'z': 1}
# tpl = (2, 0, 1)
# coord2 = {k: k*k for k in range(1_000_000)}
# tpl2 = tuple(k*k for k in range(1_000_000))
# print(hash(tpl2))
# tpl2 = (1,3)
# print(hash(tpl2))
# tpl2 = (1,3.1)
# print(hash(tpl2))

# print(coord2)
# print(coord2.__sizeof__())
# print(tpl2.__sizeof__())

# 21.08.2024


# dict5 = {'a': 5, 'b': 32, 'c': 10}
#
# rev_dict = {k: v for v, k in dict5.items()}
# print(rev_dict)
#
# lst = [1, 2, 3, 4]
#
# new_dict = current = {}
# print(id(new_dict))
# print(id(current))
# for num in lst:
#     current[num] = {}
#     print(f"current before {id(current)}")
#     current = current[num]
#     print(f"current after {id(current)}")
#     # print(current)
#     # print(id(current))
#     print(new_dict)
#     # print(id(new_dict))
# # print(new_dict)

# Z
# size = 7
# for sym in range(size):
#     if sym == size - 1 or sym == 0:
#         print('*' * size)
#     else:
#         print(' ' * (size - sym - 2), '*')

# 1
# 22
# 333

# print(str((i)*i+'\n' for i in range(1,10)), sep="")
# for i in range(1,10): print(str(i)*i)

# lst = [1, 2, 3, 1, 2, 4, 5, 6, 3, 7, 5, 6, 4, 8, 7, 8]
#
# def first_non_repeated(l):
#     cnt = {}
#     for i in l:
#         if i in cnt:
#             cnt[i] += 1
#         else:
#             cnt[i] = 1
#
#     for i in l:
#         if cnt[i] == 1:
#             return i

# print(first_non_repeated(lst))

# marks = (98, 80, 85, 100)
# print(marks[2])

from collections import namedtuple

# Marks = namedtuple('Marks', 'Physics Chemistry Math English')
# #print(Marks)
# marks1 = Marks(98, 80, 85, 100)
# print(marks1)
# mrc_t = (98, 80, 85, 100)
# mrc_names_t = ('Physics', 'Chemistry', 'Math', 'English')
# dct = {'Physics': 98, 'Chemistry': 80, 'Math': 85, 'English':100}
# print(dct)
#
# print(marks1.__sizeof__())
# print(dct.__sizeof__())
# print(mrc_t.__sizeof__() + mrc_names_t.__sizeof__())
# t_t = (('Physics', 98), ('Chemistry', 80), ('Math', 85), ('English',100))
# print(t_t.__sizeof__())

# Marks_d = namedtuple('Marks2', dct)
# # print(Marks_d(**dct))
#
# marks2 = Marks_d(88, 82, 93, 79)
# print(marks2)
# print(marks2[2])
# print(marks2.English)
# print(marks1.Chemistry)
# marks2[2] = 100  returns error due to immutable type

# lst = ['Physics', 'Chemistry', 'Math', 'English']
# Marks = namedtuple('Marks', lst)
# lst2 = [60, 37, 82, 75]
# marks3 = Marks._make(lst2)
# print(marks3)
# print(id(marks3))
# marks3 = marks3._replace(Chemistry=99)
# print(marks3)
# print(id(marks3))

# Student = namedtuple('Any_Student', ['name', 'age', 'marks'])

# def calc_avg(student):
#     total = sum(student.marks)  # total sum of grades
#     avg = total/len(student.marks)
#     return avg
#
#
# student1 = Student(name='Alice', age=22, marks=[98, 92, 69])
# print(f"Average grade of {student1.name} is {calc_avg(student1):.2f}")
#
#
# from math import pow
# print(pow(3,4))
# print(3**4)

# Person = namedtuple('AnyPerson', 'name age height')
# person1 = Person('John', 35, 180)
# print(person1)
# ExtPerson = namedtuple('ExtPerson', [*Person._fields, 'weight'])
# person2 = ExtPerson('Michael', 40, 175, 75)
# print(person2)
# Person = namedtuple('AnyPerson', 'name position height')
# person1 = Person('John', 35, 180)
# print(person1)
# print(person2)

# pers_dict = person2._asdict()
# print(pers_dict)
# p = "Hello, world"
# print(globals())

# for name, value in zip(person1._fields, person1):
#     print(name, " <--> ", value)

# 25.08.2024

# dict1 = {'c1': 'Red', 'c2': 'Green', 'c3': False}
# print("Original dict: ", dict1)
# dict1 = {key: value for (key, value) in dict1.items() if value}
# print(dict1)
#
# marks = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80], 'Math': [95, 80, 84, 79]}
#
# # [{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language': 84}, {'Science': 95, 'Language': 80}]
#
# def list_of_dicts(d):
#     # get the key (subject) from the origin dictionary
#     keys = d.keys()
#     values = zip(*[d[k] for k in keys])
#  #   print(*values)
#     result = [dict(zip(keys, v)) for v in values]
#     return result
#
# # list_of_dicts(marks)
# print(list_of_dicts(marks))
#
# lst1 = [1,2,3]
# lst2 = ['a','b','c']
# lst3 = list(zip(lst1,lst2,lst2))
# print(lst3)

nestedlist = [ [1, 2, 3], 4, ("Ten", "Twenty", "Thirty"), {4, 5}, [1.1,  1.0E1, 1+2j, 20.55], 3.142]
# flat = []
# for sublist in nestedlist:
#     for element in sublist:
#         flat.append(element)
#
# print(flat)

# from collections.abc import Iterable
#
# lst2 = []
# for sub in nestedlist:
#     if isinstance(sub,(Iterable)):
#         lst2.extend(sub)
#     else:
#         lst2.append(sub)
#
# print(lst2)

# flat2 = [element for sublist in nestedlist for element in sublist]

# print(flat2)

# flow / wolf   'forty five' / 'over fifty'


# l = [x*2 for x in range(5)]
# print(*l)
# print(l)
# lt = (x*2 for x in range(5))
# li = iter(l)

# print(list(li))
# print(list(li))
# print(list(lt))
# print(list(lt))
# print(l[2])
# print(len(l))
# print(len(li))
# print(li[2])
# for i in li:
#     print(i)
# for i in li:
#     print(i)
# st = {3,7, 5, 3,8}
# print(st)
# print(st)


def my_num():
    a = 1
    while True:
        yield a
        a += 4
my = my_num()
# print(my)
# print(next(my))
# print(next(my))
# print(next(my))

# print(my.__sizeof__())

# def func(n):
#     res = []
#     cnt = 0
#     while cnt < n:
#         res.append(cnt)
#         cnt += 1
#     return res
# ls = func(100_000_000)
# def func2():
#     cnt = 0
#     while True:
#         yield cnt
#         cnt += 1
# ls2 = func2()
#
# print(ls[1000])
#
# for i in range(1000):
#     next(ls2)
# print(next(ls2))

# from math import sqrt
#
# sq = [sqrt(x) for x in range(1_000_000)]
# sq_gen = (sqrt(x) for x in range(1_000_000))
# # print(sq)
# # print(list(sq_gen))
# print(sq[965])
# for i in range(965):
#     next(sq_gen)
# print(next(sq_gen))
#
# print(sq.__sizeof__())
# print(sq_gen.__sizeof__())

# map

# s = "0123s567895665!72"
# ls = []
# for i in s:
#     ls.append(int(i))
# print(ls)
# print(dir(map))
# print(list(map(str, s)))

str1 = "Hello world! The Python is the best programming language"
# print(str1.split())
ls = [ len(i) for i in str1.split()]
print(ls)
print(ls.__sizeof__())
length = (map(len, str1.split()))
print(list(length))
print(length.__sizeof__())

# 28.08.2024
lst = ['forty five', 'evil', 'vile', 'restful', 'fluster']

# def characterCounts(s):
#     counts = {} # empty dictionary
#     # renew the dict for ech symbol in the row
#     for ch in s:
#         if ch in counts:
#             counts[ch] += 1
#         else:
#             counts[ch] = 1
#     return counts
#
# # check if the strings are anagrams or not
# lst2 = []
# for st in range(len(lst)):
#     characterCounts(lst[st])
#     for st2 in range(1, len(lst)):
#         if characterCounts(lst[st2]) == characterCounts(lst[st]):
#             lst2.append(lst[st])
#             lst2.append(lst[st2])
#
# print(lst2)

# lst = ['forty five', 'over fifty','can', 'evil', 'vile', 'live', 'restful', 'fluster']
#
# def group_anagrams(strs):
#     result = {}
#     for s in strs:
#         sorted_string = ''.join(sorted(s))    # here we get sorted string
#         if sorted_string in result:
#             result[sorted_string].append(s)
#         else:
#             result[sorted_string] = [s]
#     return list(result.values())
#
# print(group_anagrams(lst))

# el = input("Enter the symbol: ")
#
# def del_from_tuple(tpl, elem):
#     if elem in '0123456789':
#         elem = int(elem)
#     return tuple(y for y in tpl if y != elem)
#
# print(del_from_tuple((1, 2, 3, 4, 4, 3, 5, 'a',3), el))


# Student = namedtuple('Student', 'name age mark city')
# students = (
#    Student('David', '23', 71, 'New York'),
#    Student('Mark', '21', 79, 'LA'),
#    Student('Elizabeth', '24', 91, 'Denver'),
#    Student('Robert', '22', 72, 'Chicago'),
#    Student('Samantha', '21', 61, 'Boston'),
#    Student('Jack', '21', 87, 'Cleveland'),
#    Student('Arthur', '23', 58, 'Seattle')
# )
#
# def good_students(stud):
#     total = 0
#     for student in stud:
#         total += student.mark
#     avg = total // len(stud)
#     good_mark_stud = [student.name for student in stud if student.mark >= avg]
#     print("Students ", ", ".join(good_mark_stud), "learn good this semester!")
# good_students(students)

# n, m = map(int,input().split())
# matrix = [ [0]*m for _ in range(n)]
# # print(matrix)
# dx, dy, x, y = 0, 1, 0, 0
#
# for i in range(1, n*m +1):
#     matrix[x][y] = i
#     if matrix[(x+dx) % n][(y+dy) % m]:
#         dx, dy = dy, -dx
#     x += dx
#     y += dy
#     # print(matrix)
# # print(matrix)
# for line in matrix:
#     print(*(f"{i:<3}" for i in line), sep='')

# s = map(str, input().split())
# print(*s)
# lst3 = [[0]*4]*5
# print(lst3)

string2 = "Hello world the languages of programming are different"
# print(string2.split())
#length = map(len, string2.split())
# print(length)
# each row should run separately because length is iterator
# longest = max(map(len, string2.split()))
# summ = sum(map(len, string2.split()))
# lst3 = list(map(len, string2.split()))
# print(longest)
# print(summ)
# print(lst3)
# print(next(length))
# print(next(length))
# print(next(length))
# print(next(length))

# ls = [i**2 for i in range(1, 10000000)]
# print(ls[8])

# ls2 = map(lambda j: j**2, range(1,10000000))
#
# start = datetime.datetime.now()
# for i in range(len(ls)):
#     ls[i] *=3
# print(datetime.datetime.now() - start)
#
# start = datetime.datetime.now()
# ls2 = map(lambda j: j*3, ls2)
# print(datetime.datetime.now() - start)
# start = datetime.datetime.now()
# ls[8]
# print(datetime.datetime.now() - start)
# start = datetime.datetime.now()
# list(ls2)[8]
# print(datetime.datetime.now() - start)
# print(ls)
# print(list(ls2))

# num1 = [1, 2, 3]
# num2 = [10, 20, 30]
# num3 = [5, 6, 7]
# res = map(lambda n1, n2, n3: (n1+n2)*n3, num1, num2, num3)
# print(tuple(res))
# actions = ['eat', 'sleep', 'read']
# res = map(list, actions)
# print(*res)

# car_dict = {'a': 'Mercedes', 'b': 'BMW', 'c': 'Ferrari', 'd': 'Porsche'}
# # BMW_2024
# print(id(car_dict))
# # car_dict = dict(map(lambda x: (x[0], x[1]+'_2024'), car_dict.items()))
#
# for k, v in car_dict.items():
#     car_dict[k] += '_2024'
#
# print(car_dict)
# print(id(car_dict))
