import sqlite3
from flask import Flask


app = Flask(__name__)

CONECTION = sqlite3.connect('app.db', check_same_thread=False)
CURSOR = CONECTION.cursor()

