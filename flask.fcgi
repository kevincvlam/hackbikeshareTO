#!/home/kevincvl/.virtualenvs/flask/bin/python 
import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from flup.server.fcgi import WSGIServer
from flask_app import app as application

WSGIServer(application).run()
