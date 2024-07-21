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
print(fruit1)
print(fruit1[::2])
fruit3 = fruit1[::1]
print(fruit3 is fruit1)
print(id(fruit1))
print(id(fruit3))