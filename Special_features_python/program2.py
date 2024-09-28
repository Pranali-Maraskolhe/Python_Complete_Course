# 2. Write a program to print third, fifth and seventh element from a list using enumerate
# function.

lst = [1, 2, 56, 9, 10, 56, 78, 63, 100]

for index, item in enumerate(lst):
    if index == 2 or index == 4 or index ==6:
        print(item)