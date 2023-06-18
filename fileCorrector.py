#
# namingCorrector.py
#
# Description: This program scans a directory and changes all filenames to lowercase and removes all whitespace
import os

# Empty Lists
dirList = []
newList = []

# Get the list of all files and directories
path = input(r"Enter the path of the folder: ")
print(f"Files in the directory: {path}")

# If it ends with a PDF extension, we append it to a new list
for file in os.listdir(path):
    if file.endswith(".pdf" or ".PDF"):
       dirList.append(file)

# find the . in a file extension
for filename in dirList:
    # If a file has more than one .
    if filename.count('.') > 1:
        # We use list comprehension to list all the positions where the . is found, then only add the last element
       lastDot = [pos for pos, char in enumerate(filename) if char == "."][-1]
       newList.append(filename[:lastDot].replace(" ", "_").replace(".", "_") + filename[lastDot:].lower())
    else:
        newList.append(filename.split('.')[0].replace(" ", "_") + '.' + filename.split('.')[1].lower())

# We run both lists parallel and change the old filename to the new
for x, y in zip(dirList, newList):
    print("Old: " + path + "/" + x, "New: " + path + "/" + y)
    os.rename(path + "/" + x, path + "/" + y)
