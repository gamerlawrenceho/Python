import requests
import os
import sys

os.chdir(sys.path[0])

api_key = "a622af822aea39f5851c5132c4a9aa33"

base_url = "https://api.openweathermap.org/data/2.5/weather?"
city_name = input("Enter city name : ")
units = "metric"
lang = "zh_tw"

send_url = base_url
send_url += "appid=" + api_key
send_url += "&q=" + city_name
send_url += "&units=" + units
send_url += "&lang=" + lang
print(send_url)

respones = requests.get(send_url)
info = respones.json()
print(f'city = {info["name"]}')
print(info["main"]["temp"])
print(info["weather"][0]["description"])

if "main" in info.keys():
    icon_code = info["weather"][0]["icon"]
    icon_url = f"https://openweathermap.org/img/wn/{icon_code}@2x.png"
    respones = requests.get(icon_url)
    with open(f"{icon_code}.png", "wb") as icon_file:
        icon_file.write(respones.content)
else:
    print("City Not Found")
