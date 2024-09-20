# 2. Write a python program using function to convert Celsius to Fahrenheit.

def  cel_farh(n):
    return (n * 9/5) + 32


n = int(input("Enter number to convert celsius to fahrenheit = "))

print(f"The result in Fahrenheit is = {int(cel_farh(n))}")