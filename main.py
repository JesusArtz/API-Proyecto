from __init__ import app
from src import ROOT

for route in ROOT:
    app.add_url_rule(route['path'], view_func=route['function'], methods=[route['method']])

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
