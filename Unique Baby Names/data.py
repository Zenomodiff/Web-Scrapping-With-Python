import requests
from bs4 import BeautifulSoup as bs
import time

for page_number in range(1, 11):
    url = f"https://nameberry.com/popular-names/unique/{page_number}"
    req = requests.get(url)
    soup = bs(req.content, "lxml")
    data1 = soup.find("div", {"class": "w100pct"})

    if data1:
        j = data1.find_all("a")
        for index, k in enumerate(j, start=1):
            baby_name = k.find_all("span", {"class": "jsx-2400428389"}, limit=2)[-1].text.strip()
            gender = "girl" if index % 2 == 0 else "boy"
            print(f"{baby_name} is a {gender} name")
            with open("data.txt","a")as f:
               f.write(f"{baby_name} is a {gender} name")
               f.write("\n")