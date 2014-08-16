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

'''
# Services
'''
@app.route('/api/tripduration', methods = ['GET'])
def get_tasks():
	# Read in Arguments
	start = request.args.get('start')
	end = request.args.get('end')
	weather = request.args.get('weather')
	# Do actual stuff

    return jsonify(tripDuration)


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
	return 'start: ' + start + ' end: '+end

@app.route('/returnstring/')
def adhoc_test():
    return request.query_string

'''
Main Function for Running Locally
'''
if __name__ == '__main__':
    app.run(debug = True)
