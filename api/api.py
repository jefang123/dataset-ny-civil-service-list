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
# def count():
#   count = client.get("vx8i-nprf", select="COUNT(*) as total")
#   try:
#     count = int(count[0]["total"])
#   except Exception:
#     print("Error in query, setting limit to default")
#     count = 25
#   return { 'total': count }

@app.route('/api/time', methods=["GET"])
def get_current_time():
    return jsonify({'time': time.time()})