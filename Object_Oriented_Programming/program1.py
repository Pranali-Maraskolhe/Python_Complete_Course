# 1. Create a class “Programmer” for storing information of few programmers
# working at Microsoft.

class Employee:
    company = "Microsoft"

    def __init__(self, name, salary, pincode):
        self.name = name
        self.salary = salary
        self.pincode = pincode

emp1 = Employee("Pranali", 400000000, 2400024)
emp2 = Employee("Nishant", 80000000000, 1400025)

print(emp1.name, emp1.salary, emp1.pincode, emp1.company)
print(emp2.name, emp2.salary, emp2.pincode, emp2.company)