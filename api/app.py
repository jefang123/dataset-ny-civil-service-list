import time
import requests
from flask import Flask, jsonify
from errors.errors import errors
from routes.main import extension

app = Flask(__name__)

app.register_blueprint(errors)
app.register_blueprint(extension)

@app.route('/', methods=["GET"])
def hello():
  return("Server is running")

@app.route('/api/time', methods=["GET"])
def get_current_time():
    return jsonify({'time': time.time()})