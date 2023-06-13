from __init__ import app
from src import ROOT

for route in ROOT:
    app.add_url_rule(route['path'], view_func=route['function'], methods=[route['method']])


