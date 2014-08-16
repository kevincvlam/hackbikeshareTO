import requests, json

def googleDistance(origin, destination):
	r = requests.get('http://maps.googleapis.com/maps/api/distancematrix/json?origins='+origin+'&destinations='+destination+'&mode=walking&language=EN')
	print(r.json())
	return r;

response = googleDistance("43.7,-79.4", "Ottawa,ON");
obj = json.loads(response.text)
print(obj['rows'][0]['elements'][0]['duration']['text'])