# a = 2.5
# b = 19
# c = a * b
# print(c)

# print("   /|")
# print("  / |")
# print(" /  |")
# print("/___|")

# print("bube is a girl")

# character_name = "Ebube"
# character_age = 12
# print("There once was a man named " + character_name + ", ")
# print("He was " + character_age + "years old. ")

# character_name = "mike"
# print("He really liked the name " + character_name + ", ")
# print("but he didn't like being " + character_age + ". ")

# pie = "Giraffe Academy"
# print(pie.replace("Giraffe", "Elephant"))

# my_num = -5

# my_num = -5

# from math import *
# print(sqrt(3.7))    

# # IF-STATEMENTS 
# num = int(input("Enter a number: "))

# num = 28
# if num % 2 == 0:
#     print("Even number")
# else: 
#     print("Odd number")

# name = input("Enter your name: ")
# if name == "Vanessa":
#     print("All")
# elif name == "Chioma":
#     print("Machine Learning")
# elif name == "Charles":
#     print("Django")
# else:
#     print("Name not recognized")

# def my_function():
#     print("Hello from a function")

# def greet_user(name):
#     print(F"Hello {name}")


# # def my_function(fname):
# #     print(fname + )

# greet_user("Jessie")

# num = 100



# checck_odd_even(10)def checck_odd_even(num):
#     if num % 2 == 0:
#         print("Even number")
#     else: 
#         print("Odd number")


# def add(a, b):
#     return a+b
# sum = add(3, 4)
# print(sum)

# def is_even(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False
# print(is_even(3))

# def my_function(*kids):
#     print("The youngest child is " + kids[2])

# my_function("Emil", "Tobias", "Linus")

def maximum(a, b, c):
    if (a >= b) and (a >= c):
        largest = a 
    elif (b >= a) and (b >=c):
        largest = b
    else:
        largest = c
        
        return largest

# Driven code
a = 10
b = 14
c = 12
print(maximum(a, b, c))