# 4. Write a recursive function to calculate the sum of first n natural numbers.

def sum_natural(n):
    if n == 1:
        return 1
    return n + sum_natural(n-1)


n = int(input("Enter Number = "))
print("Sum of first", n, "natural numbers is", sum_natural(n))