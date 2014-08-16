import requests, json, sys

# Use the google maps API to report the distance and trip time if walking
def googleDisDurAPI(origin, destination):
	r = requests.get('http://maps.googleapis.com/maps/api/distancematrix/json?origins='+origin+'&destinations='+destination+'&mode=walking&language=EN')
	#print(r.json())
	obj = json.loads(r.text)
	duration = obj['rows'][0]['elements'][0]['duration']['text']
	distance = obj['rows'][0]['elements'][0]['distance']['value']
	return [distance, duration];

# Read in the Station Data
# ( ID, Name, Total Docks, Latitude, Longitude)
def readStations():
	stations = []
	with open('stations.csv') as f:
		content = f.readlines()
	for line in content[1:]:
		tokens = line.split(',');
		stations.append( ( tokens[0],tokens[1],tokens[2],tokens[3],tokens[4] ) )
		#print stations[0][0]
	return stations

def returnNearestStation(origin):
	#Find the closest Station by brute force
	stations = readStations();
	closestStation = stations[0]
	minDistance = sys.maxint
	for station in stations:
		lat =  station[3]
		lon = station[4]
		address = lat+","+lon
		curdist = googleDisDurAPI(origin, address)[0]
		if(curdist < minDistance):
			minDistance = curdist
			closestStation = station
	return closestStation

# stations = readStations();
# closestStation = stations[0]
# minDistance = sys.maxint
# for station in stations:
# 	lat =  station[3]
# 	lon = station[4]
# 	address = lat+","+lon
# 	curdist = googleDisDurAPI("633 Bay St, Toronto, ON M5G 1C9", address)[0]
# 	print curdist


# station = returnNearestStation("633 Bay St, Toronto, ON M5G 1C9");
# print(station)
