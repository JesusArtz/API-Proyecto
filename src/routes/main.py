from flask import render_template
from __init__ import CONECTION, CURSOR


def index():

    CURSOR.execute(f"SELECT * FROM usuarios")
    data = CURSOR.fetchall()
    dataDict = {
        Id: {
            'name': name,
            'age': edad
        }
        for Id, name, edad in data
    }

    return render_template('index.html', data=dataDict)
