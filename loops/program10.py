# 10. Write a program to print multiplication table of n using for loops in reversed
# order.


n = int(input("Enter number of rows = "))

for i in range(10, 0, -1):
    print(f"{n} X {i} = {n*i}")