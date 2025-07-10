# py 12.ReadData.py
import os
if os.path.exists("your.txt"):
    with open ("your", "r") as file:
        print(file.read())
else:
    print("file does not exist")