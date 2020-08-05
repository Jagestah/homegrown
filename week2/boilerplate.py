#! python3

###
# To use this code run `pip3 install -r requirements.txt`
###

import requests
# https://requests.readthedocs.io/en/master/
import pprint
# https://docs.python.org/3/library/pprint.html

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
