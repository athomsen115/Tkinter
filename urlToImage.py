import requests, json
from tkinter import  *
from PIL import ImageTk, Image
from io import BytesIO

root = Tk()
root.title("Image Viewer")
root.iconbitmap('inkspot.ico')

api_key = "6fc04797a680e4a15568344846932d13"
url = "http://api.openweathermap.org/data/2.5/weather?zip=17057,us&appid=" + api_key + "&units=imperial"
res = requests.get(url)
info = json.loads(res.text)
forecastIcon = info['weather'][0]['icon']
iconURL = "http://openweathermap.org/img/wn/" + forecastIcon + ".png"
icon = requests.get(iconURL) 
image = ImageTk.PhotoImage(Image.open(BytesIO(icon.content)))
iconLbl = Label(root, image=image, background="black")
iconLbl.pack()




root.mainloop()