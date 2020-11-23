# Create a function called avg_score()that will accept scores of a user 
# and return the average  
# Create another functiom called check_status() that will accept the value return by 
# the avg_score function and decide if the user has passed or to redo the exam 

num = (40, 50, 60, 70, 80)
avg = sum(num)/len(num)
print(avg)

def avg_score(a, b, c, d, e, f, g):
    total = (a + b + c + d + e + g)
    avg = int(total / 7)
    percentage = (total / 7)* 100
    print(f"Your average score is {avg} ")
    if avg < 50 :
        print ("You have a low average score Redo exams")
    else:
        print("You have passed the exams")

avg_score(10, 20, 30, 40, 50, 60, 70)


