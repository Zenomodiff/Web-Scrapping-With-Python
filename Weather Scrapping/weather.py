import requests
from bs4 import BeautifulSoup as bs

serach = input('Search for city or place......: ')

url = F"https://www.timeanddate.com/weather/india/{serach}"

response = requests.get(url)
soup = bs(response.text,"lxml")
weather = soup.find_all("table",{"class":"table table--left table--inner-borders-rows"})
for climate in weather:
    Data = climate.find_all("tr")
    for Full_Data in Data:
        print(Full_Data.text)

