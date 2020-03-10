import time
import requests
from flask import Flask, jsonify, request
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
  d= {}
  d["base_url"] = request.base_url
  d["chrset"] = request.charset
  d["cookies"] = request.cookies
  # d["data"] = request.data
  # d["headers"] = request.headers
  d["User-Agent"] = request.headers.get('User-Agent')
  d["host"] = request.host
  d["host_url"] = request.host_url
  # d["is_multithread"] = request.is_multithread
  # d["is_run_once"] = request.is_run_once
  d["method"] = request.method
  d["remote_addr"] = request.remote_addr
  d["remote_user"] = request.remote_user
  # d["query_string"] = request.query_string

  return(jsonify(d))

@app.route('/api/time', methods=["GET"])
def get_current_time():
    return jsonify({'time': time.time()})