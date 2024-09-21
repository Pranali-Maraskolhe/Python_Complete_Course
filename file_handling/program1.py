# 1. Write a program to read the text from a given file ‘poems.txt’ and find out
# whether it contains the word ‘twinkle’.

with open("poem.txt") as f:
    text = f.read()
    if 'twinkle' in text.lower():
        print("The word 'twinkle' is present in the file.")
    else:
        print("The word 'twinkle' is not present in the file.")