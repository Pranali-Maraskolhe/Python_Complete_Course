# 8. Write a python function to print multiplication table of a given number.

def table(n):
    for i in range(1, 11):
        print(f"{n} X {i} = {n*i}")


num1 = int(input("Enter Number = "))
table(num1)