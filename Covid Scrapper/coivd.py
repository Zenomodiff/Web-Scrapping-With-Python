import requests
from bs4 import BeautifulSoup as bs

url = "https://www.worldometers.info/coronavirus/"      

response = requests.get(url)
soup = bs(response.text,"lxml")
anchor1= soup.find_all('div',"content-inner")
for span in anchor1:
    span1 = span.find_all('div',"maincounter-number")
    one = span1[0]
    two = span1[1]
    three = span1[2]
    Total_Cases = one.text.strip()
    Deaths = two.text.strip()
    Recovered = three.text.strip()

print("Total_Cases = " + str(Total_Cases))
print("Total_Deaths = " + str(Deaths))
print("Total_Recovered = " + str(Recovered))

with open("covid_data.txt", "w") as file:
          file.write(f"Total_Cases = {Total_Cases}")
          file.write("\n")
          file.write(f"Total_Deaths = {Deaths}")
          file.write("\n")
          file.write(f"Total_Recovered = {Recovered}")
          file.write("\n")  
