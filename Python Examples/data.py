from urllib import response
import requests
import datetime
import pathlib
from bs4 import BeautifulSoup as bs

half_link  = "https://www.programiz.com/"
fname = pathlib.Path('data.py')

print("Last modification time: %s" % datetime.datetime.fromtimestamp(fname.stat().st_mtime))
print("Last metadata change time or path creation time: %s" % datetime.datetime.fromtimestamp(fname.stat().st_ctime))
print()

url = "https://www.programiz.com/python-programming/examples"
req = requests.get(url)
soup= bs(req.content,"lxml") 
data1 = soup.find("div",{"class":"col-sm-12 col-reset"})
i = data1.find_all("li")
for j in i:
    Examples = j.find("a").text.strip()
    l = j.find("a")["href"]
    Link = half_link + l
    print(f"{Examples} -- {Link}")
    with open("data.txt","a")as f:
            f.write(f"{Examples} -- {Link}")
            f.write("\n")