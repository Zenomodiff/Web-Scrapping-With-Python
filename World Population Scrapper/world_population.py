from helium import *
from bs4 import BeautifulSoup as bs

url = "https://www.worldometers.info/world-population/"
browser = start_chrome(url, headless=True)

soup = bs(browser.page_source,'html.parser')
Current_Population = soup.find('div',"content-inner")
first_element = Current_Population.find('span',{'class':"rts-nr-int rts-nr-10e9"}).text
second_element = Current_Population.find('span',{'class':"rts-nr-int rts-nr-10e6"}).text
third_element = Current_Population.find('span',{'class':"rts-nr-int rts-nr-10e3"}).text
fourth_element = Current_Population.find('span',{'class':"rts-nr-int rts-nr-10e0"}).text
Current_Population_Data = str(first_element + second_element + third_element + fourth_element)

Births_Today = soup.find('span',{'rel':"births_today"})
first_element = Births_Today.find('span',{'class':"rts-nr-int rts-nr-10e3"}).text
second_element = Births_Today.find('span',{'class':"rts-nr-int rts-nr-10e0"}).text
Births_Today_Data = str(first_element + second_element)

Deaths_Today = soup.find('span',{'rel':"dth1s_today"})
first_element = Deaths_Today.find('span',{'class':"rts-nr-int rts-nr-10e3"}).text
second_element = Deaths_Today.find('span',{'class':"rts-nr-int rts-nr-10e0"}).text
Deaths_Today_Data = str(first_element + second_element)

Population_Growth_Today = soup.find('span',{'rel':"absolute_growth"})
first_element = Population_Growth_Today.find('span',{'class':"rts-nr-int rts-nr-10e3"}).text
second_element = Population_Growth_Today.find('span',{'class':"rts-nr-int rts-nr-10e0"}).text
Population_Growth_Data = str(first_element + second_element)

print('World Population is: ' + Current_Population_Data)
print('Todays Birth is: ' + Births_Today_Data)
print('Todays Death is: ' + Deaths_Today_Data)
print('Todays Population Growth is: ' + Population_Growth_Data)

with open ("data.txt", "w") as f:
    f.write(f"Current World Population is : {Current_Population_Data}")
    f.write("\n")
    f.write(f"Today's Births is : {Births_Today_Data}")
    f.write("\n")
    f.write(f"Today's Deaths is : {Deaths_Today_Data}")
    f.write("\n")
    f.write(f"Todays Population Growth is: {Population_Growth_Data}")
    f.write("\n")
