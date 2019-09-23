import os
import requests
import json
import pandas as pd

def querys(cat_ID):
    url = 'https://api.foursquare.com/v2/venues/explore'
    params= dict(
            client_id='HIX31VQGRL1GODLF1XYQO5ERLH1WBFWLLCAPWYHLNATD55JC',
            client_secret= '3CVWFRJLEFHRKVT3HCMGEAK1ZOW1NZU3OAUOSRP2AGOTLIC2',
            v='20180323',
            ll='37.781265, -122.393229',
            categoryId = cat_ID,
            radius = 1000
    )
    respoco = requests.get(url=url, params=params)
    return guarde(json.loads(respoco.text))

def guarde(lugare):
   name=[]
   lat=[]
   lng=[]
   for e in lugare['response']['groups'][0]['items']:
       name.append(e['venue']['name'])
       lat.append(e['venue']['location']['lat'])
       lng.append(e['venue']['location']['lng'])
   
   lugare = {"name":name, "latitude":lat, "longitude":lng}
   return pd.DataFrame(lugare)

def call_APIs(lst):
    return [querys(id) for id in lst]


if __name__ == "__main__":
    lst = ["5744ccdfe4b0c0459246b4c7", "4bf58dd8d48988d11f941735"]
    a = (call_APIs(lst))

    for ele in a: 
        print(ele)
        print("---------------------------------")
