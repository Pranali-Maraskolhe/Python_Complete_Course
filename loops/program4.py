# 4. Write a program to find whether a given number is prime or not.

num = int(input("Enter Number = "))
count = 0


for i in range(1,num+1):
    if(num % i == 0):
        count += 1

if(count == 2):
    print(num,"is a prime number")
else:
    print(num,"is not a prime number")  # Output: 5 is not a prime