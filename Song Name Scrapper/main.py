import requests
from bs4 import BeautifulSoup as bs

array = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for alpha in array:

    url = F"https://www.azlyrics.com/{alpha}.html"

    response = requests.get(url)
    soup = bs(response.text,"lxml")
    anchor1 = soup.find_all("div",{"class":"col-sm-6"}) 
    for i in anchor1:
        song = i.text
        print(song)
        with open(f"{alpha}.txt",'a', encoding="utf-8") as f:
            f.write(song)
