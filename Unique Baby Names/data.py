from urllib import response
import requests
from bs4 import BeautifulSoup as bs

for i in range(1,11):
    page_number = (i)
    url = f"https://nameberry.com/popular-names/unique/{page_number}"
    req = requests.get(url)
    soup= bs(req.content,"lxml") 
    data1 = soup.find("div",{"class":"w100pct"})
    for i in data1:
        j = i.find_all("a")
        for k in j:
            baby_name = k.find_all("span",{"class":"jsx-2400428389"}, limit=2)[-1].text.strip()
            print(baby_name)
            with open("data.txt","a", encoding="utf-8")as f:
                f.write(f"{baby_name}")
                f.write("\n")



