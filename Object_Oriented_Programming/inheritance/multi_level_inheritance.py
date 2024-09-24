class Employee:
    a =1

class Programer(Employee):
    b = 2

class Manager(Programer):
    c = 3

ob1 = Employee()
print(ob1.a)

ob2 = Programer()
print(ob2.a, ob2.a)

ob3 = Manager()
print(ob3.a, ob3.b, ob3.c)

