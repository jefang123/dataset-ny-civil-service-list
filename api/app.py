import time
import requests
from flask import Flask, jsonify
from flask_cors import CORS
from errors.errors import errors
from routes.main import main

app = Flask(__name__)
cors = CORS(app)

app.register_blueprint(errors)
app.register_blueprint(main)

@app.route('/', methods=["GET"])
def hello():
  return("Server is running")

@app.route('/api/time', methods=["GET"])
def get_current_time():
    return jsonify({'time': time.time()})