# 4. Write a program to filter a list of numbers which are divisible by 5.

lst = [i for i in range(1,26)]

def divisible_by_5(n):
    return n % 5 == 0

only_five = filter(divisible_by_5, lst)

print(list(only_five))