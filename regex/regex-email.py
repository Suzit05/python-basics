# py regex-email.py

import re

text="User's email is rahil@gmail.com"

match=re.search(r"[a-zA-Z0-9_%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z.-]{2,}", text)
#in regex "." ko "\." aise likhege
#qk "." mtlb ek character hota hai

if match:
    print("Email is found:", match.group())