# 5. Write a program which finds out whether a given name is present in a list or not.

names_lst = ["Nishant", "Pranali", "Rose", "Will", "Lucas"]

x = input("Enter your Name : ").capitalize()

if(x in names_lst):
    print("Name is present in the list")

else:
    print("Name is not present in the list")  # Output: Name is not present in