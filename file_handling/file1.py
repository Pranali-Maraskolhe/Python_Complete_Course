
# fp = open("file1.txt")
# data = fp.read()
# print(data)
# fp.close()

# The same can be written using with statement like this:

with open("file1.txt") as f:
    print(f.read())