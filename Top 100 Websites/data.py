import requests
from bs4 import BeautifulSoup as bs

url = "https://ahrefs.com/blog/most-visited-websites/"
req = requests.get(url)
soup = bs(req.content, "lxml") 
data1 = soup.find("table", {"class": "tablepress"})
for i in data1:
    j = i.find_all("td", {"class": "column-1"})
    k = i.find_all("td", {"class": "column-2"})
    l = i.find_all("td", {"class": "column-3"})
    for td1, td2, td3 in zip(j, k, l):
        Numbers = td1.text.strip()
        Website = td2.text.strip()
        Views = td3.text.strip()
        print(f"{Numbers} -- {Website} -- {Views}")
        with open("data.txt","a")as f:
            f.write(f"{Numbers} -- {Website} -- {Views}")
            f.write("\n") 
