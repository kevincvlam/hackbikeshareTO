import requests, json, sys, math

# Use the google maps API to report the distance and trip time if walking
def googleDisDurAPI(origin, destination):
	r = requests.get('http://maps.googleapis.com/maps/api/distancematrix/json?origins='+origin+'&destinations='+destination+'&mode=walking&language=EN')
	#print(r.json())
	obj = json.loads(r.text)
	duration = obj['rows'][0]['elements'][0]['duration']['text']
	distance = obj['rows'][0]['elements'][0]['distance']['value']
	return [distance, duration];

# One for Biking
def distDur(origin, destination, mode):
	r = requests.get('http://maps.googleapis.com/maps/api/distancematrix/json?origins='+origin+'&destinations='+destination+'&mode='+mode+'&language=EN')
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
	# Get Coordinates of Origin
	uri = 'http://open.mapquestapi.com/geocoding/v1/address?key=Fmjtd%7Cluur25ut2h%2C2a%3Do5-9w70l0&callback=renderOptions&inFormat=kvp&outFormat=json&location='+origin+'&thumbMaps=false&maxResults=1'
	#print uri
	geocodeResp = requests.get(uri)
	jsonText = geocodeResp.text
	jsonText = jsonText[jsonText.index('(')+1:jsonText.index(')')]
	#print jsonText
	obj = json.loads(jsonText)
	#print(obj)
	latitude = obj['results'][0]['locations'][0]['latLng']['lat']
	longitude = obj['results'][0]['locations'][0]['latLng']['lng']
	latitude = math.radians(latitude)
	longitude = math.radians(longitude)

	#Find the closest Station by brute force
	stations = readStations();
	closestStation = stations[0]
	minDistance = sys.maxint
	for station in stations:
		lat = math.radians(float(station[3]))
		lon = math.radians(float(station[4]))
		# Calculate Distance
		# R = 6371 # Radius of the Earth
		# theta1 = latitude
		# theta2 = lat 
		# delTheta = (lat-latitude)
		# delLamda = (lon-longitude)

		# a = math.sin(delTheta/2)*math.sin(delTheta/2)
		# + math.cos(theta1)*math.cos(theta2)*math.sin(delLamda/2)*math.sin(delLamda/2)

		# c = 2 * math.atan(math.sqrt(a)/math.sqrt(1-a))

		# curdist = R * c
		curdist = math.sqrt((lat-latitude)*(lat-latitude)+(lon-longitude)*(lon-longitude))
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
