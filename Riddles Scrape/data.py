from urllib import response
import requests
from bs4 import BeautifulSoup as bs
import datetime
import pathlib
import sys

fname = pathlib.Path('data.py')

print("Last modification time: %s" % datetime.datetime.fromtimestamp(fname.stat().st_mtime))
print("Last metadata change time or path creation time: %s" % datetime.datetime.fromtimestamp(fname.stat().st_ctime))
print()

url = "https://www.goodhousekeeping.com/life/a41779999/riddles-for-adults/"
req = requests.get(url)
soup = bs(req.content,"lxml") 
data1 = soup.find_all("p",{"class":"css-1nd4gv7 et3p2gv0"})[4:]
for i in data1:
    j = i.find("strong")
    riddles = i.get_text()
    print(riddles)
    with open("data.txt","a")as f:
        f.write(f"{riddles}")
        f.write("\n")