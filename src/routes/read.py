from __init__ import CONECTION, CURSOR
from flask import request, jsonify, make_response

# def read():
#     if request.method == 'GET':
#         args = request.args
#         name = args.get('name')
#         if name:
#             CURSOR.execute(f"SELECT * FROM usuarios WHERE nombre LIKE '{name}%'")
#             user = CURSOR.fetchone()
#             if not user:
#                 return make_response(jsonify({}), 200)
#             dataDict = {
#                 Id: {
#                     'name': name,
#                     'edad': edad
#                 }
#                 for Id, name, edad in user  
#             }   
#             return make_response(jsonify(dataDict), 200)

#         CURSOR.execute('SELECT * FROM usuarios')
#         data = CURSOR.fetchall()
#         dataDict = {
#             Id: {
#                 'name': name,
#                 'edad': edad
#             }
#             for Id, name, edad in data    
#         }
#         return make_response(jsonify(dataDict), 200)
#     else:
#         return make_response(jsonify({'message': 'Method not allowed'}), 405)


def read():
    if request.method == 'GET':
        name = request.args.get('name', "")
        CURSOR.execute(f"SELECT * FROM usuarios WHERE nombre LIKE '{name}%'")
        data = CURSOR.fetchall()
        dataDict = {
            Id: {
                'name': name,
                'edad': edad
            }
            for Id, name, edad in data
        }
        return make_response(jsonify(dataDict), 200)
    
    return make_response(jsonify({'message': 'Method not allowed'}), 405)
