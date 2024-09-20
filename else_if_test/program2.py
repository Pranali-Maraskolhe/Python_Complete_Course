# 2. Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.

eng = int(input("Enter marks of English = "))
maths = int(input("Enter marks of Maths = "))
science = int(input("Enter marks of Science = "))

total = (100*(eng + maths + science))/300

if(eng >= 33 and maths >= 33 and science >= 33):
    if(total > 40):
        print("Student has passed")

else:
    print("Student has failed")  # This will print if the student has failed