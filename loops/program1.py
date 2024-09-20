# 1. Write a program to print multiplication table of a given number using for loop.

num = int(input("Enter the number of which you want to print a table =  "))

for i in range(1,11):
    print(f"{num} * {i} = {num*i}")