from . import app
from flask import jsonify, request
from app.models import property, user

@app.route('/')
def index():
    return 'Hello World!'

