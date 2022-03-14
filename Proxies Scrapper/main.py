import requests
from bs4 import BeautifulSoup as bs

url = F"https://free-proxy-list.net/"

response = requests.get(url)
soup = bs(response.text,"lxml")

try:
        
    anchor1 = soup.find_all("table",{"class":"table"})
    for i in anchor1:
        prox = i.find("tbody")
        for j in prox:
            a = j.find_all('td')[0]
            b = j.find_all('td')[1]
            c = j.find_all('td')[2]
            d = j.find_all('td')[3]
            e = j.find_all('td')[4]
            f = j.find_all('td')[5]
            g = j.find_all('td')[6]
            h = j.find_all('td')[7]
            ip = a.text
            port = b.text
            country_code = c.text
            country = d.text
            anonimity = e.text
            google_pass = f.text
            https = g.text
            last_checked = h.text

            print(f"{ip} - {port} - {country_code} - {country} - {anonimity} - {google_pass} - {https} - {last_checked}")
            with open("proxies.txt",'a')as f:
                f.write(f"{ip}:{port}")
                f.write("\n")
except:
    pass
