# name = "jirawan"
# first_name = "jirawan"
# last_name = "chuapradit"
# age = 18
# birth = "25/01/2541"
# weight = 53
# hight = 164.5
# print()

# import datetime
#
# birth = '23/01/25'
# datetime_object = datetime.datetime.strptime(birth, '%y/%m/%d')
# print(datetime_object)
# print(type(datetime_object))
# birth = datetime_object.strftime('%d/%m/%Y')
# print(birth) # 25/01/2023


# from math import pi
# r = float(input ("Input the radius of the circle : "))
# area = pi * r**2
# print ("The area of the circle with radius " + str(r) + " is: " + str(area))

#
# age = int(input("Input your age: "))
#
# if age > 90:
#     print("you are too old too party, granny")
# elif age >= 18:
#     print("you are allowed to party")
# elif age > 0:
#     print("you are too young")
# else:
#     print("you are not born yet")


# ถ้า 0 ให้แสดงคำว่า you are not born yet


# age = int(input("Input your age: "))
#
# if age > 90:
#     print("you are too old too party, granny")
# elif age >= 18 and age <0 :
#     print("you are allowed to party")
# else:
#     print("you are not born yet")


# age = int(input("Input your age: "))
#
# if age > 90:
#     print("you are too old too party, granny")
# elif 18 <= age > 0:
#     print("you are allowed to party")
# else:
#     print("you are not born yet")


# score = float(input("score is "))
#
# if score >= 50:
#     if score >= 60:
#         if score >= 70:
#             if score >= 80:
#                 print("A")
#             else:
#                 print("B")
#         else:
#             print("C")
#     else:
#         print("D")
# else:
#     print("F")

# count = 0
# while count < 3:
#     print(count)
#     count = count + 1
#     print("hello Geek")

# n = 10
# for i in range(0,n):
#     print(i)
#
# fname = "jig"

# for i in fname:
#     print(i)


# def get_box_area(width, length, height):
#     box_area = width * height * length
#     print(box_area)
#
# get_box_area(30,20,10)
# get_box_area(width=10,length=20,height=10)


# def find_even_odd(num):
#     """find even or odd"""
#     if (num % 2) == 0:
#         ans = """{0} is Even""".format(num)
#     else:
#         ans = """{0} is Odd""".format(num)
#     return ans
#

# ans = find_even_odd(18)
# print(ans)


# def plus(a, b):
#     return a + b
#
#
# def minus(a, b):
#     return a - b
#
#
# def multiply(a, b):
#     return a * b
#
#
# def divide(a, b):
#     return a / b
#
#
# import calculator
# print(calculator.divide(1, 2))
#
# def get_circle_area(radius):
#     return 22 / 7 * (radius ** 2)
#
#
# def get_triangle_area(width, height):
#     return 1 / 2 * width * height
#
#
# def get_rectangle_area(width, height):
#     return width * height
#
#
# print(get_circle_area(10))
#

# age = 18
# print(age)
# print(type(age))


# var = 10
# print(var)
# # print its type
# print(type(var))
#
# var = 55
# print(var)
# print(type(var))
# var = "jirawan" # python is dynamic type
# print(var)
# print(type(var))
#
# var = 153.8
# print(var)
# print(type(var))

# a = 1
# b = 2
# # add
# ans = a + b
# print(ans)
# # sub
# ans = a - b
# print(ans)
# # multi
# ans = a * b
# print(ans)
# # divi
# ans = a / b
# print(ans)
# # mod
# ans = a % b
# print(ans)


# score = float(input("score is "))


# เช่น  jig 
# j
# i
# g

name = input("name: ")

print(name.lower())
fname = name.lower()
counter_1 = 0
counter_2 = 0

for letter  in fname:

    # a e i o u
    if letter == "a":
        counter_1 += 1
    elif letter == "e":
        counter_1 += 1
    elif letter == "i":
        counter_1 += 1
    elif letter == "o":
        counter_1 += 1
    elif letter == "u":
        counter_1 += 1
    else:
        counter_2+=1
print("สระ " + str(counter_1) + " พยัญชนะ " +str( counter_2))

