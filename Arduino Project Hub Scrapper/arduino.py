import requests
import pyshorteners
from bs4 import BeautifulSoup as bs

for i in range(265,266):
    page_number = (i)

    url = F"https://create.arduino.cc/projecthub?category=&difficulty=&page={page_number}&part_id=&sort=trending"

    response = requests.get(url)
    sh = pyshorteners.Shortener()
    soup = bs(response.text,"lxml")
    anchor1 = soup.find_all("div",{"id":"content"}) 
    for project in anchor1:
     project1 = project.find_all("div",{"class":"mobile-scroll-row-item"})
    for proj in project1:
        projj1 = proj.find("img", alt=True)
        projj2 = proj.find("a")
        Name = projj1['alt']
        Link = projj2["href"]
        url2 = F"https://create.arduino.cc{Link}"
        X = sh.tinyurl.short(url2)
        print(f"{page_number}--{Name}--{X}")
        with open("arduino_projects.txt", "a", encoding="utf-8") as file:
         file.write(f"{page_number}--{Name}--{X}")
         file.write("\n") 