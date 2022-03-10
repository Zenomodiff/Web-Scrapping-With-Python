import requests
from bs4 import BeautifulSoup as bs

for i in range(100):

    url = "https://randomword.com/"
    response = requests.get(url)
    soup = bs(response.content,"lxml")
    Word= soup.find('div', id = "random_word").text.strip()
    Meaning= soup.find('div', id = "random_word_definition").text.strip()

    print(f"{Word} - {Meaning}")
    with open("total.txt",'a', encoding="utf-8")as f:
        f.write(f"{Word} - {Meaning}")
        f.write("\n")
