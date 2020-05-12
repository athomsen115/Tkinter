import json, requests
from datetime import datetime
from tkinter import  *
from PIL import ImageTk, Image
from io import BytesIO

root = Tk()
root.title("Air Quality App")
root.iconbitmap('inkspot.ico')
#root.geometry("600x100")
root.configure(background="blue")


def zipLookup():
    #zipLabel = Label(root, text=zipCode.get())
    #szipLabel.grid(row=1, column=0, columnspan=2)
    api_key = "7FA1426C-C1A5-4354-93F7-A5FEBC2C4149"
    #http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=17057&distance=5&API_KEY=7FA1426C-C1A5-4354-93F7-A5FEBC2C4149
    try:
        apiRequest = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipCode.get() + "&distance=25&API_KEY=" + api_key)
        api = json.loads(apiRequest.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']
        
        if category.lower() == "good":
            weatherColor = "#0C0"
        elif category.lower() == "moderate":
            weatherColor = "#FFFF00"
        elif category.lower().contains("usg"):
            weatherColor = "#FF9900"
        elif category.lower() == "unhealthy":
            weatherColor = "#FF0000"
        elif category.lower() == "very unhealthy":
            weatherColor = "#990066"
        elif category.lower() == "hazardous":
            weatherColor = "#660000"
        
        label = Label(qualityFrame, text=city + " Air Quality " + str(quality), font=("comicsans", 15), background=weatherColor)
        label.grid(row=1, column=0, columnspan=2)
        qualityFrame.configure(background=weatherColor)
    except:
        api = "Error..."

def weather():
    api_key = "6fc04797a680e4a15568344846932d13"

    try:
        url = "http://api.openweathermap.org/data/2.5/weather?zip=" + zipCode.get() + ",us&appid=" + api_key + "&units=imperial"
        res = requests.get(url)
        info = json.loads(res.text)
        forecast = info['weather'][0]['main']
        forecastDes = info['weather'][0]['description']
        forecastIcon = info['weather'][0]['icon']
        iconURL = "http://openweathermap.org/img/wn/" + forecastIcon + ".png"
        icon = requests.get(iconURL) 
        image = ImageTk.PhotoImage(Image.open(BytesIO(icon.content)))
        
        town = info['name']
        townLbl = Label(townFrame, text=town, font=("comicsans", 20))
        townLbl.pack()
        
        forecastLbl = Label(forecastFrame, text="Current Forecast: " + forecast, font=("comicsans", 10))
        forecastLbl.grid(row=0, column=0, stick=W)
        forecastDesLbl = Label(forecastFrame, text="Forecast Description: " + forecastDes, font=("comicsans", 10))
        forecastDesLbl.grid(row=1, column=0, stick=W)
        iconLbl = Label(forecastFrame, image=image)
        iconLbl.grid(row=0, column=1, rowspan=2)
        
        currentTemp = round(info['main']['temp'])
        tempLbl = Label(infoFrame, text=currentTemp, font=("comicsans", 25))
        tempLbl.grid(row=0, column=0, columnspan=2, pady=5, padx=5)
        minTemp = info['main']['temp_min']
        minLbl = Label(infoFrame, text=minTemp, font=("comicsans", 14), fg="#0a609d")
        minLbl.grid(row=1, column=0, padx=10)
        minL = Label(infoFrame, text="Low", font=("comicsans", 12), fg="#0a609d")
        minL.grid(row=2, column=0, pady=(0,10), padx=10)
        maxTemp = round(info['main']['temp_max'])
        maxLbl = Label(infoFrame, text=maxTemp, font=("comicsans", 14), fg="red")
        maxLbl.grid(row=1, column=1, padx=10)
        maxL = Label(infoFrame, text="High", font=("comicsans", 12), fg="red")
        maxL.grid(row=2, column=1, pady=(0,10), padx=10)
        pressure = info['main']['pressure'] # in hPa
        pressLbl = Label(infoFrame, text="Pressure: " + str(pressure) + " hPa", font=("comicsans", 10))
        pressLbl.grid(row=3, column=0, columnspan=2, stick=W)
        humidity = info['main']['humidity'] # returns percentage
        humLbl = Label(infoFrame, text="Humidity: " + str(humidity) + "%", font=("comicsans", 10))
        humLbl.grid(row=4, column=0, columnspan=2, stick=W)
        visibility = info['visibility'] # in meters
        visibility = round(visibility * (0.000621)) #miles = meters * 0.000621
        visLbl = Label(infoFrame, text="Visibility: " + str(visibility) + " miles", font=("comicsans", 10))
        visLbl.grid(row=5, column=0, columnspan=2, stick=W)
        
        windSpeed = info['wind']['speed']
        windDir = info['wind']['deg'] # returns in degrees
        sector = ["N","NNE","NE","ENE","E","ESE","SE","SSE","S","SSW","SW","WSW","W","WNW","NW","NNW","N"]
        index = windDir % 360
        index = round(index/22.5)+1
        compassDir = sector[index]
        windLbl = Label(windFrame, text="Wind Speed: " + str(windSpeed) + " " + compassDir, font=("comicsans", 12))
        windLbl.pack()
        
        #print(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
        sunrise = int(info['sys']['sunrise'])
        sunrise = datetime.fromtimestamp(sunrise).strftime('%H:%M:%S')
        sunriseLbl = Label(sunFrame, text="Sunrise: " + sunrise, font=("comicsans", 10))
        sunriseLbl.grid(row=0, column=0)
        sunset = int(info['sys']['sunset'])
        sunset = datetime.fromtimestamp(sunset).strftime('%H:%M:%S')
        sunsetLbl = Label(sunFrame, text="Sunset: " + sunset, font=("comicsans", 10))
        sunsetLbl.grid(row=1, column=0)
        
    except:
        weather = "Error..."
        

zipFrame = LabelFrame(root, text="Zip Code", pady=25)
zipFrame.grid(row=0, column=0)
qualityFrame = LabelFrame(root, text="Air Quality", pady=25)
qualityFrame.grid(row=1, column=0)
weatherFrame = LabelFrame(root, text="Current Weather", pady=25)
weatherFrame.grid(row=2, column=0, columnspan=2)
indexFrame = LabelFrame(root, text="Air Quality Legend")
indexFrame.grid(row=0, column=1, rowspan=2)
indexFrame.configure(background="#5dbcd2")

townFrame = LabelFrame(weatherFrame)
townFrame.grid(row=0, column=0, columnspan=2)
forecastFrame = LabelFrame(weatherFrame, pady=10)
forecastFrame.grid(row=1, column=0, columnspan=2, rowspan=3)
windFrame = LabelFrame(weatherFrame)
windFrame.grid(row=4, column=0, columnspan=2)
infoFrame = LabelFrame(weatherFrame, padx=10)
infoFrame.grid(row=0, column=2, columnspan=2, rowspan=6)
sunFrame = LabelFrame(weatherFrame)
sunFrame.grid(row=5, column=0, columnspan=2, rowspan=2)


zipCode = Entry(zipFrame)
zipCode.grid(row=0, column=0, stick=W+E+N+S)

submitButton = Button(zipFrame, text="Air Quality Lookup", command=zipLookup)
submitButton.grid(row=0, column=1, stick=W+E+N+S)

weatherButton = Button(zipFrame, text="Weather Lookup", command=weather)
weatherButton.grid(row=0, column=2, stick=W+E+N+S)

goodRange = Label(indexFrame, text="0-50", font=("comicsans", 12), background="#0C0")
goodRange.grid(row=1, column=0, stick=E)
moderateRange = Label(indexFrame, text="51-100", font=("comicsans", 12), background="#FFFF00")
moderateRange.grid(row=2, column=0, stick=E)
usgRange1 = Label(indexFrame, text="101-150", font=("comicsans", 12), background="#FF9900")
usgRange1.grid(row=3, column=0, stick=E)
usgRange1 = Label(indexFrame, text="              ", font=("comicsans", 12), background="#FF9900")
usgRange1.grid(row=4, column=0, stick=E)
unhealthyRange = Label(indexFrame, text="151-200", font=("comicsans", 12), background="#FF0000")
unhealthyRange.grid(row=5, column=0, stick=E)
veryunhealthyRange = Label(indexFrame, text="201-300", font=("comicsans", 12), background="#990066")
veryunhealthyRange.grid(row=6, column=0, stick=E)
hazardousRange = Label(indexFrame, text="301-500", font=("comicsans", 12), background="#660000")
hazardousRange.grid(row=7, column=0, stick=E)

good = Label(indexFrame, text="Good", font=("comicsans", 12), background="#0C0")
good.grid(row=1, column=1, stick=W)
moderate = Label(indexFrame, text="Moderate", font=("comicsans", 12), background="#FFFF00")
moderate.grid(row=2, column=1, stick=W)
usg1 = Label(indexFrame, text="(USG) Unhealthy", font=("comicsans", 12), background="#FF9900")
usg1.grid(row=3, column=1, stick=W)
usg2 = Label(indexFrame, text="for Sensitive Groups", font=("comicsans", 12), background="#FF9900")
usg2.grid(row=4, column=1, stick=W)
unhealthy = Label(indexFrame, text="Unhealthy", font=("comicsans", 12), background="#FF0000")
unhealthy.grid(row=5, column=1, stick=W)
veryunhealthy = Label(indexFrame, text="Very Unhealthy", font=("comicsans", 12), background="#990066")
veryunhealthy.grid(row=6, column=1, stick=W)
hazardous = Label(indexFrame, text="Hazardous", font=("comicsans", 12), background="#660000")
hazardous.grid(row=7, column=1, stick=W)


root.mainloop()
