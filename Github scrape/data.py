import requests
from bs4 import BeautifulSoup as bs

url = "https://github.com/Zenomodiff/Web-Scrapping-With-Python"
req = requests.get(url)
soup = bs(req.content, "html.parser") 
https = "https://github.com"

data1 = soup.find_all("div", {"class": "Layout-main"})
l = soup.find_all("div", {"class": "Box-sc-g0xbh4-0 izjvBm"})

seen_data = set()

for i in data1:
    j = i.find_all("div", {"class": "react-directory-truncate"})
    for k in j:
        Data = k.find('a').text.strip()
        small = k.find('a')["href"]
        if Data not in seen_data:
            seen_data.add(Data)
            Link = https + small
            print(f"{Data} -- {(Link)}")
            with open("data.txt","a")as f:
                f.write(f"{Data} -- {(Link)}")
                f.write("\n")