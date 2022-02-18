import requests
import pyshorteners
from bs4 import BeautifulSoup as bs

for i in range(0,30):
    page_number = (i)

    url = F'https://www.keralapsc.gov.in/previous-question-papers?tid=All&page={page_number}'  
    response = requests.get(url)
    sh = pyshorteners.Shortener()
    soup = bs(response.text,"lxml")
    anchor1 = soup.find_all("div",{"class":"main-content-inner"})
    
    for Title in anchor1:
     new_title = Title.find_all("td",{"headers":"view-title-table-column"})
     new_title2 = Title.find("td",{"class":"views-field views-field-body"})
     new_title3 = Title.find_all("td",{"headers":"view-field-file-table-column"})
     new_title4 = new_title2.find('p')
     Date = new_title4.text
     for new_title1 in new_title:
      new_title2 = new_title1.find('a')
      Title = new_title2.text
      for new_title5 in new_title3:
           new_title6 = new_title5.find('a')
           Link = new_title6["href"]
           url2 = F"https://www.keralapsc.gov.in{Link}"
           X = sh.tinyurl.short(url2)
      print(f"{Title}  --  {Date}  --  {X}")
      with open("psc.txt", "a") as file:
        file.write(f"{Title}  --  {Date}  --  {X}")
        file.write("\n") 
        file.close()