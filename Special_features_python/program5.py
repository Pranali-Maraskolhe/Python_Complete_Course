# 5. Store the multiplication tables generated in problem 3 in a file named Tables.txt.


num = int(input("Enter a Number: "))
with open("multipy.txt", "w") as f:
    for i in range(1, 11):
        f.write(f"{i} X {num} = {num*i} \n")