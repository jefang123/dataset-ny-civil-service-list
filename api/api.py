import time
from flask import Flask, jsonify
import basic_client

app = Flask(__name__)

client, dataset = basic_client.client()

@app.route('/')
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


@app.route('/api/time')
def get_current_time():
    return jsonify({'time': time.time()})