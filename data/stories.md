## story 01
* greet
    - utter_greet
    
## story 02
* goodbye
    - utter_goodbye
    
## story 03
* inform
    -utter_ask_city
    
## story 04
* inform
    - action_weather
## Generated Story 5156830279945553429
* greet
    - utter_greet
* inform_weather{"city": "gilgit"}
    - slot{"city": "gilgit"}
    - action_weather
    - action_default_ask_rephrase
* inform_weather
    - utter_ask_city
* inform_weather{"city": "gilgit"}
    - slot{"city": "gilgit"}
    - action_weather
* inform_weather{"city": "Skardu"}
    - slot{"city": "Skardu"}
    - action_weather

## Generated Story 3153215875198942873
* greet
    - utter_greet
* inform_weather
    - utter_ask_city
* inform_weather{"city": "gilgit"}
    - slot{"city": "gilgit"}
    - action_weather
* inform_weather{"city": "gilgit"}
    - slot{"city": "gilgit"}
    - action_weather
* goodbye
    - utter_goodbye
* inform_weather{"city": "gilgit"}
    - slot{"city": "gilgit"}
    - action_weather

## Generated Story -6218818592191921076
* greet
    - utter_greet
* inform_weather{"city": "gilgit"}
    - slot{"city": "gilgit"}
    - action_weather
    - action_restart

## Generated Story 0

## Generated Story -2452911884090309816
* inform_weather{"city": "gilgit"}
    - slot{"city": "gilgit"}
    - action_weather

## Generated Story 5988071869571764407
* inform_weather{"city": "gilgit"}
    - slot{"city": "gilgit"}
    - action_weather

## Generated Story 6449970007497154410
* inform_weather{"city": "gilgit"}
    - slot{"city": "gilgit"}
    - action_weather

## Generated Story 4669150817388182310
* inform_weather{"city": "gilgit"}
    - slot{"city": "gilgit"}
    - action_weather

## Generated Story -484466340855980840
* inform_weather{"city": "gilgit"}
    - slot{"city": "gilgit"}
    - action_weather

## Generated Story 0

## Generated Story -9008537755046641847
* inform_weather{"city": "Skardu"}
    - slot{"city": "Skardu"}
    - action_weather

## Generated Story 1054076127521894487
* inform_weather{"city": "Skardu"}
    - slot{"city": "Skardu"}
    - action_weather

## Generated Story 3601314487036446390
* greet
    - utter_greet

## Generated Story 6943098384496641460
* greet
    - utter_greet
* inform_weather{"city": "karimabad"}
    - slot{"city": "karimabad"}
    - action_weather

## Generated Story -6853679546672545298
* inform_weather{"city": "Skardu"}
    - slot{"city": "Skardu"}
    - action_weather

## Generated Story 907339365047732917
* inform_weather{"city": "Skardu"}
    - slot{"city": "Skardu"}
    - action_weather
* inform_weather{"city": "gilgit"}
    - slot{"city": "gilgit"}
    - action_weather

## Generated Story 111018850490330240
* greet
    - utter_greet
* inform_weather{"city": "gilgit"}
    - slot{"city": "gilgit"}
    - action_weather

## Generated Story -3580173527085727919
* inform_weather{"city": "gilgit"}
    - slot{"city": "gilgit"}
    - action_weather

## Generated Story -3547827718592178928
* greet
    - utter_greet

## Generated Story -8157092261500455553
* inform_weather{"city": "gilgit"}
    - slot{"city": "gilgit"}
    - action_weather

## Generated Story -5278590569829031402
* inform_weather{"city": "gilgit"}
    - slot{"city": "gilgit"}
    - action_weather

## Generated Story -2676085331221646564
* inform_weather{"city": "gilgit"}
    - slot{"city": "gilgit"}
    - action_weather

## Generated Story 8190058747689751110
* inform_weather{"city": "gilgit"}
    - slot{"city": "gilgit"}
    - action_weather

## Generated Story 4390023565677948872
* inform_weather{"city": "gilgit"}
    - slot{"city": "gilgit"}
    - action_weather

## Generated Story 5318930633978565395
* inform_weather{"city": "gilgit"}
    - slot{"city": "gilgit"}
    - action_weather

## Generated Story 5801730028275498822
* inform_weather{"city": "gilgit"}
    - slot{"city": "gilgit"}
    - action_weather
    - slot{"city": "gilgit"}


## interactive_story_1
* inform_best_hotels{"city": "gilgit"}
    - slot{"city": "gilgit"}
    - action_best_hotels
* inform_best_hotels{"city": "skardu"}
    - slot{"city": "skardu"}
    - action_best_hotels

## interactive_story_1
* inform_cheap_hotels{"city": "Gilgit"}
    - slot{"city": "Gilgit"}
    - action_cheap_hotels

## interactive_story_1
* inform_cheap_hotels{"city": "gilgit"}
    - slot{"city": "gilgit"}
    - action_cheap_hotels
* inform_cheap_hotels{"city": "skardu"}
    - slot{"city": "skardu"}
    - action_cheap_hotels

## interactive_story_1
* :inform_price{"position": "first"}
    - action_price

## interactive_story_1
* inform_price{"position": "first"}
    - slot{"position": "first"}
    - action_price

## interactive_story_1
* inform_price{"position": "second"}
    - slot{"position": "second"}
    - action_price

## interactive_story_1
* inform_fallback{"city": "gilgit"}
    - slot{"city": "gilgit"}
    - utter_fallback
* inform_fallback{"city": "gilgit"}
    - slot{"city": "gilgit"}
    - utter_fallback

## interactive_story_1
* inform_address{"position": "first"}
    - slot{"position": "first"}
    - action_address
* inform_address{"position": "fifth"}
    - slot{"position": "fifth"}
    - action_address

## interactive_story_1
* inform_picture{"position": "first"}
    - slot{"position": "first"}
    - action_picture
* inform_picture{"position": "second"}
    - slot{"position": "second"}
    - action_picture

## interactive_story_1
* inform_best_hotels{"city": "gilgit"}
    - slot{"city": "gilgit"}
    - action_best_hotels
* inform_best_hotels{"city": "kalam"}
    - slot{"city": "kalam"}
    - action_best_hotels
* inform_fallback{"city": "gilgit"}
    - slot{"city": "gilgit"}
    - utter_fallback
* inform_hotels_price{"city": "gilgit", "query": "price", "condition": "greater", "price": "2000"}
    - slot{"city": "gilgit"}
    - slot{"condition": "greater"}
    - slot{"price": "2000"}
    - slot{"query": "price"}
    - action_hotels_price
* inform_hotels_price{"city": "swat", "query": "price", "condition": "less", "price": "10000"}
    - slot{"city": "swat"}
    - slot{"condition": "less"}
    - slot{"price": "10000"}
    - slot{"query": "price"}
    - action_hotels_price

## interactive_story_1
* inform_best_hotels{"city": "gilgit"}
    - slot{"city": "gilgit"}
    - action_best_hotels

## interactive_story_1
* inform_hotels_price{"city": "swat", "query": "price", "condition": "between", "price": "2000 and 3000"}
    - slot{"city": "swat"}
    - slot{"condition": "between"}
    - slot{"price": "2000 and 3000"}
    - slot{"query": "price"}
    - action_hotels_price
* inform_hotels_price{"city": "gilgit", "query": "price", "condition": "between", "price": "2000 and 2500"}
    - slot{"city": "gilgit"}
    - slot{"condition": "between"}
    - slot{"price": "2000 and 2500"}
    - slot{"query": "price"}
    - action_hotels_price

## interactive_story_1
* inform_weather
    - utter_ask_city
* inform_weather{"city": "gilgit"}
    - slot{"city": "gilgit"}
    - action_weather
    - slot{"city": "gilgit"}
* inform_weather
    - utter_ask_city
* inform_weather{"city": "skardu"}
    - slot{"city": "skardu"}
    - action_weather
    - slot{"city": "skardu"}

## interactive_story_1
* inform_hotels_rating{"city": "gilgit", "query": "rating", "condition": "greater", "rating": "7"}
    - slot{"city": "gilgit"}
    - slot{"condition": "greater"}
    - slot{"query": "rating"}
    - slot{"rating": "7"}
    - action_hotels_rating
* inform_hotels_rating{"city": "skardu", "query": "rating", "condition": "greater", "rating": "4"}
    - slot{"city": "skardu"}
    - slot{"condition": "greater"}
    - slot{"query": "rating"}
    - slot{"rating": "4"}
    - action_hotels_rating

## interactive_story_1
* inform_tourist_spots{"city": "gilgit"}
    - slot{"city": "gilgit"}
    - action_tourist_spots
    - slot{"city": "gilgit"}
* inform_tourist_spots{"city": "skardu"}
    - slot{"city": "skardu"}
    - action_tourist_spots
    - slot{"city": "skardu"}
