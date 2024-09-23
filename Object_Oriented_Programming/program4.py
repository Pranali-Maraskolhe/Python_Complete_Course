# 4. Add a static method in problem 2, to greet the user with hello.

# 2. Write a class “Calculator” capable of finding square, cube and square root of a
# number.

class Calculator:
    def __init__(self, number):
        self.number = number

    def square(self):
        print(f"Square is {self.number*self.number}")
    
    def cube(self):
        print(f"Cube is {self.number*self.number*self.number}")
    
    def square_root(self):
        print(f"Square root is {self.number**1/2}")

    @staticmethod
    def greet():
        print("Hello everyone")
    
num = Calculator(4)
num.square()
num.cube()
num.square_root()
num.greet()
    