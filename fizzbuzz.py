# write a code that checks if a number is a multiple of 3, 5 or both.
# it should print fizz, buzz or fizzbuzz respectively

variable = int(input("Enter a number: "))
if variable % 3 == 0 and variable % 5 == 0:
    print("Fizzbuzz")
elif variable % 3 == 0:
    print("Fizz")
else:
    print("Invalid")