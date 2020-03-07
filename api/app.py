import time
import requests
from flask import Flask, jsonify
from flask_cors import CORS
from errors.errors import errors
from routes.main import main

app = Flask(__name__)
cors = CORS(app) # ERRORS WILL RESULT IN CORS ERRORS! MAKE SURE TO TEST

# @app.after_request # blueprint can also be app~~
# def after_request(response):
#     header = response.headers
#     header['Access-Control-Allow-Origin'] = '*'
#     return response


app.register_blueprint(errors)
app.register_blueprint(main)

@app.route('/', methods=["GET"])
def hello():
  return("Server is running")

@app.route('/api/time', methods=["GET"])
def get_current_time():
    return jsonify({'time': time.time()})