import requests
from bs4 import BeautifulSoup as bs
from gtts import gTTS
import os

for i in range(1,8):
    page_number = (i)
    url = F"https://www.ndtv.com/latest/page-{page_number}"
    response = requests.get(url)
    soup = bs(response.text,"lxml")

    header = soup.find("div",{"class":"row s-lmr mt-10"})
    for news in header:
      title_news = news.find_all("h2",{"class":"newsHdng"})
      for heading in title_news:
         with open("news.txt", "a") as file:
          tag = heading.find("a")
          Title = tag.text
          file.write(f"{Title}")
          file.write("\n") 
          file.write(f"next news")
          file.write("\n") 
          print(f"{Title}")
f = open("news.txt")
x = f.read()
language = "en"
audio = gTTS(text=x, slow=False)
audio.save("audio.mp3")
os.system("audio.mp3")
