# Get prices of every monster listed in cyberse_list.txt
# Write output to cyberse_prices.txt
# Written by Petra Lynn Vanderhei (mvanderhei2@huskers.unl.edu)
#
# YuGiOhPrice's API and documentation is at https://yugiohprices.docs.apiary.io/#
# YuGiOhPrice is at http://yugiohprices.com

import requests
import time # Rate limiting
import json

url_ygop = 'http://yugiohprices.com/api/get_card_prices/'

headers = {'User-Agent': 'Cyberse-GetPriceBot/0.1 (https://github.com/Brunswick-Khorasan/Cyberse-GetPrice; mvanderhei2@huskers.unl.edu)' }

# Clear output file
open('cyberse_prices.txt',mode='w').close()

with open('cyberse_list.txt', mode='r', encoding='utf8') as cyberse_file:
    with open('cyberse_prices.txt', mode='a', encoding='utf8') as cyberse_prices:
        for name in cyberse_file:
            name_noend = name[:-1]
            response = requests.get(url_ygop+name_noend, headers=headers)
            time.sleep(0.001) #1 ms dely between requests

            try:
                info = json.loads(response.content)['data']
                price_low = info[0]['price_data']['data']['prices']['low']
                for key in info:
                    try:
                        set_price = key['price_data']['data']['prices']['low']
                        if set_price < price_low:
                            price_low = set_price
                    except KeyError:
                        pass
                print(name_noend,price_low)
                cyberse_prices.write(name_noend+' '+str(price_low)+'\n')
            except KeyError:
                print('No price for',name_noend)
