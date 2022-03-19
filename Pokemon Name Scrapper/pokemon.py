import requests
from bs4 import BeautifulSoup as bs

url = f"https://www.pokemon.com/us/pokedex/"
response = requests.get(url)
soup = bs(response.text,"lxml")
anchor1 = soup.find_all("div",{"class":"container"}) 
for pok in anchor1:
 with open("pokemon.txt", "w",encoding="utf-8") as file:
    poke = pok.find_all("li")
    for pok1 in poke:
         poke1 = pok1.find("a")
         if(poke1!=None):
          file.write(poke1.text)
          file.write("\n")
          print(poke1.text)
          