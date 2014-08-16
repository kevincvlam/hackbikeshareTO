import requests, json
# from neareststation import returnNearestStation

# station = returnNearestStation("633 Bay St, Toronto, ON M5G 1C9");
# print(station)

######


r = requests.get('http://maps.googleapis.com/maps/api/distancematrix/json?origins=Toronto,ON&destinations=Ottawa,ON&mode=walking&language=EN')
#print(r.json())
obj = json.loads(r.text)
print(obj);
# duration = obj['rows'][0]['elements'][0]['duration']['text']
# distance = obj['rows'][0]['elements'][0]['distance']['value']
