from __init__ import CONECTION, CURSOR
from flask import request, jsonify, make_response

def create():
    data = request.get_json()
    if not all([data['name'], data['age'], data['id']]):
        return ("All fields are required", 400)
    CURSOR.execute('SELECT id FROM usuarios WHERE id = ?', (data['id'],))
    user = CURSOR.fetchone()
    if user:
        return ("User already exists", 400)
    CURSOR.execute('INSERT INTO usuarios (id, nombre, edad) VALUES (?, ?, ?)', (data['id'], data['name'], data['age']))
    CONECTION.commit()
    return make_response(jsonify({'message': 'User created'}), 201)
