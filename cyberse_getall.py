import requests

url = 'https://yugipedia.com/api.php'

query = 'action=ask&\
    format=json&\
    query=[[Concept%3ACG+monsters]][[Type%3A%3ACyberse]]|limit=500'

headers = {'User-Agent': 'Cyberse-GetPriceBot/0.1 (https://github.com/Brunswick-Khorasan/Cyberse-GetPrice; mvanderhei2@huskers.unl.edu)' }

response = requests.get(url, params=query, headers=headers)

print(response.content)
