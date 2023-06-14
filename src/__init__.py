from src.routes.create import create
from src.routes.read import read
from src.routes.update import update
from src.routes.delete import delete
from src.routes.main import index

ROOT = [
    {
        'path': '/create',
        'method': 'POST',
        'function': create
    },
    {
        'path': '/read',
        'method': 'GET',
        'function': read
    },
    {
        'path': '/update',
        'method': 'PUT',
        'function': update
    },
    {
        'path': '/delete',
        'method': 'DELETE',
        'function': delete
    },
    {
        'path': '/',
        'method': 'GET',
        'function': index
    }
]