from urllib import response
import requests
from bs4 import BeautifulSoup as bs

url = "https://www.billboard.com/charts/greatest-hot-100-singles/"
req = requests.get(url)
soup= bs(req.content,"lxml") 
data1 = soup.find_all("div",{"class":"o-chart-results-list-row-container"})
for i in data1:
    song = i.find("h3",{"class":"c-title"}).text.strip()
    num = i.find("span",{"class":"c-label"}).text.strip()
    print(f"{num} -- {song}")
    with open("data.txt","a")as f:
            f.write(f"{num} -- {song}")
            f.write("\n")

