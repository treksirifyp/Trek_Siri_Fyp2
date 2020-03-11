from flask import Flask, render_template, request
import requests, json
import os
import csv
import time
from rasa.nlu.model import Metadata, Interpreter
app = Flask(__name__)

class Message:
    def __init__(self, text, sender, time, image):
        self.text = text
        self.sender = sender
        self.time = time
        self.image = image

class Hotel:
    def __init__(self, name, rating, price, address, image):
        self.name = name
        self.rating = rating
        self.price = price
        self.address = address
        self.image = image

class Weather:
    def __init__(self, city, temparature, description, image):
        self.city = city
        self.temparature = temparature
        self.description = description
        self.image = image

class City:
    def __init__(self, name, image):
        self.name = name
        self.image = image


Messages = []
City_Weather = []
City_Hotels = []
CitiesWithIamges = []

Cities = ["Gilgit", "Karimabad", "Skardu", "Chitral", "Gulmit", "Chilas", "Khaplu", "Gakuch", "Naran", "Kalam", "Swat"]

for city in Cities:
    c = City(city, './static/img/' + city + '.jpg')
    CitiesWithIamges.append(c)



"""for city in Cities:
    time.sleep(1.5)
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    api_key = "410463b3935acea56c8171825dbb4440"
    complete_url = base_url + "appid=" + api_key + "&q=" + city + "&units=metric"
    response = requests.get(complete_url)
    x = response.json()
    try:
        y = x["main"]
    except KeyError:
        pass
    current_temperature = y["temp"]
    try:
        z = x["weather"]
    except KeyError:
        pass
    weather_description = z[0]["description"]

    W = Weather(city, current_temperature, weather_description, "./static/img/"+city+ ".jpg")
    City_Weather.append(W)"""


for city in os.listdir("./scrapped data"):
    try:
        with open("./scrapped data/" + city + "/Hotels.csv", "r") as f:
            reader = csv.reader(f, delimiter=",")
            for i, line in enumerate(reader):
                if 'Hotel Name' not in line and len(line) > 0:
                    image = line[0].replace(" ", "%20")
                    H = Hotel(line[0], line[2], line[3], line[1], "./static/img/" + image + ".jpg")
                    if (line[0] != ""):
                        City_Hotels.append(H)
    except FileNotFoundError:
        pass

"""chilas_hotel = Hotel("Shangrila Hotel", 7, 5000, "KKH Main Road Chilas, Chilas")
gilgit_Hotel = Hotel("PTDC Motel Rama Lake", 8, 4000, "Rama Lake, Gilgit")
chitral_hotel = Hotel("PTDC Motel Bamborait", 7, 3500, "Main Road Bamborait, Chitral")
skardu_hotel = Hotel("Serena Khaplu Palace", 9, 13000, "Main Road Khaplu, Skardu")
swat_hotel = Hotel("Hotel Green", 6, 4000, "Main Road Kalam, Swat")
karimabad_hotel = Hotel("Hunza Serena Hotel", 8, 9000, "Main Road Hunza, Karimabad")
"""
#Hotels = {"Chillas": chilas_hotel, "Gilgit": gilgit_Hotel, "Chitral": chitral_hotel, "Skardu": skardu_hotel,
#          "Swat": swat_hotel, "Karimabad": karimabad_hotel}



@app.route("/")
@app.route("/home")
def hello():
    return render_template('Home.html', Cities=CitiesWithIamges)


@app.route("/hotels")
def hotels():
    return render_template('Hotels.html', Hotels=City_Hotels)


@app.route("/weather")
def weather_page():
    return render_template("Weather.html", Weather=City_Weather)


@app.route("/chat")
def Chat():
    return render_template("Chatbot.html", Messages=Messages)


@app.route('/ask', methods=['GET', 'POST'])
def ask():
    if request.method == 'POST':
        question = ""
        interpreter = Interpreter.load('./models/nlu/default/weathernlu')
        question = request.form["message"]
        delivered_message = Message(question, "User", "12:00", "static/user.png")
        Messages.append(delivered_message)
        reply_dict = interpreter.parse(question)
        print(reply_dict)
        reply_string = "Intent: " + json.dumps(reply_dict['intent'])
        reply_string1 = "Scores: " + json.dumps(reply_dict['intent_ranking'])
        reply = Message(reply_string + reply_string1, "Bot", "12:00", "static/bot.png")
        Messages.append(reply)
        return render_template("Chatbot.html", Messages=Messages)

    return render_template("Chatbot.html", Messages=Messages)

"""message = request.form["message"]
        delivered_message = Message(message, "User", "12:00", "static/user.png")
        Messages.append(delivered_message)
        array = message.split(' ')
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        api_key = "410463b3935acea56c8171825dbb4440"
        if "weather" in message:
            for city in Cities:
                if city in message:
                    complete_url = base_url + "appid=" + api_key + "&q=" + city + "&units=metric"
                    response = requests.get(complete_url)
                    x = response.json()
                    y = x["main"]
                    current_temperature = y["temp"]
                    z = x["weather"]
                    weather_description = z[0]["description"]

                    replied_message = Message("The Temprature in " + city + " is " + str(current_temperature) + " degree celcius " + " and the weather is " + weather_description,
                                              "Bot", "12:01", "static/bot.png")

                    Messages.append(replied_message)

                    return render_template("Chatbot.html", Messages=Messages)

        elif "hotel" in message:
            for city in Cities:
                if city in message:
 #                   city_hotel = Hotels[city]

#                    replied_message = Message("The best hotel in " + city + " is " + city_hotel.name + " and its rating is "
 #                                             + str(city_hotel.rating) + " stars. " +  "Its price is " + str(city_hotel.price)
  #                                            + " rupees per night. " + "Its address is " + city_hotel.address,
   #                                           "Bot", "12:01", "static/bot.png")

    #                Messages.append(replied_message)

                    return render_template("Chatbot.html", Messages=Messages)

        else:
            replied_message = Message("Sorry your question is not clear to me", "Bot", "12:01", "static/bot.png")
            Messages.append(replied_message)

    return render_template("Chatbot.html", Messages=Messages)"""

if __name__ == '__main__':
    app.run(debug=True)

