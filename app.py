from flask import jsonify
from .setting.settings import create_app

app = create_app(__name__)

@app.route('/')
def hello_world():
    print(app.config['ENV'])
    return jsonify(data='Hello, World')
    
