from hashlib import new
from urllib import response
import requests
from bs4 import BeautifulSoup as bs

search_name = input('Enter Baby Starting Name:')

url = F"https://parenting.firstcry.com/baby-names/starting-with/{search_name}/"

res = requests.get(url)
soup = bs(res.text,"lxml")
names = soup.find_all("div",{"class":"baby-name M15_42"})
# meanings = soup.find_all("span",{"class":"nm-ming R12_9e"})
with open(search_name +".txt", "a") as file:
 for div in names:
     Names = div.text
  

     file.write(f"{Names}")
     file.write("\n")
     print(f"{Names}")


    





