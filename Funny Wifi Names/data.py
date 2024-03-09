import requests
from bs4 import BeautifulSoup as bs
import sys

url = "https://blog.internxt.com/best-wifi-names/"

req = requests.get(url)
soup= bs(req.content,"lxml") 
data1 = soup.find_all("ol")
for i in data1:
    j = i.text.strip()
    if "One more time, go to your router and copy your router's IP address from its back." in j:
        sys.exit()
    print(j) 
    with open("wifi.txt","a")as f:
            f.write(f"{j}")
            f.write("\n")   

