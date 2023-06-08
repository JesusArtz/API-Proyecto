from __init__ import CONECTION, CURSOR
from flask import request, jsonify, make_response

def update():
    if request.method == 'PUT':
        data = request.get_json()
  
        if not all([data['newName'], data['newAge'], data['id']]):
            return make_response(jsonify({'message': 'All fields are required'}), 400)
        
        CURSOR.execute('SELECT id FROM usuarios WHERE id = ?', (data['id'],))
        user = CURSOR.fetchone()
        if not user:
            return make_response(jsonify({'message': 'User does not exists'}), 400)
        CURSOR.execute('UPDATE usuarios SET nombre = ?, edad = ? WHERE id = ?', (data['newName'], data['newAge'], data['id']))
        CONECTION.commit()
        return make_response(jsonify({'message': 'User updated'}), 200)
    else:
        return make_response(jsonify({'message': 'Method not allowed'}), 405)