import requests
from bs4 import BeautifulSoup as bs

for i in range(0,9):
    page_number = (i)
    url = F"https://circuitdigest.com/arduino-projects?page={page_number}"
    response = requests.get(url)
    soup = bs(response.text,"lxml")
    anchor1 = soup.find_all("div",{"class":"content"})
    for head in anchor1:
        header = head.find_all("h3")
        for b in header:
            content = b.find_all("a")
            for tag in content:
              tag1 = tag.find("b")
              if(tag1!=None):
                  print(tag1.text)
                  with open("circuit.txt", "a") as file:
                   file.write(f"{tag1.text}")
                   file.write("\n") 
                   file.close()
