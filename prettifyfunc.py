from bs4 import BeautifulSoup
import requests
url="https://internshala.com/chat/c-1753083/"
req=requests.get(url)
soup=BeautifulSoup(req.text,"html.parser")
print(soup.prettify())