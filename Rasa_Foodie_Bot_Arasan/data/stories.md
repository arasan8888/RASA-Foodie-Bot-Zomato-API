## complete path
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_t1t2_location
    - slot{"check_loc": "True"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_price_preference
* restaurant_search{"price": "below_300"}
    - slot{"price": "below_300"}
    - action_search_restaurants
* affirm
    - utter_enterEmail
* get_email{"email" : "abcd1234@gmail.com"}
    - send_email
    - utter_goodbye
    - action_restart


## complete path 9
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - action_t1t2_location
    - slot{"check_loc": "True"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_price_preference
* restaurant_search{"price": "below_300"}
    - slot{"price": "below_300"}
    - action_search_restaurants
* deny
    - utter_goodbye
    - action_restart

## complete path 5
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_t1t2_location
    - slot{"check_loc": "False"}
    - utter_locationNotServiced
    - utter_goodbye
    - action_restart

## location specified 1
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_t1t2_location
    - slot{"check_loc": "True"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_price_preference
* restaurant_search{"price": "below_700"}
    - slot{"price": "below_700"}
    - action_search_restaurants
* affirm
    - utter_enterEmail
* get_email{"email" : "george.bush@hotmail.com"}
    - send_email
    - utter_goodbye
    - action_restart

## location specified 3
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_t1t2_location
    - slot{"check_loc": "True"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_price_preference
* restaurant_search{"price": "below_700"}
    - slot{"price": "below_700"}
    - action_search_restaurants
* deny
    - utter_goodbye
    - action_restart

## location specified 2
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_t1t2_location
    - slot{"check_loc": "False"}
    - utter_locationNotServiced
    - utter_goodbye
    - action_restart

## complete path 2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - action_t1t2_location
    - slot{"check_loc": "True"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_price_preference
* restaurant_search{"price": "above_700"}
    - slot{"price": "above_700"}
    - action_search_restaurants
* affirm
    - utter_enterEmail
* get_email{"email" : "george.bush@hotmail.com"}
    - send_email
    - utter_goodbye
    - action_restart


## complete path 10
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - action_t1t2_location
    - slot{"check_loc": "True"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_price_preference
* restaurant_search{"price": "above_700"}
    - slot{"price": "above_700"}
    - action_search_restaurants
* deny
    - utter_goodbye
    - action_restart

## complete path 6
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - action_t1t2_location
    - slot{"check_loc": "False"}
    - utter_locationNotServiced
    - utter_goodbye
    - action_restart

# complete path 3
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - action_t1t2_location
    - slot{"check_loc": "True"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_price_preference
* restaurant_search{"price": "above_700"}
    - slot{"price": "above_700"}
    - action_search_restaurants
* affirm
    - utter_enterEmail
* get_email{"email" : "george.bush@hotmail.com"}
    - send_email
    - utter_goodbye
    - action_restart

## complete path 11
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - action_t1t2_location
    - slot{"check_loc": "True"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_price_preference
* restaurant_search{"price": "above_700"}
    - slot{"price": "above_700"}
    - action_search_restaurants
* deny
    - utter_goodbye
    - action_restart


## complete path 7
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - action_t1t2_location
    - slot{"check_loc": "False"}
    - utter_locationNotServiced
    - utter_goodbye
    - action_restart

## complete path 4
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_t1t2_location
    - slot{"check_loc": "True"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_price_preference
* restaurant_search{"price": "below_700"}
    - slot{"price": "below_700"}
    - action_search_restaurants
* affirm
    - utter_enterEmail
* get_email{"email" : "ravi_kishan9999@gmail.com"}
    - send_email
    - utter_goodbye
    - action_restart


## complete path 12
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_t1t2_location
    - slot{"check_loc": "True"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_price_preference
* restaurant_search{"price": "below_700"}
    - slot{"price": "below_700"}
    - action_search_restaurants
* deny
    - utter_goodbye
    - action_restart


## complete path 8
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_t1t2_location
    - slot{"check_loc": "False"}
    - utter_locationNotServiced
    - utter_goodbye
    - action_restart

## cuisine_specified_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_t1t2_location
    - slot{"check_loc": "True"}
    - utter_price_preference
* restaurant_search{"price": "below_700"}
    - slot{"price": "below_700"}
    - action_search_restaurants
* affirm
    - utter_enterEmail
* get_email{"email" : "ravi_kishan99@gmail.com"}
    - send_email
    - utter_goodbye
    - action_restart

## cuisine_specified_3
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_t1t2_location
    - slot{"check_loc": "True"}
    - utter_price_preference
* restaurant_search{"price": "below_700"}
    - slot{"price": "below_700"}
    - action_search_restaurants
* deny
    - utter_goodbye
    - action_restart


## cuisine_specified_2
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_t1t2_location
    - slot{"check_loc": "False"}
    - utter_locationNotServiced
    - utter_goodbye
    - action_restart

## price_specified_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"price": "below_300"}
    - slot{"price": "below_300"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_t1t2_location
    - slot{"check_loc": "True"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
* affirm
    - utter_enterEmail
* get_email{"email" : "ravi_kishan99@gmail.com"}
    - send_email
    - utter_goodbye
    - action_restart


## price_specified_3
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"price": "below_300"}
    - slot{"price": "below_300"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_t1t2_location
    - slot{"check_loc": "True"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
* deny
    - utter_goodbye
    - action_restart


## price_specified_2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"price": "below_300"}
    - slot{"price": "below_300"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_t1t2_location
    - slot{"check_loc": "False"}
    - utter_locationNotServiced
    - utter_goodbye
    - action_restart

## cuisineandlocation_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - action_t1t2_location
    - slot{"check_loc": "True"}
    - utter_price_preference
* restaurant_search{"price": "below_700"}
    - slot{"price": "below_700"}
    - action_search_restaurants
* affirm
    - utter_enterEmail
* get_email{"email" : "ravi_kishan99@gmail.com"}
    - send_email
    - utter_goodbye
    - action_restart


## cuisineandlocation_story_3
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - action_t1t2_location
    - slot{"check_loc": "True"}
    - utter_price_preference
* restaurant_search{"price": "below_700"}
    - slot{"price": "below_700"}
    - action_search_restaurants
* deny
    - utter_goodbye
    - action_restart


## cuisineandlocation_story_2
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - action_t1t2_location
    - slot{"check_loc": "False"}
    - utter_locationNotServiced
    - utter_goodbye
    - action_restart


## happy_path
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "mumbai"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
    - action_t1t2_location
    - slot{"check_loc": "True"}
    - utter_price_preference
* restaurant_search{"price": "above_700"}
    - slot{"price": "above_700"}
    - action_search_restaurants
* affirm
    - utter_enterEmail
* get_email{"email" : "ravi_kishan99@gmail.com"}
    - send_email
    - utter_goodbye
    - action_restart


## happy_path_3
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "mumbai"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
    - action_t1t2_location
    - slot{"check_loc": "True"}
    - utter_price_preference
* restaurant_search{"price": "above_700"}
    - slot{"price": "above_700"}
    - action_search_restaurants
* deny
    - utter_goodbye
    - action_restart


## happy_path_2
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "mumbai"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
    - action_t1t2_location
    - slot{"check_loc": "False"}
    - utter_locationNotServiced
    - utter_goodbye
    - action_restart



## cuisine_specified_4
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_location
* restaurant_search{"location": "jaipur"}
    - slot{"location": "jaipur"}
    - action_t1t2_location
    - slot{"check_loc": "True"}
    - utter_price_preference
* restaurant_search{"price": "below_700"}
    - slot{"price": "below_700"}
    - action_search_restaurants
* affirm
    - utter_enterEmail
* get_email{"email" : "ravi_kishan99@gmail.com"}
    - send_email
    - utter_goodbye
    - action_restart

## cuisine_specified_5
* greet
    - utter_greet
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "south indian"}
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_t1t2_location
    - slot{"check_loc": "True"}
    - utter_price_preference
* restaurant_search{"price": "above_700"}
    - slot{"price": "above_700"}
    - action_search_restaurants
* deny
    - utter_goodbye
    - action_restart


## cuisine_specified_6
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_location
* restaurant_search{"location": "hyderabad"}
    - slot{"location": "mumbai"}
    - action_t1t2_location
    - slot{"check_loc": "False"}
    - utter_locationNotServiced
    - utter_goodbye
    - action_restart


## happy_path4
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "mumbai", "price": "above_700"}
    - slot{"cuisine": "italian"}
    - slot{"price": "above_700"}
    - slot{"location": "mumbai"}
    - action_t1t2_location
    - slot{"check_loc": "True"}
    - action_search_restaurants
* affirm
    - utter_enterEmail
* get_email{"email" : "ravi_kishan99@gmail.com"}
    - send_email
    - utter_goodbye
    - action_restart


## happy_path5
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "mumbai", "price": "below_700"}
    - slot{"cuisine": "italian"}
    - slot{"price": "below_700"}
    - slot{"location": "mumbai"}
    - action_t1t2_location
    - slot{"check_loc": "True"}
    - action_search_restaurants
* deny
    - utter_goodbye
    - action_restart


## happy_path6
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "mumbai", "price": "below_300"}
    - slot{"cuisine": "italian"}
    - slot{"price": "below_300"}
    - slot{"location": "mumbai"}
    - action_t1t2_location
    - slot{"check_loc": "False"}
    - utter_locationNotServiced
    - utter_goodbye
    - action_restart
