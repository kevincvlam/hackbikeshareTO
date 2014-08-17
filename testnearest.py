import requests, json
from neareststation import returnNearestStation

station = returnNearestStation("276 King St W, Toronto ON");
print(station)

######


# r = requests.get('http://maps.googleapis.com/maps/api/distancematrix/json?origins=Toronto,ON&destinations=Ottawa,ON&mode=walking&language=EN')
# #print(r.json())
# obj = json.loads(r.text)
# print(obj);
# duration = obj['rows'][0]['elements'][0]['duration']['text']
# distance = obj['rows'][0]['elements'][0]['distance']['value']
