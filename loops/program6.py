# 6. Write a program to calculate the factorial of a given number using for loop.

fact = 1

num = int(input("Enter a number : "))

for i in range(1,num+1):
    fact = fact * i

print(f"Factorial of {num} is = {fact}")