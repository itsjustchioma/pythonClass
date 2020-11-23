# A company decides to give bonus of 5% to employee if his/her year of service is more than five years 
# Ask user for their salary and year of service and print the net bonus amount 

print ("Enter Salary")
salary = input()
print ("Enter year of service")
yos = input()
if yos>5:
    print ("Bonus is",.05*salary)
else:
    print ("No bonus")