import requests
from bs4 import BeautifulSoup as bs

Wikipedia = input('Enter The Content To Search :- ')
url = (f"https://en.wikipedia.org/wiki/{Wikipedia}")
response = requests.get(url)

try:

  soup = bs(response.text,'html.parser')
  Words = soup.find("div",{"class":"mw-parser-output"})
  Data1 = Words.find_all("p")[0]
  Data2 = Words.find_all("p")[1]
  Data3 = Words.find_all("p")[2]

  Output = str(Data1.text.strip()) + str(Data2.text.strip()) + str(Data3.text.strip())

  print(Output)
except:
  print('\n')
  print('It is not found in Wikipedia')
  print('\n')
