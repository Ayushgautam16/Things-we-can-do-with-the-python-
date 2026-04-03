# CRUD operation in file handling 
from pathlib import Path

def readfileandfolder():
    path = path('')
    item = list(path.rglob('*'))
    for i, items in enumerate(items):
        print(f"{i+1}: {items}")
    

def createfile():
    readfileslandfolder()
    name = input("please tell your file name: ")
    p = Path(name)
    with open(p,"w") as fs:
        data = input("what you want to write in this file")

print("press 1 to create the file")
print("press 2 to create the file")
print("press 3 to create the file")
print("press 4 to create the file")

check = int(input("enter the response u want to enter: "))

if check ==1:
    createfile()