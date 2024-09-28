from functools import reduce

# Map Example
lst = [1, 2, 3, 4, 5]

square = lambda x : x*x

sqlist = map(square, lst)

print(list(sqlist))


# Filter Example

def even(n):
    if (n%2 == 0):
        return True
    return False


onlyeven = filter(even, lst)

print(list(onlyeven))

# Reduce function

def sum(a, b):
    return a + b

print(reduce(sum, lst))