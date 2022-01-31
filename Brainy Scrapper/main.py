import requests
from bs4 import BeautifulSoup as bs
from random import *

search_term = input('Enter quote input:')

page = 4

url = f"https://www.brainyquote.com/search_results?q={search_term}&pg={page}"

r=requests.get(url)
soup= bs(r.content,"html.parser")   
anchor1= soup.find_all('a',{"class":"b-qt"})
anchor2= soup.find_all('a',{"class":"bq-aut"})

for i,(quote,author) in enumerate(zip(anchor1,anchor2)):
  with open(search_term +".txt", "a") as file:
    quote = quote.find('div').text.strip()
    author = author.text.strip()
    file.write(f"{quote} - {author}")
    file.write("\n")

print("done saving !!!")
