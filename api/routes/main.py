

from flask import Blueprint, jsonify
from requests import exceptions
import basic_client

client = basic_client.client()

extension = Blueprint('extension', __name__)

@extension.route("/api")
def treasure_list():
    return "list of objects"

@extension.route('/api/<dataset>', methods=["GET"])
def get_dataset(dataset):
  try:
    count = client.get(dataset, select="COUNT(*) as total")
  except exceptions.HTTPError:
    return ("Dataset doesn't exist, check dataset id")
  try: 
    count = int(count[0]["total"])
  except Exception:
    count = 25
  ## error handling for nonexistent dataset?
  return jsonify({"total":count})