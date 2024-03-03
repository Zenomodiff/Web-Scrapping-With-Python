from json import encoder
from bs4 import BeautifulSoup as bs
import requests,re

url = "https://forecast.weather.gov/MapClick.php?lat=32.3301&lon=-88.9367"
response = requests.get(url)
soup = bs(response.content,'lxml')

def weather_data():

    data1 = soup.find('h2',{"class":"panel-title"})
    P = data1.text.strip()
    Place = ("Place "+ " - " + str(P))
    print(Place)

    data2 = soup.find('span', {"class": "smallTxt"})
    latitude = re.match('^Lat:\s(.*)Lon:', data2.text).group(1)
    longitude = re.match('.*Lon:\s(.*)Elev:', data2.text).group(1)
    elevation = re.match('.*Elev:\s(.*).$', data2.text).group(1)
    print(f"Latitude:- {latitude}, Longitude:- {longitude}, Elevation:- {elevation}")

    data3 = soup.find('p',{"class":"myforecast-current"})
    C = data3.text.strip()
    Condition = ("Condition "+ " - " + str(C))
    print(Condition)

    data4 = soup.find('p',{"class":"myforecast-current-lrg"})
    FARE = data4.text.strip()
    Temp_F = ("Temp in F "+ " - " + str(FARE))
    print(Temp_F)

    data5 = soup.find('p',{"class":"myforecast-current-sm"})
    CEL = data5.text.strip()
    Temp_C = ("Temp in C "+ " - " + str(CEL))
    print(Temp_C)

    data6 = soup.find('div',{"id":"current_conditions_detail"})
    value = data6.find_all('td')

    Humidity = value[0].text.strip()
    Humidity_Val = value[1].text.strip()
    humidity = (str(Humidity) + " - " + str(Humidity_Val))
    print(humidity)

    Wind_Speed = value[2].text.strip()
    Wind_Speed_Val = value[3].text.strip()
    wind_speed = (str(Wind_Speed) + " - " + str(Wind_Speed_Val))
    print(wind_speed)

    Barometer = value[4].text.strip()
    Barometer_Val = value[5].text.strip()
    barometer = (str(Barometer) + " - " + str(Barometer_Val))
    print(barometer)

    Dew_point = value[6].text.strip()
    Dew_point_Val = value[7].text.strip()
    dew_point = (str(Dew_point) + " - " + str(Dew_point_Val))
    print(dew_point)

    Visibility = value[8].text.strip()
    Visibility_Val = value[9].text.strip()
    visibility = (str(Visibility) + " - " + str(Visibility_Val))
    print(visibility)

    Wind_Chill = value[10].text.strip()
    Wind_Chill_Val = value[11].text.strip()
    wind_chill = (str(Wind_Chill) + " - " + str(Wind_Chill_Val))
    print(wind_chill)

    Lastupdate = value[1].text.strip()
    Lastupdate_Val = value[1].text.strip()
    last_updtte = (str(Lastupdate) + " - " + str(Lastupdate_Val))
    print(last_updtte)

    with open("data.txt","w",encoding="utf-8")as f:
        f.write(Place)
        f.write("\n")
        f.write(f"Latitude:- {latitude}, Longitude:- {longitude}, Elevation:- {elevation}")
        f.write("\n")
        f.write(Condition)
        f.write("\n")
        f.write(Temp_F)
        f.write("\n")
        f.write(Temp_C)
        f.write("\n")
        f.write(humidity)
        f.write("\n")
        f.write(wind_speed)
        f.write("\n")
        f.write(barometer)
        f.write("\n")
        f.write(dew_point)
        f.write("\n")
        f.write(visibility)
        f.write("\n")
        f.write(wind_chill)
        f.write("\n")
        f.write(last_updtte)
        f.write("\n")

weather_data()
