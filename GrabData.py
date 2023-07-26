# UTILITY
# Program to connect with League of Legends Statistical Data
# By: Alex O'Brien

import requests
import json


VERSION_URL = "https://ddragon.leagueoflegends.com/api/versions.json"


# Function to retrieve and parse json data to extract current version
# @params: none
# @return: str
def grabVersion():
    response = requests.get(VERSION_URL)
    if response.status_code == 200:
        version = json.loads(response.text)
        return version[0]
    else:
        print(f"Error: {response.status_code}")


DATA_URL = "http://ddragon.leagueoflegends.com/cdn/" + grabVersion() + "/data/en_US/champion.json"


# Function to retrieve and parse json data into a dictionary
# @params: none
# @return: dictionary
def grabData():
    response = requests.get(DATA_URL)
    if response.status_code == 200:
        data = json.loads(response.text)
        return data['data']
    else:
        print(f"Error: {response.status_code}")
