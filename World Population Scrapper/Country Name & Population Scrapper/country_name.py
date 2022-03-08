from xml.dom.minidom import Element
import requests,time
from helium import *
from bs4 import BeautifulSoup as bs

def get_data():

    url = F"https://www.worldometers.info/population/"
    response = requests.get(url)
    soup = bs(response.text,"lxml")
    Population = soup.find_all("div",{"class":"col-md-6"})                    
    for pop in Population:
        new1 = pop.find_all("ul")[-1]
        for new_pop in new1:
            new_pop = new_pop.find("a")
            Old_Link = new_pop["href"]
            Country_Name = new_pop.get_text()
            Link = Old_Link
            try:
                Url = F"https://www.worldometers.info{Link}"

                browser = start_chrome(Url, headless=True)
                soup = bs(browser.page_source,'html.parser')
                Current_Population = soup.find('div',{'class':"maincounter-number"})
                first = Current_Population.find('span',{'class':"rts-nr-int rts-nr-10e6"}).text
                second = Current_Population.find('span',{'class':"rts-nr-int rts-nr-10e3"}).text
                third = Current_Population.find('span',{'class':"rts-nr-int rts-nr-10e0"}).text
                Population = str(first + second + third)
                print(f"the population of - {Country_Name} is {Population}")
                with open("population.txt",'a')as file:
                    file.write(f"the population of - {Country_Name} is {Population}")
                    file.write('\n')
                time.sleep(1)
            except:
                Url = F"https://www.worldometers.info{Link}"
                browser = start_chrome(Url, headless=True)
                soup = bs(browser.page_source,'html.parser')
                Current_Population = soup.find('div',{'class':"maincounter-number"})
                first = Current_Population.find('span',{'class':"rts-nr-int rts-nr-10e3"}).text
                second = Current_Population.find('span',{'class':"rts-nr-int rts-nr-10e0"}).text
                Population = str(first + second)
                print(f"the population of - {Country_Name} is {Population}")
                with open("population.txt",'a')as file:
                    file.write(f"the population of - {Country_Name} is {Population}")
                    file.write('\n')
                time.sleep(1)
                
get_data()

