from bs4 import BeautifulSoup
import requests
url="https://sites.google.com/apssdc.in/lifecycleofasoftwarebuilding/days/day-8/"
req=requests.get(url)
soup=BeautifulSoup(req.text,"html.parser")
print(soup.find_all('h1'))