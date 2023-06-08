from __init__ import CONECTION, CURSOR
from flask import request, jsonify, make_response

def read():
    if request.method == 'GET':
        name = request.args.get('name', "")
        CURSOR.execute(f"SELECT * FROM usuarios WHERE nombre LIKE '{name}%'")
        data = CURSOR.fetchall()
        dataDict = {
            Id: {
                'name': name,
                'age': edad
            }
            for Id, name, edad in data
        }
        return make_response(jsonify(dataDict), 200)
    
    return make_response(jsonify({'message': 'Method not allowed'}), 405)
