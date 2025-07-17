#py task1.py
#combine req and BeautifulSoup

from bs4 import BeautifulSoup
import requests

url="https://www.google.com"
response=requests.get(url)
if(response.status_code==200):
    print(response.status_code)
    #print(response.text[:500])
    soup=BeautifulSoup(response.text, "html.parser")
    print("\n Links:")
    for link in soup.find_all("a"):
        print("Link: ",link.get("href"))
    print("title: ", soup.title.text)
    print("\n Images:")
    for image in soup.find_all("img"):
        print("Image: ",image.get("src"))
    
else:
    print("Invalid url")

