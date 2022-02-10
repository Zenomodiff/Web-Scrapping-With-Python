import requests
import pyshorteners
from bs4 import BeautifulSoup as bs

for i in range(1,10):
    page_number = (i)


    url = F"https://www.ndtv.com/latest/page-{page_number}"

    response = requests.get(url)
    sh = pyshorteners.Shortener()
    soup = bs(response.text,"lxml")

    header = soup.find("div",{"class":"row s-lmr mt-10"})
    for news in header:
      title_news = news.find_all("h2",{"class":"newsHdng"})
      for heading in title_news:
         with open("news.txt", "a") as file:
          tag = heading.find("a")
          Title = tag.text
          Dev = tag["href"]
          x = sh.tinyurl.short(Dev)
          file.write(f"{Title}--{x}")
          file.write("\n") 
          print(f"{Title}--{x}")

