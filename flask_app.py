from datetime import datetime
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

'''
# Home Page
'''
@app.route('/')
def hello_world():
	return 'Our App is Coming Soon!!'

'''
# Help Page
'''
@app.route('/api/')
@app.route('/api/help')
def api_help():
	return render_template('api_help.html')

'''
Mock data
'''
tripDuration = {'minutes':20}
station = {'id':1}

'''
# Services
'''
@app.route('/api/bikeduration', methods = ['GET'])
def bikeDuration():
	# Read in Arguments
	start = request.args.get('start')
	end = request.args.get('end')
	weather = request.args.get('weather')
	return jsonify(tripDuration)

@app.route('/api/walkduration', methods = ['GET'])
def walkDuration():
	# Read in Arguments
	start = request.args.get('start')
	end = request.args.get('end')
	return jsonify(tripDuration)

@app.route('/api/closeststationwithbike', methods = ['GET'])
def closestStationWithBike():
	return jsonify(station)

@app.route('/api/closeststationwithdock', methods = ['GET'])
def closestStationWithDock():
	return jsonify(station)

@app.route('/api/bikepath', methods = ['GET'])
def bikePath():
	return 'NOT READY'

@app.route('/api/walkpath', methods = ['GET'])
def walkPath():
	return 'NOT READY'

'''
# Example Code And Tests
'''
@app.route('/argtest', methods =['GET'])
def argtest():
	start = request.args.get('start')
	end = request.args.get('end')
	if start is None:
		start = 'N/A'
	if end is None:
		end = 'N/A'	
	return 'start: ' + start + ' end: '+end;	

@app.route('/returnstring/')
def adhoc_test():
	return request.query_string

'''
Main Function for Running Locally
'''
if __name__ == '__main__':
	app.run(debug = True)
