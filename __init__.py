import sqlite3
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

CONECTION = sqlite3.connect('app.db', check_same_thread=False)
CURSOR = CONECTION.cursor()

