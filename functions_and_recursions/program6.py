# 6. Write a python function which converts inches to cms.

def convert_inch_cm(length):
    return length * 2.54


length = float(input("Enter Length = "))

print(f"The length in cm = {round(convert_inch_cm(length),2)}")