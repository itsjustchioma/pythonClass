# def maximum(a, b, c):
#     list = [a, b, c]
#     return max(list)

# Driven code
# a = 10
# b = 1
# c = 12
# print(max(a, b, c))

# def function1():
#     print("ahhhh")
#     print("ahhhhhhhhh 2")
# print("this is outside the function")
# function1


# def function2(x):
#     return 2*x
# a = function2(3)
# print(a)
# b = function2(4)
# print(b)
# c = function2(5)
# print(c)

# def function3(x, y):
#     return x + y
# e = function3(1, 2)
# print(e)

# def function4(x):
#     print(x)
#     print("still in this function")
#     return 3*4
# f = function4(4)

# name1 = "YK"
# height_m1 = 2
# weight_kg1 = 90

# name2 = "YK's sister"
# height_m2 = 1.8
# weight_kg2 = 70

# name3 = "YK's brother"
# height_m3 = 2.5
# weight_kg3 = 160
# def bmi_calculator(name, height_m, weight_kg):
#     bmi = weight_kg / (height_m ** 2)
#     print("bmi: ")
#     print(bmi)
#     if bmi < 25:
#         return name + " is not overweight"
#     else:
#         return name + " is overweight"
# result1 = bmi_calculator(name1, height_m1, weight_kg1)
# result2 = bmi_calculator(name2, height_m2, weight_kg2)
# result3 = bmi_calculator(name3, height_m3, weight_kg3)
# print(result1)
# print(result2)
# print(result3)

# # def avg_score(numlist):
# # avg = sum(numlist) / len
# # avg_status(chioma)

import statistics
data = [11, 21, 11, 19, 46, 21, 19, 29, 21, 18, 3, 11, 11]
x = statistics.mean(data)
print(x)

# app.py
def avg_score(numlist):
    avg = sum(numlist) / len(numlist)
    return avg
print("The average of the list is", round(avg_score([19, 21, 46, 11,18]), 2))


