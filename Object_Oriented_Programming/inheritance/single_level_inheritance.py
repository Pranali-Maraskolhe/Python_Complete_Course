class Employee:
    company = "ITC"
    def show(self):
        print(f"Company is {self.company}")


class Programmer(Employee):
    company = "ITC Infotec"

    def showLanguage(self):
        print("Language is Python")


a = Employee()
b = Programmer()

print(b.company)
b.show()
b.showLanguage()  # Output: Language is Python