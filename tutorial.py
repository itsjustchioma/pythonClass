# tuna = 5
# bacon = 56
# print(bacon + tuna) 


# firstname = "Robert "
# a = firstname * 5
# print(a)

# index = 2
# word = "snake"
# length =len(word)
# while index < length:
#     print(word[index])
#     index += 5


# a = "This is orange juice"
# print('orange' in a.split)

# a = "Robert Brett Roser"
# a = a.split()
# b = a[0][1]+". "+a[1][0]+". "+a[2]
# print(b)

# a = ['a','e','i','o','u','A','E','I','O','U',' ']
# b = "Hello, have a good day"
# for i in b:
#     if i not in a:
#         b = b[:b.index(i)]+b[b.index(i)+1:]
# print(b)

# a = "This is an umbrella"
# a = a.split()
# maxx = a[0]
# max_len = len(a[0])
# for i in a:
#     if len(i)>max_len:
#         max_len = len(i)
#         maxx = i
# print(maxx)
# #similarly find minimum


# a = raw_input()
# #a[:] will give the whole string 
# print(a[:])
# #a[::-1] -1 is step. It will reverse the string
# print(a[::-1])
# print(a == a[::-1])
# #There are a lot of other ways to solve this problem


# user = "Oluebubechukwu"
# count = 0
# for i in user:
#     count = count + 1
# print(count)

# players = [29, 58, 66, 71, 87]
# players[:] = []
# print(players)

# name = "Lucy"

# if name is "Bucky":
#     print("Hey there bucky")
# elif name is "Lucy":
#     print("Waddup Luc dawg")

foods = ["bacon", "tuna", "ham", "sausages", "beef"]
for f in foods[:2]:
    print(f)
    print(len(f))


