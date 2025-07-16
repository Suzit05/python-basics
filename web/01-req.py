# py 01-req.py

import requests

url="https://www.facebook.com"
response=requests.get(url)

#check the respnse  code
if response.status_code==200:
    print(response.status_code)
    print(response.text[:500])
else:
    print(f"failed to fetch the response {response.status_code}")