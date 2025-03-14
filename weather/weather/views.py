from django.shortcuts import render, redirect
from weather.key import api_key
import requests
import math
from googletrans import Translator


def index(request):
    return render(request, "weather/home.html")


def result(request):
    if request.method == "POST":
        original_city_name = request.POST["city"]
        city_name = Translator().translate(original_city_name, dest="en").text
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}&lang=ja&units=metric"  # {api_key} のような変数を文字列内に埋め込むために f が必要
        weather_data = requests.get(url).json()
        try:
            context = {
                "city_name": weather_data["city"]["name"],
                "city_country": weather_data["city"]["country"],
                "wind": weather_data["list"][0]["wind"]["speed"],
                "pressure": weather_data["list"][0]["main"]["pressure"],
                "humidity": weather_data["list"][0]["main"]["humidity"],
                "status": weather_data["list"][0]["weather"][0]["description"],
                "date": weather_data["list"][0]["dt_txt"],
                "date1": weather_data["list"][1]["dt_txt"],
                "date2": weather_data["list"][2]["dt_txt"],
                "date3": weather_data["list"][3]["dt_txt"],
                "date4": weather_data["list"][4]["dt_txt"],
                "date5": weather_data["list"][5]["dt_txt"],
                "date6": weather_data["list"][6]["dt_txt"],
                "weather": weather_data["list"][1]["weather"][0]["main"],
                "description": weather_data["list"][1]["weather"][0]["description"],
                "icon": weather_data["list"][0]["weather"][0]["icon"],
                "icon1": weather_data["list"][1]["weather"][0]["icon"],
                "icon2": weather_data["list"][2]["weather"][0]["icon"],
                "icon3": weather_data["list"][3]["weather"][0]["icon"],
                "icon4": weather_data["list"][4]["weather"][0]["icon"],
                "icon5": weather_data["list"][5]["weather"][0]["icon"],
                "icon6": weather_data["list"][6]["weather"][0]["icon"],
                "temp": round(weather_data["list"][0]["main"]["temp"]),
                "temp_min1": math.floor(weather_data["list"][1]["main"]["temp_min"]),
                "temp_max1": math.ceil(weather_data["list"][1]["main"]["temp_max"]),
                "temp_min2": math.floor(weather_data["list"][2]["main"]["temp_min"]),
                "temp_max2": math.ceil(weather_data["list"][2]["main"]["temp_max"]),
                "temp_min3": math.floor(weather_data["list"][3]["main"]["temp_min"]),
                "temp_max3": math.ceil(weather_data["list"][3]["main"]["temp_max"]),
                "temp_min4": math.floor(weather_data["list"][4]["main"]["temp_min"]),
                "temp_max4": math.ceil(weather_data["list"][4]["main"]["temp_max"]),
                "temp_min5": math.floor(weather_data["list"][5]["main"]["temp_min"]),
                "temp_max5": math.ceil(weather_data["list"][5]["main"]["temp_max"]),
                "temp_min6": math.floor(weather_data["list"][6]["main"]["temp_min"]),
                "temp_max6": math.ceil(weather_data["list"][6]["main"]["temp_max"]),
            }
        except:
            context = {"city_name": "見つかりませんでした"}

        return render(request, "weather/results.html", context)
    else:
        return redirect("weather:index")
