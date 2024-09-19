# Create an empty dictionary. Allow 4 friends to enter their favorite language as
# value and use key as their names. Assume that the names are unique.


friend = {}

for i in range(4):
    name = input("Enter Name: ")
    lan = input("Enter Language: ")
    friend[name] = lan

print(friend)