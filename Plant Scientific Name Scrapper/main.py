from helium import *
from bs4 import BeautifulSoup as bs

url = ("https://www.thespruce.com/plants-a-to-z-5116344")
browser = start_chrome(url, headless=True)

soup = bs(browser.page_source,'html.parser')
data = soup.find("div",{"id":"alphabetical-nav--container_1-0"})
name = data.find_all("div",{"class":"alphabetical-card__title"}) 
sci_name = data.find_all("div",{"class":"alphabetical-card__subtitle"})

for i,(Plant_Name,Plant_Sci_Name) in enumerate(zip(name,sci_name)):
  with open("data.txt", "a") as file:
        plant = Plant_Name.text
        sci = Plant_Sci_Name.text
        print(f"plant name is :- {plant}, its scientic name is :- {sci}")
        file.write(f"plant name is :- {plant}, its scientic name is :- {sci}")
        file.write("\n")
