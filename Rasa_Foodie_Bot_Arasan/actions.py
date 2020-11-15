from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
import smtplib
from smtplib import SMTPException

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
import json

class ActionSearchRestaurants(Action):
        def name(self):
                return 'action_search_restaurants'

        def run(self, dispatcher, tracker, domain):
                config={ "user_key":"Enter your Key here"}
                zomato = zomatopy.initialize_app(config)
                loc = tracker.get_slot('location')
                cuisine = tracker.get_slot('cuisine')
                location_detail=zomato.get_location(loc, 1)
                price = tracker.get_slot('price')
                d1 = json.loads(location_detail)
                lat=d1["location_suggestions"][0]["latitude"]
                lon=d1["location_suggestions"][0]["longitude"]
                cuisines_dict={'chinese':25,'Mexican':73,'italian':55,'American':1,'south indian':85,'north indian':50}
                results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 100)
                d = json.loads(results)
                response=""
                if d['results_found'] == 0:
                                response= "no results"
                                dispatcher.utter_message("-----"+response)
                                return [SlotSet('location',loc)]

                new_data = []



                def filter_restaurants_price(price, restaurants):
                                """
                                Takes budget, restaurants list and filters the list of restaurants
                                based on the budget of user.
                                """
                                price_filter = {"below_300": list(filter(
                                                lambda restaurant: restaurant["restaurant"]["average_cost_for_two"] < 300, restaurants)),
                                                "below_700": list(filter(lambda restaurant: 300 < restaurant["restaurant"]["average_cost_for_two"] < 700, restaurants)),
                                                "above_700": list(filter(lambda restaurant: restaurant["restaurant"]["average_cost_for_two"]> 700,restaurants,))}
                                return price_filter.get(price)

                restaurants = filter_restaurants_price(price, d["restaurants"])

                for restaurant in restaurants:
                                new_restaurant = {}

                                new_restaurant.update({"name": restaurant["restaurant"]["name"]})
                                new_restaurant.update({"address": restaurant["restaurant"]["location"]["address"]})
                                new_restaurant.update({"cost_for_two": restaurant["restaurant"]["average_cost_for_two"]})
                                new_restaurant.update({"rating": restaurant["restaurant"]["user_rating"]["aggregate_rating"]})
                                new_restaurant.update({"cusine": restaurant["restaurant"]["cuisines"]})
                                new_data.append(new_restaurant)


                x = sorted(new_data, key=lambda x: float(x["rating"]), reverse=True)

                # Top five restaurants based on rating
                response = "\nRestaurant List\n\n"
                for restaurant in x[:5]:
                                response += "{} located at {} costs an average of {} for two and has been rated {} stars.\n\n".format(restaurant["name"],restaurant["address"],
                                restaurant["cost_for_two"], restaurant["rating"])

                responseforemail = "\nRestaurant List\n\n"
                for restaurant in x[:10]:
                                responseforemail += "{} located at {} costs an average of {} for two and has been rated {} stars.\n\n".format(restaurant["name"],restaurant["address"],
                                restaurant["cost_for_two"], restaurant["rating"])

                file_path = "./data/restaurants.txt"
                with open(file_path, "w") as file_open:
                        file_open.write(responseforemail)


                dispatcher.utter_message(response)
                emailask = "\n\nDo you want us to email the Top 10 restaurants for your selected criteria to your email address? \n\n"
                dispatcher.utter_message("\n\n")
                dispatcher.utter_message(emailask)


class ActionT1T2Location(Action):
    """
    Validate only TIER-I & TIER-II cities Locations are served
    """

    def name(self):
        return "action_t1t2_location"

    def run(self, dispatcher, tracker, domain):
        config={ "user_key":"Enter your Key Here"}
        zomato = zomatopy.initialize_app(config)
        location = tracker.get_slot("location")
        location_list = open("./data/tier1&2_cities.txt").read().split("\n")
        if location in location_list:
                return [SlotSet("check_loc", True)]
        else:
                return [SlotSet("check_loc", False)]

class sendemail(Action):

         def name(self):
                 return "send_email"

         def run(self, dispatcher, tracker, domain):

             try:

                 message = open("./data/restaurants.txt").read()
                 email = tracker.get_slot("email")
                 sender_email_id = "Enter Sender Email ID"
                 sender_email_id_password = "Enter Password here"
                 s = smtplib.SMTP('smtp.gmail.com', 587)
                 s.starttls()
                 s.login(sender_email_id, sender_email_id_password)
                 s.sendmail(sender_email_id, email, message)
                 s.quit
                 return [dispatcher.utter_message("Email Sent!")]

             except SMTPException:
                 return [dispatcher.utter_message("Error in sending Email!")]
