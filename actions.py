from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import pandas as pd
import requests
from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import os

bot_messages = []
user_messages = []

position_dictionary = {"first": 1, "second": 2, "third": 3, "fourth": 4, "fifth": 5, "sixth": 6, "seventh": 7,
                        "eight": 8, "ninth": 9, "tenth": 10, "eleventh": 11, "twelfth": 12, "thirteenth": 13,
                        "fourteenth": 14, "fifteenth": 15, "sixteenth": 16, "seventeenth": 17, "eighteenth": 18,
                        "nineteenth": 19, "twentieth": 20}


cities = ["gilgit", "skardu", "astore", "chitral", "chilas", "gulmit", "naran", "khaplu", "karimabad", "kalam", "gakuch"]

tourist_spots = {"karimabad": ["Baltit Fort", "Altit Fort", "Ultar Base Camp", "Ganish Village", "Cafe De Hunza"],
                "chitral": ["Tirich Mir", "Chitral Museum", "Shahi Masjid", "Shahi Qila", "Gram Chashma"],
                "naran": ["Saif ul Malook Lake", "Babusar Top", "Lulusar Lake", "Ansoo Lake"],
                "skardu": ["Deosai National Park", "Basho Valley", "Katpana Cold Desert", "Manthal Buddha Rock Carvings", "Shigar Valley"],
                "gilgit": ["Atabad Lake", "Phandar Valley", "Naltar Lake", "Rakaposhi"]
                }

class ActionWeather(Action):
    def name(self):
        return "action_weather"

    def run(self, dispatcher, tracker, domain):
        message = tracker.latest_message['text']
        loc = tracker.get_slot('city')

        if message == "in " + loc or message == "In " + loc or message == "IN " + loc:
            try:
                event = tracker.events[len(tracker.events) - 4]['text']
            except KeyError:
                dispatcher.utter_message("I am sorry I can't understand you")
                return[]

            if event == "In which city?": 
                if loc in cities:
                    base_url = "http://api.openweathermap.org/data/2.5/weather?"
                    api_key = "410463b3935acea56c8171825dbb4440"
                    complete_url = base_url + "appid=" + api_key + "&q=" + loc + "&units=metric"
                    response = requests.get(complete_url)
                    x = response.json()
                    try:
                        y = x["main"]
                    except KeyError:
                        dispatcher.utter_message("I do not have the weather information about this city")
                        return []
                    try:
                        current_temperature = y["temp"]
                    except KeyError:
                        dispatcher.utter_message("I do not have the weather information about this city")
                        return []
                    try:
                        z = x["weather"]
                    except KeyError:
                        dispatcher.utter_message("I do not have the weather information about this city")
                        return []
                    weather_description = z[0]["description"]

                    response = "The Temprature in " + loc + " is " + str(
                        current_temperature) + " degree celcius " + " and the weather is " + weather_description

                    bot_messages.append(response)
                    dispatcher.utter_message(response)
                        #dispatcher.utter_message(template="utter_greet", image_path="static/Gilgit.jpg")
                        #print(bot_messages)
                    return [SlotSet('city', loc)]
                else:
                    dispatcher.utter_message("I do not have the weather information about this city")
                    return []

        if loc is None:
            dispatcher.utter_ask_city()
            return []

        else:
            if loc in cities:
                base_url = "http://api.openweathermap.org/data/2.5/weather?"
                api_key = "410463b3935acea56c8171825dbb4440"
                complete_url = base_url + "appid=" + api_key + "&q=" + loc + "&units=metric"
                response = requests.get(complete_url)
                x = response.json()
                try:
                    y = x["main"]
                except KeyError:
                    dispatcher.utter_message("I do not have the weather information about this city")
                    return []
                try:
                    current_temperature = y["temp"]
                except KeyError:
                    dispatcher.utter_message("I do not have the weather information about this city")
                    return []
                try:
                    z = x["weather"]
                except KeyError:
                    dispatcher.utter_message("I do not have the weather information about this city")
                    return []
                weather_description = z[0]["description"]

                response = "The Temprature in " + loc + " is " + str(
                    current_temperature) + " degree celcius " + " and the weather is " + weather_description

                bot_messages.append(response)
                dispatcher.utter_message(response)
                #dispatcher.utter_message(template="utter_greet", image_path="static/Gilgit.jpg")
                #print(bot_messages)
                return [SlotSet('city', loc)]
            else:
                dispatcher.utter_message("I do not have the weather information about this city")
                return []


def preprocess(x):
    if "PKR" in str(x):
        y = x.split(' ')
        y[1] = y[1].replace(',', '')
        return float(y[1])

    else:
        x = x.replace(',', '')
        return float(x)

def preprocess_ratings(x):
    return float(x)

class ActionBestHotels(Action):
    def name(self):
        return "action_best_hotels"

    def run(self, dispatcher, tracker, domain):

        loc = tracker.get_slot('city')
        filepath = "./scrapped data/" + loc.lower() + "/Hotels.csv"

        hotels = pd.read_csv(filepath)

        hotels["Rating"] = hotels["Rating"].apply(preprocess_ratings)

        hotels.sort_values(by="Rating", inplace=True, ascending=False)

        response = "The best hotels in " + loc + " are\n\n1. " + hotels.iloc[0]["Hotel Name"] + "\n\n2. " + hotels.iloc[1]["Hotel Name"] + "\n\n3. " + hotels.iloc[2]["Hotel Name"]
        bot_messages.append(response)
        #print(bot_messages)
        dispatcher.utter_message(response)

        return []


class ActionCheapHotels(Action):
    def name(self):
        return "action_cheap_hotels"

    def run(self, dispatcher, tracker, domain):

        loc = tracker.get_slot('city')
        filepath = "./scrapped data/" + loc.lower() + "/Hotels.csv"

        hotels = pd.read_csv(filepath)

        hotels = hotels.dropna()

        print(hotels["Price"])

        hotels["Price"] = hotels["Price"].apply(preprocess)

        hotels.sort_values(by="Price", inplace=True)

        response = "The cheapest hotels in " + loc + " are\n\n1. " + hotels.iloc[0]["Hotel Name"] + "\n\n2. " + hotels.iloc[1]["Hotel Name"] + "\n\n3. " + hotels.iloc[2]["Hotel Name"]
        bot_messages.append(response)
        #print(bot_messages)
        dispatcher.utter_message(response)

        return []



class ActionPrice(Action):
    def name(self):
        return "action_price"

    def run(self, dispatcher, tracker, domain):

        pos = tracker.get_slot('position')
        last_messsage = bot_messages[len(bot_messages) - 1]

        last_messsage_list = last_messsage.split('\n\n')
        message1 = last_messsage_list[0].split(' ')

        city = ""
        if message1[3] in os.listdir('./scrapped data'):
            city = message1[3]

        else:
            city = message1[4]

        if pos in list(position_dictionary.keys()):
            filepath = "./scrapped data/" + city.lower() + "/Hotels.csv"
            message2 = ""
            hotel = ""
            try:
                message2 = last_messsage_list[position_dictionary[pos]].split('.')
                hotel = message2[1]
            except IndexError:
                dispatcher.utter_message("The position you asked for is not available")
                return []
            hotels = pd.read_csv(filepath)

            hotel = hotel[1:]
            #price = hotels.loc[hotels["Hotel Name"] == hotel]["Price"]

            response = "The price of the hotel " + hotel + " is " + hotels[hotels["Hotel Name"] == hotel]["Price"].item() + " per night"

            dispatcher.utter_message(response)

            return []

        else:
            response = "I am sorry, I can't understand you."
            dispatcher.utter_message(response)
            return []



class ActionAddress(Action):
    def name(self):
        return "action_address"

    def run(self, dispatcher, tracker, domain):

        pos = tracker.get_slot('position')
        last_messsage = bot_messages[len(bot_messages) - 1]

        last_messsage_list = last_messsage.split('\n\n')
        message1 = last_messsage_list[0].split(' ')
        city = ""
        if message1[3] in os.listdir('./scrapped data'):
            city = message1[3]

        else:
            city = message1[4]

        if pos in list(position_dictionary.keys()):
            filepath = "./scrapped data/" + city.lower() + "/Hotels.csv"
            message2 = ""
            hotel = ""
            try:
                message2 = last_messsage_list[position_dictionary[pos]].split('.')
                hotel = message2[1]
            except IndexError:
                dispatcher.utter_message("The position you asked for is not available")
                return []
            hotels = pd.read_csv(filepath)

            hotel = hotel[1:]
            #price = hotels.loc[hotels["Hotel Name"] == hotel]["Price"]

            response = "The address of the hotel " + hotel + " is " + hotels[hotels["Hotel Name"] == hotel]["Address"].item()

            dispatcher.utter_message(response)

            return []

        else:
            response = "I am sorry, I can't understand you."
            dispatcher.utter_message(response)
            return []

        
            
class ActionPicture(Action):
    def name(self):
        return "action_picture"

    def run(self, dispatcher, tracker, domain):

        pos = tracker.get_slot('position')
        last_messsage = bot_messages[len(bot_messages) - 1]

        last_messsage_list = last_messsage.split('\n\n')
        message1 = last_messsage_list[0].split(' ')
        if message1[3] in os.listdir('./scrapped data'):
            city = message1[3]

        else:
            city = message1[4]

        if pos in list(position_dictionary.keys()):
            filepath = "./scrapped data/" + city.lower() + "/Hotels.csv"
            message2 = ""
            hotel = ""
            try:
                message2 = last_messsage_list[position_dictionary[pos]].split('.')
                hotel = message2[1]
            except IndexError:
                dispatcher.utter_message("The position you asked for is not available")
                return []
            hotels = pd.read_csv(filepath)

            hotel = hotel[1:]
            #price = hotels.loc[hotels["Hotel Name"] == hotel]["Price"]

            name = hotels[hotels["Hotel Name"] == hotel]["Hotel Name"].item()

            dispatcher.utter_message(template="utter_picture", image_path="./static/img/" + name.lower() + ".jpg")

            return []

        else:
            response = "I am sorry, I can't understand you."
            dispatcher.utter_message(response)
            return []


class ActionHotelsPrice(Action):
    def name(self):
        return "action_hotels_price"

    def run(self, dispatcher, tracker, domain):
        query = tracker.get_slot('query')
        condition = tracker.get_slot('condition')
        price = tracker.get_slot('price')
        city = tracker.get_slot('city')
        
        if query.lower() == 'price':
            if condition == 'less':
                int_price = float(price)
                filepath = "./scrapped data/" + city.lower() + "/Hotels.csv"

                hotels = pd.read_csv(filepath)

                hotels = hotels.dropna()

                hotels["Price"] = hotels["Price"].apply(preprocess)

                hotels_condition = hotels[hotels["Price"] <= int_price]

                response = "The hotels in " + city + " having price less than " + price + " are\n\n"
                i=0
                for hotel in hotels_condition["Hotel Name"]:
                    response += str(i) + '. '
                    response += hotel 
                    response += "\n\n"
                    i+=1

                dispatcher.utter_message(response)
                bot_messages.append(response)
                return []

            elif condition == 'greater':
                int_price = float(price)
                filepath = "./scrapped data/" + city.lower() + "/Hotels.csv"

                hotels = pd.read_csv(filepath)

                hotels["Price"] = hotels["Price"].apply(preprocess)

                hotels_condition = hotels[hotels["Price"] >= int_price]

                response = "The hotels in " + city + " having price greater than " + price + " are\n\n"
                i=0
                for hotel in hotels_condition["Hotel Name"]:
                    response += str(i) + '. '
                    response += hotel 
                    response += "\n\n"
                    i+=1

                dispatcher.utter_message(response)
                bot_messages.append(response)
                return []

            elif condition == 'between':
                price_array = price.split(' ')
                lower_limit = float(price_array[0])
                upper_limit = float(price_array[2])

                filepath = "./scrapped data/" + city.lower() + "/Hotels.csv"

                hotels = pd.read_csv(filepath)

                hotels["Price"] = hotels["Price"].apply(preprocess)

                hotels_condition = hotels[(hotels["Price"] >= lower_limit) & (hotels["Price"] <= upper_limit)]

                response = "The hotels in " + city + " having price between " + price + " are\n\n"
                i=0
                for hotel in hotels_condition["Hotel Name"]:
                    response += str(i) + '. '
                    response += hotel 
                    response += "\n\n"
                    i+=1

                dispatcher.utter_message(response)
                bot_messages.append(response)
                return []

            else:
                dispatcher.utter_message("I am sorry I can't understand you")
                return []


class ActionHotelsRating(Action):
    def name(self):
        return "action_hotels_rating"

    def run(self, dispatcher, tracker, domain):
        query = tracker.get_slot('query')
        condition = tracker.get_slot('condition')
        rating = tracker.get_slot('rating')
        city = tracker.get_slot('city')
        
        if query.lower() == 'rating':
            if condition == 'less':
                float_rating = float(rating)
                filepath = "./scrapped data/" + city.lower() + "/Hotels.csv"

                hotels = pd.read_csv(filepath)

                hotels["Rating"] = hotels["Rating"].apply(preprocess_ratings)

                hotels_condition = hotels[hotels["Rating"] <= float_rating]

                response = "The hotels in " + city + " having rating less than " + rating + " are\n\n"
                i=0
                for hotel in hotels_condition["Hotel Name"]:
                    response += str(i) + '. '
                    response += hotel 
                    response += "\n\n"
                    i+=1

                dispatcher.utter_message(response)
                bot_messages.append(response)
                return []

            elif condition == 'greater':
                float_rating = float(rating)
                filepath = "./scrapped data/" + city.lower() + "/Hotels.csv"

                hotels = pd.read_csv(filepath)

                hotels["Rating"] = hotels["Rating"].apply(preprocess_ratings)

                hotels_condition = hotels[hotels["Rating"] >= float_rating]

                response = "The hotels in " + city + " having rating greater than " + rating + " are\n\n"
                i=0
                for hotel in hotels_condition["Hotel Name"]:
                    response += str(i) + '. '
                    response += hotel 
                    response += "\n\n"
                    i+=1

                dispatcher.utter_message(response)
                bot_messages.append(response)
                return []

            else:
                dispatcher.utter_message("I am sorry I can't understand you")
                return []



class ActionTouristSpots(Action):
    def name(self):
        return "action_tourist_spots"

    def run(self, dispatcher, tracker, domain):
        city = tracker.get_slot('city')

        if city in list(tourist_spots.keys()):
            spots = tourist_spots[city.lower()]

            response = "The tourist spots in " + city + " are\n\n"

            i=1
            for spot in spots:
               response += str(i) + '. '
               response += spot
               response += "\n\n"
               i+=1 

            dispatcher.utter_message(response)

            return [SlotSet('city', city)]

        else:
            dispatcher.utter_message("I don't have information about this city")
            return []