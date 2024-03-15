# Get a list of all Cyberse monsters
# Written by Petra Lynn Vanderhei (mvanderhei2@huskers.unl.edu)
#
# Yugipedia's API and documentation is at https://yugipedia.com/api.php?action=help

import requests
import json

url_yugipedia = 'https://yugipedia.com/api.php'

query_yugipedia = 'action=ask&\
    format=json&\
    query=[[Concept%3ACG+monsters]][[Type%3A%3ACyberse]]|limit=500'

headers = {'User-Agent': 'Cyberse-GetPriceBot/0.1 (https://github.com/Brunswick-Khorasan/Cyberse-GetPrice; mvanderhei2@huskers.unl.edu)' }

response = requests.get(url_yugipedia, params=query_yugipedia, headers=headers)

json_list = json.loads(response.content)['query']['reuslts']

string_list = ''

for key in json_list:
    name = json_list[key]['fulltext']
    string_list += name + '\n'
