#py 02-beautifulsoup.py
from bs4 import BeautifulSoup
html="<html><body><h1>Welcome to PYTHON</h1></body></html"
soup=BeautifulSoup(html,"html.parser")
#print(soup.h1.text)

html1="""<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>pw devops</title>
</head>

<body>
    <h2>Pw skills</h2>
    <p class="info">Welcome to the class of web automation</p>
     <p class="demo">Welcome to the another class demo automation</p>
     <a href="www.pantu.com">Pantu site</a>
     <a href="www.daisyui.com">daisyui</a>
</body>

</html>"""

soup=BeautifulSoup(html1,"html.parser")
print("title:",soup.title.text)
print("heading:",soup.h2.text)
for link in soup.find_all("a"):
    print("Link: ",link.get("href"))
print("paragraph:",soup.find("p",class_="demo").text) #class wala <p> dhunda hai