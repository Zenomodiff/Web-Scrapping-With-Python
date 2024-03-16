import requests
from bs4 import BeautifulSoup as bs
import time

small_link = "https://www.timeanddate.com"

url = "https://www.timeanddate.com/worldclock/"
req = requests.get(url)
soup = bs(req.content, "html.parser") 

data1 = soup.find_all("tr")[1:]
for i in data1:
    l = i.find("a")['href']
    Country = i.find("a").text.strip()
    Link = small_link + l
    print(f"{Country} -- {Link}")
    with open("data.txt","a")as f:
        f.write(f"{Country} -- {Link}")
        f.write("\n")

