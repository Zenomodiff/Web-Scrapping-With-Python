import requests
import os
from bs4 import BeautifulSoup
from selenium import webdriver

mydirectory = os.path.dirname(os.path.abspath(__file__))
driver = webdriver.Chrome(mydirectory + "\chromedriver.exe")

population = []
url = "https://www.worldometers.info/world-population/"
driver.get(url)
response = driver.page_source
soup = BeautifulSoup(response, "html.parser")
soup1 = soup.find_all('div', class_ = "maincounter-number")
for i in soup1:
 print(i.text)

     
