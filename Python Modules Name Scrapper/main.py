from encodings import utf_8
import requests
from bs4 import BeautifulSoup as bs


url = "https://docs.python.org/3/py-modindex.html#cap-b"
res = requests.get(url)
soup = bs(res.text,"lxml")

anchor1 = soup.find_all("table",{"class":"indextable"})
for i in anchor1:
    j = i.find_all("code",{"class":"xref"})
    l = i.find_all('em')
    for k in j:
        Modules = k.text.strip()
        with open('data.txt','a', encoding="utf_8")as f:
            f.write(Modules)
            f.write('\n')
            print(Modules)
