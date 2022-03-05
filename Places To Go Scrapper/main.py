from helium import *
from bs4 import BeautifulSoup as bs

url = "https://blog.thomascook.in/50-must-visit-places-in-the-world/"
browser = start_chrome(url, headless=True)

soup = bs(browser.page_source,'html.parser')
data = soup.find('div',"post-single-content")
new = data.find_all('ul')[-2]
for i in new:
    Place = i.text
    print(Place)
    with open('place.text','a')as file:
        file.write(Place)
        file.write("\n")
