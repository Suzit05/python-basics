# py regex-mobile.py

import re

pattern=r"^[6-9]\d{9}$" 
#[6-9] — first digit must be 6, 7, 8, or 9
#\d{9} — followed by exactly 9 digits

mobile_num="9876543451"

if re.match(pattern,mobile_num):
    print(f"{mobile_num} is valid")
else:
    print("not a vaild mobile number")