class Employee:
    a = 1

    @classmethod # using classmethod decorator we can access only class 
    def show(cls):
        print(f"The value of Class Variable is {cls.a}")


emp1 = Employee()

emp1.a = 20

emp1.show()
