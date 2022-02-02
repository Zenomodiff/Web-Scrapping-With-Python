import requests
from bs4 import BeautifulSoup as bs

url = f"https://www.tomsonelectronics.com/collections/resistors"

r = requests.get(url)
soup = bs(r.text,"lxml")
anchor1 = soup.find_all("div",{"class":"product-group-vendor-name"})
anchor2 = soup.find_all("div",{"class":"product-price notranslate"})
with open("tomson.txt", "a") as file:

 for i,(name,sale) in enumerate(zip(anchor1,anchor2)):
     with open("tomson.txt", "a" ,encoding="utf-8") as file:
      name = name.text.strip()
      sale = sale.text.strip() 
      file.write(f"{name}--{sale}") 
      file.write("\n") 
      print(f"{name}--{sale}")