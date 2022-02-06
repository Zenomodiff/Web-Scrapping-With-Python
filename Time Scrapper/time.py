import requests
from bs4 import BeautifulSoup as bs

url = "https://www.timeanddate.com/counters/newyear.html"
req = requests.get(url)
soup = bs(req.text,"lxml")

day = soup.find_all("td",{"id":"el_d2"})
day_name = soup.find_all("td",{"id":"el_d2t"})
hour = soup.find_all("td",{"id":"el_h2"})
hour_name = soup.find_all("td",{"id":"el_h2t"})
minute = soup.find_all("td",{"id":"el_m2"}) 
minute_name = soup.find_all("td",{"id":"el_m2t"})
second = soup.find_all("td",{"id":"el_s2"}) 
second_name = soup.find_all("td",{"id":"el_s2t"})
current = soup.find_all("span",{"id":"el"})

for days in day:
     days_text = days.text
for days_name in day_name:
     days_name = days_name.text    
for hours in hour:
     hours_text = hours.text    
for hours_name in hour_name:
     hours_name = hours_name.text     
for minutes in minute:
     minutes_text = minutes.text
for minutes_name in minute_name:
     minutes_name = minutes_name.text     
for seconds in second:
     seconds_text = seconds.text   
for seconds_name in second_name:
     seconds_name = seconds_name.text      

print(days_text ,days_name)
print(hours_text ,hours_name)
print(minutes_text ,minutes_name)
print(seconds_text ,seconds_name)