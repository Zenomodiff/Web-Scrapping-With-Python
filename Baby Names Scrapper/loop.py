from hashlib import new
from urllib import response
import requests
from bs4 import BeautifulSoup as bs
import re

array = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# search_name = input('Enter Baby Starting Name:')

for i in array:
    search_name = (i)

    url = F"https://parenting.firstcry.com/baby-names/starting-with/{search_name}/"

    res = requests.get(url)
    soup = bs(res.text,"lxml")
    anchor1 = soup.find_all("div",{"class":"baby-name M15_42"})
    anchor2 = soup.find_all("span",{"class":"nm-ming R12_9e"})
    with open(search_name +".txt", "a") as file:

     for i,(name,meaning) in enumerate(zip(anchor1,anchor2)):
      name = name.text.strip()
      meaning = meaning.text.strip() 
      file.write(f"{name}--{meaning}")
      file.write("\n") 
      print(f"{name}--{meaning}")