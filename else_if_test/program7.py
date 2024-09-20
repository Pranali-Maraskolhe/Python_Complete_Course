# 7. Write a program to find out whether a given post is talking about “Pranali” or not.

post = input("Enter the post: ")

if("Pranali".lower() in post.lower()):
    print("The post is talking about Pranali")

else:
    print("The post is not talking about Pranali")