from xml.dom.minidom import Element
import requests
from bs4 import BeautifulSoup as bs

url = F"https://gadgets.ndtv.com/cryptocurrency#pfrom=home-gadgets_header-globalnav"

response = requests.get(url)
soup = bs(response.text,"lxml")

anchor1= soup.find_all('div',"_flx crynm") 
anchor2 = soup.find_all('td',"_rft _tdpr") 
anchor3 = soup.find_all('div',"_sortval")
anchor4 = soup.find_all('span',"_chper")

for i,(Coin_Name,Price,Change_Top,Change_Bottom) in enumerate(zip(anchor1,anchor2,anchor3,anchor4)):
    Coin = Coin_Name.text.strip()
    price = Price.text.strip()
    Top = Change_Top.text.strip()
    Bottom = Change_Bottom.text.strip()
    print(f"{Coin}Price == {price}, Today's_Top_Rate == {Top}, Today's_Bottom_Rate == {Bottom}")
    with open("bitcoin_data.txt", "a", encoding="utf-8") as file:
     file.write(f"{Coin}Price == {price}, Today's_Top_Rate == {Top}, Today's_Bottom_Rate == {Bottom}")
     file.write("\n") 
     file.close()
