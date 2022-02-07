import requests
from flask import *
import json, time
from bs4 import BeautifulSoup as bs

app = Flask(__name__)
@app.route('/', methods=['GET'])
def home_page():
    url = "https://www.timeanddate.com/counters/newyear.html"
    req = requests.get(url)
    soup = bs(req.text,"lxml")

    day = soup.find_all("p",{"id":"rs2"})
    for days in day:
      span1 = days.find("span", id="el_d1")
    #   span11 = days.find("span", id="el_d1t")
      span2 = days.find("span", id="el_h1")
    #   span22 = days.find("span", id="el_h1t")
      span3 = days.find("span", id="el_m1")
    #   span33 = days.find("span", id="el_m1t")
      span4 = days.find("span", id="el_s1")
    #   span44 = days.find("span", id="el_s1t")

    data_set = {"Next New Year Eve": {'days': span1.text , 'hours': span2.text , 'minutes': span3.text , 'seconds': span4.text}}
    json_dump = json.dumps(data_set)
    return json_dump
if __name__ == '__main__':
    app.run(port=5000) 