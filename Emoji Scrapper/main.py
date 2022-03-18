import requests
from bs4 import BeautifulSoup as bs 

url = "https://unicode.org/emoji/charts/full-emoji-list.html"

res = requests.get(url)
soup = bs(res.text,"lxml")
try:
    anchor1 = soup.find_all("td",{"class":"chars"})
    for i in anchor1:
        Emoji = i.text
        print(Emoji)
        with open("data.txt",'a', encoding="utf-8")as f:
            f.write(Emoji)
            f.write('\n')
except:
    pass
