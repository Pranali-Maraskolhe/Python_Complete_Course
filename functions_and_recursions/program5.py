# 5. Write a python function to print first n lines of the following pattern:

# ***
# **
# *        - for n = 3


def pattern(rows):
 for x in range(rows, 0, -1):
    for y in range(1, x+1):
      print("*", end=" ")
    print()


pattern(3)