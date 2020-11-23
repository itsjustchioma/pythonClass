# take two inputs from user and check whether they are equal or not 

print("Mark scored: ")
scored = int(input(">"))
passing_mark = 35
if scored > passing_mark:
    print("You scored greater than the passing mark.")
elif scored < passing_mark:
    print("You scored less than the passing mark.")
else:
    print('You scored the passing mark')