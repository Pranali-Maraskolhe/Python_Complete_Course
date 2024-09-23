# 3. Create a class with a class attribute a; create an object from it and set ‘a’
# directly using ‘object.a = 0’. Does this change the class attribute


class Demo:
    a = 4


ob = Demo()

print(ob.a) # Print the class attribute

ob.a = 0

print(ob.a) # Print the instance attribute

print(Demo.a)
