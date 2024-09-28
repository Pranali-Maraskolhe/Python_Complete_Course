# 5. Write a program to find the maximum of the numbers in a list using the reduce
# function.


from functools import reduce

lst = [56, 21, 896, 36, 10004, 8, 9623]

def greater(a, b):
    if (a > b):
        return a
    else:
        return b
    

print(reduce(greater, lst))