class Employee:
    language = "Python"
    salary = 120000


    # Self is use for acessing variable, attributes and methods of a defined class
    def get_info(self):
        print(f"The language is {self.language} and salary is {self.salary}")

    @staticmethod  #It is use as decorater here there is no need to pass all the object using self
    def greet():
        print("Hello, I am an employee")

p1 = Employee()
p1.language = "Javascript"
print(p1.language)  # Output: Python
print(p1.salary)    # Output: 120000
p1.get_info()
p1.greet()