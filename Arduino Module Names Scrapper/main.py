import requests
from bs4 import BeautifulSoup as bs

for i in range(4):
    page_number = i

    url = (f"https://arduinomodules.info/page/{page_number}/")

    res = requests.get(url)
    soup = bs(res.text,"lxml")

    anchor1 = soup.find_all("div",{"class":"inside-article"})
    for i in anchor1:
        a = i.find("a")
        Name = a.text.strip()
        Link = i.find("a")['href']
        print(f"{Name} - {Link}")
        with open("data.txt","a")as f:
            f.write(f"{Name} - {Link}")
            f.write("\n")
