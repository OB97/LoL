# UTILITY
# Program to connect with League of Legends Statistical Data
# By: Alex O'Brien

import requests
import json
import Champion


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


# get data by field name -
## info, partype, stats, tags
# @params: field name
# @return: [str,{str}]
def getByField(f):
    d = grabData()
    fData = []
    for champ in d.keys():
        fData.append([champ, d[champ][f]])
    return fData


# set up list of champion objects
# @params: none
# @return: {str:obj}
def setChamps():
    champObjs = {}
    for obj in getByField("stats"):
        champObjs[obj[0]] = Champion.Champion(obj[0], getByField("stats"))
    return champObjs
