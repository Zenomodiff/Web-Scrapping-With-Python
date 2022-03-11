from helium import *
from bs4 import BeautifulSoup as bs

user_name = input('Enter the github profile name : ')

url = (f"https://github.com/{user_name}")
browser = start_chrome(url, headless=True)

def Github_stats():

    soup = bs(browser.page_source,'html.parser')

    a = soup.find('span',"p-nickname")
    User_Name = a.text.strip() 
    print(f"User_Name = {User_Name}") #user name

    b = soup.find_all('div',"flex-order-1")
    for i in b:
        a = i.find('span',"text-bold")
        if a != None:
            Followers = a.text.strip() 
            print(f"Followers = {Followers}") #followers count

    c = soup.find_all('div',"flex-order-1")[-1]
    data = c.find_all('span',"text-bold")[1]
    Following = (data.text)
    print(f"Following = {Following}") #following count

    d = soup.find('div',"p-note")
    Content = d.text.strip()
    print(f"Contents = {Content}")

    e = soup.find('span',"Counter")
    Repositories = e.text.strip()
    print(f"Repositories = {Repositories}") #repository count

    f = soup.find_all('div',"position-relative")[-3]
    h2 = f.find('h2',"f4")
    for i in h2:
        j=i.get_text().split(' ')
        Contributions = j[6].strip()
        print(f"Contributions = {Contributions}") #contributions

    g = soup.find_all('span',"Counter")[7]
    Stars = g.text.strip()
    print(F"Stars = {Stars}") #stars count

    h = soup.find('span',"p-label")
    Place = h.text.strip()
    print(F"Place = {Place}") #place
    print('')

    with open(f"{User_Name}.txt",'w')as f:
        f.write((f"User_Name = {User_Name}"))
        f.write('\n')
        f.write((f"Followers = {Followers}"))
        f.write('\n')
        f.write((f"Following = {Following}"))
        f.write('\n')
        f.write((f"Contents = {Content}"))
        f.write('\n')
        f.write((f"Repositories = {Repositories}"))
        f.write('\n')
        f.write((f"Contributions = {Contributions}"))
        f.write('\n')
        f.write((F"Stars = {Stars}"))
        f.write('\n')
        f.write((F"Place = {Place}"))
        f.write('\n')

    data = soup.find('svg',"js-calendar-graph-svg")
    g = data.find_all('rect',"ContributionCalendar-day")

    for i in g:
        Date = i.get('data-date')
        Contributions = i.get('data-count')
        Data_Level = i.get('data-level')

        print(f"on this date {Date} you have {Contributions} contributions and its data level is {Data_Level}")
        with open(f"{User_Name}.txt",'a')as f:
            f.write(f"on this date {Date} you have {Contributions} contributions and its data level is {Data_Level}")
            f.write('\n')

Github_stats()
