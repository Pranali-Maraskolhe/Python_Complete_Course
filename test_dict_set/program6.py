# If the names of 2 friends are same; what will happen to the program in problem
# 5?

friend = {}

for i in range(4):
    name = input("Enter Name: ")
    lan = input("Enter Language: ")
    friend[name] = lan
    friend.update({name: lan})

print(friend)