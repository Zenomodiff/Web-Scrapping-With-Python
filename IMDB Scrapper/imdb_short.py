import requests
import pyshorteners
from bs4 import BeautifulSoup as bs

url = f"https://www.imdb.com/chart/top/?ref_=nv_mv_250"

res = requests.get(url)
sh = pyshorteners.Shortener()
soup = bs(res.text,"lxml")
movie = soup.find_all("td",{"class":"titleColumn"})
rating = soup.find_all("td",{"class":"ratingColumn imdbRating"})
with open("movies_url_shortenered.txt", "a") as file:
  for movies in movie:
    name = movies.find("a")
    link = name["href"]
    name = movies.find("a").text.strip()
    
    for rat in rating:
     ratings = rat.find("strong").text.strip()
     year = movies.find("span",{"class":"secondaryInfo"})
     year = year.text.strip()
     insert = link

    url_1 = f"https://www.imdb.com{insert}?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=9703a62d-b88a-4e30-ae12-90fcafafa3fc&pf_rd_r=K4N1S8KNE22RX0TTDWXV&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_1"
    x = sh.tinyurl.short(url_1)
    file.write(f"{name}--{ratings}--{year}--{x}")
    file.write("\n")
print("done saving !!!")