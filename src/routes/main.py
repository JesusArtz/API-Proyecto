from flask import render_template
from __init__ import CONECTION, CURSOR
import requests

def index():

    request = requests.get('http://0.0.0.0:7014/read')
    dataDict = request.json()

    return render_template('index.html', data=dataDict)