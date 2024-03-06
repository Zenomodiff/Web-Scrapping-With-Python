from urllib import response
import requests
from bs4 import BeautifulSoup as bs

for i in range(6):
    page_number = i
    
    url = f"https://randomnerdtutorials.com/projects-esp32/{page_number}"

    req = requests.get(url)
    soup= bs(req.content,"lxml") 
    data1 = soup.find_all("div",{"class":"elementor-widget-container"})
    for i in data1:
       j = i.find_all("h2",{"class":"elementor-post__title"})
       for k in j:
          title = k.find("a").text.strip()
          link = k.find("a")['href']
          print(f"{title} --- {link}")
          with open("data.txt","a")as f:
            f.write(f"{title} --- {link}")
            f.write("\n")



