# 11. Write a python program to rename a file to “renamed_by_ python.txt.

# with open("old.txt", "r") as f:
#     content = f.read()

# with open("rename_old.txt", "w") as f:
#     f.write(content)

import os

os.rename("old.txt", "renamed_by_python.txt")  # Renames the file to