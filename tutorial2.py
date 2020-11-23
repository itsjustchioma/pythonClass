# magicnumber = 26

# # to find magic number

# for n in range(101):
#     if n is magicnumber:
#         print(n, "Is the magic number")
#         break
#     else:
#         print(n)

# for x in range(101):
#     if x % 4 == 0:
#         print(x, "is divisible by 4")
#     else:
#         print(x)

# print("Enter length: ")
# length = input()
# print("Enter breadth: ")
# breadth = input()
# if length == breadth:
#     print("It's a square")
# else:
#     print("It's not a square")


# print("Enter a number1: ")
# number1 = input()
# print("Enter a number2: ")      
# number2 = input()               
# if number1 > number2:
#     print(number1, "is the greatest number")                  
# elif number1 < number2:
#     print(number2, "is the greatest number")                   
# else:
#     print("The two numbers are equal")    
# 


# print("Enter quantity: ")
# quantity = int(input(">"))
# if quantity*100 == 1000:
#     print("Cost is", ((quantity*100)-(.1*quantity*100)))
# else:
#     print("Cost is", quantity*100)

# print("Enter salary: ")
# salary = int(input(">"))
# print("Years of service: ")
# Years = input()
# if Years> "5":
#     print("Net bonus is", (salary*.5))
# else:
#     print("No bonus")

# print("Enter first age: ")
# first = int(input(">"))
# print("Enter second age: ")
# second = int(input(">"))
# print("Enter third age: ")
# third = int(input(">"))
# if first >= second and first >= third:
#     print("The first is the oldest")
# elif second >= first and second >= third:
#     print("The second is the oldest")
# elif third >= first and third >= second:
#     print("The third is the oldest")
# elif first == second == third:
#     print("All are equal")


# print("Enter mark: ")
# mark = int(input(">"))
# if mark < 25:
#     print("F")
# elif mark >= 25 and mark < 45:
#     print("E")
# elif mark >= 45 and mark < 50:
#     print("D")
# elif mark >= 50 and mark < 60:
#     print("C")
# elif mark >= 60 and mark < 80:
#     print("B")
# else:
#     print("A")


# print("Enter a number: ")
# number = int(input(">"))
# if number < 0:
#     print(number * -1)
# else:
#     print(number)

# print("Number of classes held: ")
# held = int(input(">"))
# print("Number of classes attended: ")
# attended = int(input(">"))
# attendance = attended/held*100
# print("Do you do medical_course? ")
# medical_course = int(input(">"))
# if medical_course == "Y":
#     print("You're allowed")
# # print("Attendance is", attendance)
# # if attendance >=75:
# #     print("Permitted to sit in the exam hall")
# elif attendance
# else:
#     print("Not permitted to sit in exam hall")

# print("Do you take a medical course?: ")
# medical = int(input("Yes or No: "))
# if medical == Yes:
#     print("Sit")
# else:
#     print("Don't sit")

# print("Enter year: ")
# year = int(input(">"))
# if year % 4 == 0:
#     print("Ths is a leap year")
# # elif year % 400 == 0:
# #     print("This century year is a leap year")
# else:
#     print("This is not a leap year")

print("Age: ")
Age = int(input(">"))
print("sex: M or F? ")
sex = int(raw_input())
print("Marital status: Y or N? ")
marital = int(input(">"))
if sex == "F":
    print("You will work in urban area only")
elif sex == "M" and Age > 20 and Age <=40:
    print("You may work anywhere")
elif sex == "M" and Age > 40 and Age <= 60:
    print("You may work in urban areas only")
else:
    print("ERROR")
