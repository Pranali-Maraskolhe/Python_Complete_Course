# 3. Attempt problem 1 using while loop.
# 1. Write a program to print multiplication table of a given number using for loop.

num = int(input("Enter Number of which table you want to print = "))

i = 1

while(i<=10):
    print(f"{num} * {i} = {num*i}")
    i += 1

    