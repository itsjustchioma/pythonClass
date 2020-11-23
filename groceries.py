# print("Enter your name: ")
# name = input(">")
# print(name)

beans = 300
rice = 500
beef = 750
egg = 200
chioma_money = 1500


food = input("What do you want: ")
if food.lower() == "beans":
    print(f"It costs {beans} NGN")
    ask = input("Buying? ")
    if ask.lower() == "yes":
        chioma_money = chioma_money - beans
        print(f"Ping Ping !!! You have {chioma_money} left in your account.")
elif food.lower() == "rice": 
    print(f"It costs {rice} NGN")
    ask = input("Buying? ")
    if ask.lower() == "yes":
        chioma_money = chioma_money - rice
        print(f"Ping Ping!!!You have {chioma_money} left in your account. ")
elif food.lower() == "beef":
    print(f"It costs {beef} NGN.")
    ask = input("Buying? ")
    if ask.lower() == "yes":
        chioma_money = chioma_money- beef
        print(f"Ping Ping !!! You have {chioma_money} left in your account.")
elif food.lower() == "egg":
    print(f"It costs {egg} NGN")
    ask = input("Buying? ")
    if ask.lower() == "yes":
        chioma_money = chioma_money - egg
        print(f"Ping Ping!!! You have {chioma_money} left in your account.")
else: 
    print("This item is currently unavailable. ")

