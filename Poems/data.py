from urllib import response
import requests
from bs4 import BeautifulSoup as bs

url = "https://earlybirdbooks.com/most-famous-poems"
req = requests.get(url)
soup= bs(req.content,"lxml") 
data1 = soup.find_all("div",{"class":"jsx-4993694ecb0ccbe1"})
for i in data1:
    j = i.find_all("div",{"class":"header"})
    for data in j:
        Title  = data.find("p").text.strip()
        k = i.find("div",{"class":"jsx-15b6b749792a397 sub-header"})
        By = k.text.strip()
        k = i.find("div",{"class":"jsx-15b6b749792a397 sub-header"})
        
        print(f"{Title} --- {By}")
        with open("data.txt","a")as f:
            f.write(f"{Title} --- {By}")
            f.write("\n")
