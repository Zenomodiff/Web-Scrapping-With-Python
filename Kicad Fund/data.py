from urllib import response
import requests
from bs4 import BeautifulSoup as bs

url = "https://www.kicad.org/download/windows/"
req = requests.get(url)
soup= bs(req.content,"lxml") 
data1 = soup.find("div",{"class":"fund-banner__text--light"})
data2 = soup.find("div",{"class":"fund-banner__bar-current-sum"})
fund1 = data1.text.strip()
fund2 = data2.text.strip()

print(f"{fund1} - {fund2}")

with open("fund.txt","a")as f:
            f.write(f"{fund1} - {fund2}")
            f.write("\n")




