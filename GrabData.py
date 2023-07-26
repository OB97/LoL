# Program to connect with League of Legends Statistical Data
# By: Alex O'Brien

import requests
import json

_DATA_URL = "http://ddragon.leagueoflegends.com/cdn/13.13.1/data/en_US/champion.json"


# Function to retrieve and parse json data into a dictionary
# @params: none
# @return: dictionary
def getData():
    response = requests.get(_DATA_URL)
    if response.status_code == 200:
        data = json.loads(response.text)
        return data['data']
    else:
        print(f"Error: {response.status_code}")
