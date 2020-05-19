import requests, json
from datetime import datetime

def weather():
    api_key = {INSERT-YOUR-OPENWEATHER-API-KEY}

    try:
        url = "http://api.openweathermap.org/data/2.5/weather?zip=17057,us&appid="+api_key+"&units=imperial"
        res = requests.get(url)
        info = json.loads(res.text)
        print(res.text)
        print(info)
        forecast = info['weather'][0]['main']
        print(forecast)
        forecastDes = info['weather'][0]['description']
        forecastIcon = info['weather'][0]['icon']
        iconURL = "http://openweathermap.org/img/wn/" + forecastIcon + ".png"
        
        print("forecast: {}, description: {}".format(forecast, forecastDes))
        
        currentTemp = info['main']['temp']
        print(str(currentTemp) + "F")
        minTemp = info['main']['temp_min']
        print(str(minTemp) + "F")
        maxTemp = info['main']['temp_max']
        print(str(maxTemp) + "F")
        pressure = info['main']['pressure'] # in hPa
        print(str(pressure) +"hPa")
        humidity = info['main']['humidity'] # returns percentage
        print(str(humidity) + "%")
        visibility = info['visibility'] # in meters
        print(str(visibility) + "meters")
        #miles = meters * 0.000621
        visibility = round(visibility * (0.000621))
        print(str(visibility) + "miles")
        windSpeed = info['wind']['speed']
        print(str(windSpeed) +"m/s")
        windDir = info['wind']['deg'] # returns in degrees
        print(str(windDir) + "degrees")
        sector = ["N","NNE","NE","ENE","E","ESE","SE","SSE","S","SSW","SW","WSW","W","WNW","NW","NNW","N"]
        index = windDir % 360
        index = round(index/22.5)+1
        compassDir = sector[index]
        print(compassDir)
        town = info['name']
        print(town)
        #print(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
        sunrise = int(info['sys']['sunrise'])
        print(sunrise)
        sunrise = datetime.utcfromtimestamp(sunrise).strftime('%H:%M:%S')
        print(sunrise)
        sunset = int(info['sys']['sunset'])
        print(sunset)
        sunset = datetime.utcfromtimestamp(sunset).strftime('%H:%M:%S')
        print(sunset)
        
        print("currentTemp: {}, minTemp: {}, maxTemp: {}, pressure: {}hPa, humidity: {}%, visibility: {} miles, windspeed: {}m/s, windDir: {}, town: {}, sunrise: {}, sunset: {}".format(currentTemp, minTemp, maxTemp, pressure, humidity, visibility, windSpeed, compassDir, town, sunrise, sunset ))
 
    except:
        weather = "Error..."
        
weather()
