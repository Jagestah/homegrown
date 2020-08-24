#! /bin/python3

###
# To use this code run `pip3 install -r requirements.txt`
###

import requests
# https://requests.readthedocs.io/en/master/
import pprint
# https://docs.python.org/3/library/pprint.html
import time
import sys

STARSHIP_ID = sys.argv[1]

# PrettyPrint changes ugly single-line json in to a human readable format
pp = pprint.PrettyPrinter(indent=2)

# Pull the information about some starships from the API
response = requests.get('https://swapi.dev/api/starships/')
# pp.pprint(response)

# Convert to response to JSON
response = response.json()
# pp.pprint(response)

# Give us just the list of starships from the response
starships = response["results"]
# pp.pprint(starships)

#### PUT ALL NEW CODE BELOW THIS LINE ####

# print(len(starships))

# pp.pprint(starships[0])

while True:
    success = False
    for starship in starships:
        starship_url = starship["url"].rsplit("/")
        if STARSHIP_ID in starship_url:
            print("Name: "+starship["name"])
            print("   Class: "+starship["starship_class"])
            # print(type(starship["pilots"]))
            if len(starship["pilots"]) > 0:
                print("   Pilots: ")
            for pilot in starship["pilots"]:
                # print("Pilot URL: "+pilot)
                pilot_data = requests.get(pilot)
                pilot_data_json = pilot_data.json()
                print("    "+pilot_data_json["name"])
            # print("Pilots: "+starship["pilots"])
            success = True
    if success == False:
        print("Unable to find a ship with ID "+STARSHIP_ID)
    time.sleep(10)
