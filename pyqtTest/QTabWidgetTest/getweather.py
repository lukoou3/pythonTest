#coding = utf-8

import requests
# import json

class GetWeatherInfo:
    def __init__(self, flag, city):
        self.flag = flag
        if city == "北京":
            self.city = "beijing"
        elif city == "上海":
            self.city = "shanghai"
        else:
            self.city = "guangzhou"
        self.real_time = "https://api.seniverse.com/v3/weather/now.json?key=7q157rsodxjtpq9z&location=" + self.city + "&language=zh-Hans&unit=c"
        self.nearly_3_days = "https://api.seniverse.com/v3/weather/daily.json?key=7q157rsodxjtpq9z&location=" + self.city + "&language=zh-Hans&unit=c&start=0&days=5"

    def getweather(self):
        if self.flag == 0:
            widc = self.internet(self.real_time)
            if widc:
                weather = widc["results"][0]["now"]["text"]
                weather_code = widc["results"][0]["now"]["code"]
                weather_temperature = widc["results"][0]["now"]["temperature"]
                last_update =  widc["results"][0]["last_update"]
                return weather, weather_code, weather_temperature, last_update
        if self.flag == 1:
            widc = self.internet(self.nearly_3_days)
            weather0 =widc["results"][0]["daily"][0]
            weather1 =widc["results"][0]["daily"][1]
            weather2 =widc["results"][0]["daily"][2]
            return weather0, weather1, weather2

    def internet(self, url):
        r = requests.get(url)
        weatherinfo = r.text
        weatherinfo_dic = eval(weatherinfo)
        if "status_code" in weatherinfo_dic:
            return 0
        else:
            return weatherinfo_dic