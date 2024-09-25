class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a =1

class Programer(Employee):
    def __init__(self):
        print("Constructor of Programmer")
    b = 2

class Manager(Programer):
    def __init__(self):
        super().__init__()  # Use to access method of super class in the derived class
        print("Constructor of Manager")
    c = 3

# ob1 = Employee()
# print(ob1.a)

# ob2 = Programer()
# print(ob2.a, ob2.a)

ob3 = Manager()
print(ob3.a, ob3.b, ob3.c)

