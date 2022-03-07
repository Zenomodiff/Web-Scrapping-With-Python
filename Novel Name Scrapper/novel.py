from bs4 import BeautifulSoup as bs
import requests

url = "https://www.modernlibrary.com/top-100/100-best-novels/"
response = requests.get(url)

soup = bs(response.content,'lxml')
data = soup.find('div',"list-100").find('ol')
new = data.find_all('div',"row")
for i in new:
    g = i.find('li')
    j = g.get_text().split('by')
    Book = j[0]
    Name = j[1]
    print(f"Book_Name :- {Book}, Its Author is :- {Name}")
    with open("data.txt",'a') as f:
        f.write(f"Book_Name :- {Book}, Its Author is :- {Name}")
        f.write('\n')
