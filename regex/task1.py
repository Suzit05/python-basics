# py task1.py
import re

number=input("Enter your phone number with country code ex:91-2433...: ")
pattern=r"^\d{1,3}-[6-9]\d{9}$" 

#Use \d{1,3} to match country codes like 91, 001, 44, etc.


if re.match(pattern,number):
    print("valid mobile number")
else:
    print("not a valid mobile number")
