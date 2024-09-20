# 5. Write a program to find the sum of first n natural numbers using while loop.

num = int(input("Enter a number up to you want to print natural numbee = "))
sum = 0

for i in range(0,num+1):
    sum += i

print(f"The sum of Natural Number is = {sum}")