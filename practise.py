import math
import time
from itertools import count
from math import floor
from time import sleep
from tkinter.font import names
from urllib.parse import uses_relative

# i havent done anthing on mah builtin functions so i learnt  few

#
# x = 5
# y = 39.3
# z = -6
#
# print(round(y))
# print(abs(z))
# print(pow(x, 3))
# print(max(x, y))
# print(min(x,y))
#
#
# name = input("What is your name ?   ")
# classIn = int(input("what class are you? "))
#
# if classIn >= 5:
#     print(f"hello {name} welcome to Teens class")
# else:
#     print(f"Hello {name} have a good day you are not eligibel yet for the promotion  ")



#calculator

# operator = input("Choose an operator (+, -, /, *): ")
# num1 = (float(input("Enter first number: ")))
# num3 = float(input("Enter second number: "))
#
# if operator == "+":
#     result = round(num1 + num3, 1)
#     print(result)
# elif operator == "-":
#     result = round(num1 - num3, 1)
#     print(result)
# elif operator == "/":
#     result = round(num1 / num3, 1)
#     print(result)
# elif operator == "*":
#     result = round(num1 * num3, 1)
#     print(result)
# else:
#     print(f"{operator}  is An invalid Choice ")


#weightcoversion

# quantifier = input("What is the measurement in (K/L)?: ")
# weight = int(input("What is the weight ?: "))
#
# if quantifier== "k":
#     result = round(weight * 2.20462, 3)
#     print(result)
# elif quantifier=="l":
#     result = round(weight / 2.20462 , 3)
#     print(result)
# else:
#     print(f"{quantifier} is Not Valid")
#
# user inpt validation
# user_name = input("Enter Your Name?")
#
# length = len(user_name)
# check_space = user_name.count(" ")
#
# if length > 12:
#     print(f"Hello {user_name} your name is invalid")
#     print(f"Please your Usernme should not be more than 12 character must not "
#           f"have a space and must not contain digits  ")
# elif check_space > 0:
#     print(f"Hello {user_name} your name is invalid")
#     print(f"Please your Username should not be more than 12 character must not "
#           f"have a space and must not contain digits  ")
# elif  user_name.isdigit():
#     print("Username cat be all digits ")
# else:
#     print(f"Hello {user_name} your name is validated ")
#
# # print(len(user_name))
# # print(user_name.count(" "))
# # print(user_name.isdigit())

#while loop to make an interest calculator formula is p * (1 + r/ 100) rqise to power of time

# principal = int(input("What Is Your Principal ? "))
# interest = int(input("What Is Your Interest Rate ? "))
# time = int(input("What Amount Of Time ? "))
#
# while True :
#     if principal < 0 and interest < 0 and time < 0 :
#         print("Input Cant Be Less Than Zero")
#         principal = int(input("What Is Your Principal ? "))
#     else:
#         break
#
# totalCompound = principal * pow ((1 + interest /100),time)
#
# print(f"Congrats The Final Interest Is ${totalCompound : .2f}")


#for loop
# print(dir(time))
# print(help(time))

for number in reversed(range(1,21)):
    if number % 2 == 0:
        print(f" {number} is an  even number ")
    else:
        print(f"{number } is an odd number ")