from __init__ import CONECTION, CURSOR
from flask import request, jsonify, make_response

def create():
    if request.method == 'POST':
        data = request.get_json()
        if not all([data['name'], data['edad'], data['id']]):
            return make_response(jsonify({'message': 'All fields are required'}), 400)
        CURSOR.execute('SELECT id FROM usuarios WHERE id = ?', (data['id'],))
        user = CURSOR.fetchone()
        if user:
            return make_response(jsonify({'message': 'User already exists'}), 400)
        CURSOR.execute('INSERT INTO usuarios (id, nombre, edad) VALUES (?, ?, ?)', (data['id'], data['name'], data['edad']))
        CONECTION.commit()
        return make_response(jsonify({'message': 'User created'}), 201)
    else:
        return make_response(jsonify({'message': 'Method not allowed'}), 405)