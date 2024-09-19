lst = []

num = int(input("Enter the Number of Students: "))

for i in range(num):
    score = int(input(f"Enter Score {i}: "))
    lst.append(score)

print(lst)

lst.sort()
print(lst)