# Write a program to input eight numbers from the user and display all the unique
# numbers (once).

s = set()

for i in range(8):
    num = int(input("Enter a number: "))
    s.add(num)

print(s)