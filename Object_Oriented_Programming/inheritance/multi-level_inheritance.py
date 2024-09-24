class Employee:
    company = "ITC"
    name = "Default name"
    def show(self):
        print(f"The name of the Employee is {self.name} and the company is {self.company}")

class Coder:
    language = "Python"
    def printLanguage(self):
        print(f"The language of the Coder is {self.language}")


class Programmer(Employee, Coder):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.company} and I am good with {self.language} language")

a = Employee()
b = Programmer()

b.show()
b.printLanguage()
b.showLanguage()  # This will print the company name from Programmer class and language from Coder