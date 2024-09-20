# 7. Write a program to print the following star pattern.

#   *
#  ***
# ***** for n = 3


rows = int(input("Enter a Number: "))

for i in range(1, rows+1):
    for j in range(1,rows-i+1):
        print(end=" ")

    for k in range(1, i+1):
        print("*", end=" ")

    print()

