from tkinter import *
from PIL import ImageTk, Image
import requests
import json


root = Tk()
root.title("Learn to Code")
root.iconbitmap(r"C:\Users\salim\PycharmProjects\Tkinter_Course")
root.geometry("750x400")


try:
    api_request = requests.get("http://api.weatherapi.com/v1/current.json?key=ce95ddec7b264dbaaad25711211510&q=Hatay&aqi=no")
    api = json.loads(api_request.content)

    city = api["location"]["name"]
    quality = api["current"]["condition"]["text"]
    degree = api["current"]["temp_c"]
    current_time = api["location"]["localtime"]

    api2_request =  requests.get("https://api.waqi.info/feed/@4048/?token=2f103e93714dccfd28839c438776caffe2121281")
    api2 = json.loads(api2_request.content)
    
    air_qual = api2["data"]["aqi"]


    if air_qual < 50:
        weather_color = "#0C0"
        print("Air Pollution Level is Good")
    
    elif air_qual >= 50 and air_qual<100:
        weather_color = "#FFFF00"
        print("Air Pollution Level is Moderate")
        
    
    elif air_qual >=100 and air_qual<150:
        weather_color = "ff9900"
        print("Air Pollution Level is Unhealthy for Sensitive Groups")


    elif air_qual >= 150 and air_qual<200:
        weather_color = "FF0000"
        print("Air Pollution Level is Unhealthy")

    elif air_qual >=200 and air_qual < 300:
        weather_color = "#990066"
        print("Air Pollution Level is Very Unhealthy")

    elif air_qual >= 300:
        weather_color = "#660000"
        print("Air Pollution Level is HAZARDOUS !!!!!!!!")


    root.configure(background=weather_color)

    myLabel = Label(root, text = city + "\n" + "Air Condition : " + str(quality) + "\n" + " Air Quality : " + str(air_qual) + "\n" + "Current Temperature : " + str(degree) + " Degree" + "\n" + "Last Update : " + current_time, font=("Helvetica", 30), background=weather_color)
    myLabel.pack()


except Exception as e:
    api = "Error.."
    api2 = "Error...."


root.mainloop()