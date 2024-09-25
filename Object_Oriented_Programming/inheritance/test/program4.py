# 4. Write a class ‘Complex’ to represent complex numbers, along with overloaded
# operators ‘+’ and ‘*’ which adds and multiplies them.


class Complex:

    def __init__(self, i, j):
        self.i = i
        self.j = j

    def __add__(self, c2):
        return Complex(self.i + c2.i, self.j + c2.j)
    
    def __mul__(self, c2):
        real_part = self.i * c2.i - self.j * c2.j
        imag_part = self.i * c2.j + self.j * c2.i
        return Complex(real_part, imag_part) 
    
    def __str__(self):
        return f"{self.i} + {self.j}j"

    

c1 = Complex(1, 2)
c2 = Complex(3, 4)
print(c1 + c2)
print(c1 * c2)

