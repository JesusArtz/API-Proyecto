from __init__ import CONECTION, CURSOR
from flask import request, jsonify, make_response

def delete():
    if request.method == 'DELETE':
        data = request.get_json()
        if not data['id']:
            return make_response(jsonify({'message': 'Id is required'}), 400)
        CURSOR.execute('DELETE FROM usuarios WHERE id = ?', (data['id'],))
        CONECTION.commit()
        return make_response(jsonify({'message': 'User deleted'}), 200)
    else:
        return make_response(jsonify({'message': 'Method not allowed'}), 405)