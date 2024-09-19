"""Importing json to write a .json file and requests to query API"""
import json
import requests

# Dict to store player info
player_dict = {}
COUNTER = 1

# Querying main API
URL = 'https://sports.core.api.espn.com/v2/sports/football' \
'/leagues/nfl/seasons/2023/teams/18/athletes?limit=5'
response = requests.get(URL, timeout=10, verify = False)
response = response.json()
response_list = response['items']

# Querying player API to get deatils
for url_dict in response_list:
    player_details = []
    player_resp = requests.get(url_dict['$ref'], timeout=10, verify = False)
    player_resp = player_resp.json()
    player_details.append(player_resp['firstName'])
    player_details.append(player_resp['lastName'])
    player_details.append(player_resp['age'])

    player_dict[COUNTER] = player_details
    COUNTER += 1


# Updating 2nd player age to 99
player_dict[2][2] = 99

# Deleting a player informaiton
del player_dict[3]

# Writing the output into a JSON file
with open('final.json', 'w', encoding="utf-8") as output_file:
    json.dump(player_dict,output_file)
