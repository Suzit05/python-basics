import requests

url="https://www.google.com"
response=requests.get(url)

if(response.status_code==200):
    print(response.status_code)
    print("Print Content:")
    print(response.text[:500])
else:
    print("Invalid url")