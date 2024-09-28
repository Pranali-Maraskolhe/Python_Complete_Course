# 4. Write a program to display a/b where a and b are integers. If b=0, display infinite by
# handling the ‘ZeroDivisionError’.

try:
    a = int(input("Enter a Number1: "))
    b = int(input("Enter a Number2: "))
    print(a/b)

except ZeroDivisionError as e:
        print("Error: Division by zero is not allowed.")

