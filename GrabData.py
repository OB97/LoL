# Program to connect with League of Legends Statistical Data
# By: Alex O'Brien

import requests
import json
import pprint

API_KEY = "RGAPI-2385d6ea-9a68-4b03-be76-30b771b3e843"
DATA_URL = "http://ddragon.leagueoflegends.com/cdn/13.13.1/data/en_US/champion.json"


def main():
    response = requests.get(DATA_URL)
    if response.status_code == 200:
        data = json.loads(response.text)
        pprint.pprint(data['data'])
    else:
        print(f"Error: {response.status_code}")


if __name__ == "__main__":
    main()
