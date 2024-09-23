class Employee():
    language = "Python"
    salary = 12000000

    # automatically call as the we exceute the program
    # It will always exceuted whenever we create an object 
    def __init__(self, name, language, salary): 

        self.name = name
        self.language = language
        self.salary = salary
        print("Object creation")

    def getinfo(self):
        print(f"The language {self.language} and salary is {self.salary}")


p1 = Employee("Pranali", "Javascript", 15000000)
print(p1.name, p1.language, p1.salary)
p1.getinfo()

p2 = Employee("Nishant", "Python", 2500000000)
print(p2.name, p2.language, p2.salary)

