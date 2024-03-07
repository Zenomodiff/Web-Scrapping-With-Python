from urllib import response
import requests
from bs4 import BeautifulSoup as bs

for i in range(1,3):
    page_number = (i)

    url = f"https://editorial.rottentomatoes.com/guide/essential-comedy-movies/{page_number}"
    req = requests.get(url)
    soup= bs(req.content,"lxml") 
    data1 = soup.find_all("div",{"class":"row countdown-item"})
    for i in data1:
       Number = i.find("div",{"class":"countdown-index"}).text.strip()
       j = i.find_all("div",{"class":"article_movie_title"})
       for k in j:
           Name = k.find("a").text.strip() 
           Year = i.find("span",{"class":"subtle start-year"}).text.strip()
           Ratings = i.find("span",{"class":"tMeterScore"}).text.strip()
           Link = i.find('a')['href']
           print(f"{Number} -- {Name} -- {Year} -- {Ratings} -- {Link}")
           with open("data.txt","a")as f:
            f.write(f"{Number} -- {Name} -- {Year} -- {Ratings} -- {Link}")
            f.write("\n")
            


