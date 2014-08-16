from datetime import datetime
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Our App is Coming Soon!!'

@app.route('/api/')
def api_help():
	return render_template('api_help.html')
