# 1. Write a program to open three files 1.txt, 2.txt and 3.txt if any these files are not
# present, a message without exiting the program must be printed prompting the same.

try:
    with open("txt1.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(e)

try:
    with open("txt2.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(e)

try:
    with open("txt3.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(e)


print("Thank You")