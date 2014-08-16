import requests, json

def directions(origin, destination,mode):
	url = 'https://maps.googleapis.com/maps/api/directions/json?origin='+origin+'&destination='+destination+'&key=AIzaSyA608VM6a1x08vl6Q7h9b4IvISSjV5oMRc&mode='+mode
	r = requests.get(url)
	#print(r.json())
	return r;

# directions("633 Bay St, Toronto ON", "45 Ulster, Toronto ON")