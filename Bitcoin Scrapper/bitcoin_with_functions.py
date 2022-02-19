from xml.dom.minidom import Element
import requests
from bs4 import BeautifulSoup as bs

url = F"https://gadgets.ndtv.com/cryptocurrency#pfrom=home-gadgets_header-globalnav"

response = requests.get(url)
soup = bs(response.text,"lxml")

def mon():
  Money = soup.find_all('div',"_flx crynm") 
  for Coin_Name in Money:
    print(Coin_Name.text.strip()) 

def tue():
  Rate = soup.find_all('td',"_rft _tdpr") 
  for Price in Rate:
   print(Price.text.strip())

def wed():  
  new2 = soup.find_all('div',"_sortval") 
  for Change_Top in new2:
   print(Change_Top.text.strip())

def thur(): 
  new3 = soup.find_all('span',"_chper") 
  for Change_Bottom in new3:
   print(Change_Bottom.text.strip())


mon() 
tue()
wed()
thur()