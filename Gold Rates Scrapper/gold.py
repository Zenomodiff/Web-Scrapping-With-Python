import requests 
import time
from bs4 import BeautifulSoup as bs

url = F"https://gadgets.ndtv.com/finance/gold-rate-in-india"

response = requests.get(url)
soup = bs(response.text,"lxml")
anchor1= soup.find_all('div',"_cptbl _cptblm")
print("Date & Time =" , time.asctime())
print("------------------------------------------------")
for State in anchor1:
    Title =  State.find_all('tr',"_cptbltr")
    with open("Gold_Rate.txt", "w",encoding="utf-8") as file:
     for value in Title:
        Title1 = value.find("a")
        Title2 = value.find('td',"_lft")
        if(Title1!=None):
            State = Title1.text
            Price = Title2.text
            file.write(str(time.asctime()))
            Data = " Today's Gold Price in "
            file.write(Data)
            file.write(f"{State} --- {Price}")
            file.write("\n")
            print(f"{(str(time.asctime()))} --- {Data} --- {State} --- {Price}")
        


    

