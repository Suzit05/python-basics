# py 10.ReadData.py

with open("details.txt", "r") as file:  #with open("file name", "operation") as "name to this function as whole"
    content=file.read()
    print(content)