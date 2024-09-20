# 9. Write a program to print the following star pattern.

# ***
# * * for n = 3
# ***

rows = int(input("Enter Number of rows: "))

for i in range(1, rows+1):
    if((i==1) or (i==rows)):
        print("*" * rows,end="")

    else:
        print('*',end="")
        print(" "* (rows-2),end="")
        print('*',end="")
    print("")

