from urllib import response
import requests
from bs4 import BeautifulSoup as bs

url = "https://www.cosmopolitan.com/uk/worklife/a33367076/fun-facts-random/"
req = requests.get(url)
soup= bs(req.content,"lxml") 
anchor1 = soup.find("div",{"class":"standard-body"}) 

for new in anchor1:
    new1 = anchor1.find_all("ol",{"class":"body-ol"}) 
for new2 in new1:
      new3 = new2.find_all("li")
      for new4 in new3:
          with open("fun_fact.txt", "a") as file:
           new5 = new4.find('strong').text.strip()
           print(new5)
           file.write(f"{new5}")
           file.write("\n") 
           file.close()