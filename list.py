numlist = [1, 30, 3, 40, 10]

def large(param: list):
    """This function takes in a list and returns the largest"""
    largest = 0
    for x in param:
        if x > largest:
            largest = x
    return largest
    
print(large(numlist))