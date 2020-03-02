

from flask import Blueprint, jsonify
from requests import exceptions
import basic_client

client = basic_client.client()

main = Blueprint('main', __name__)

@main.route("/api")
def treasure_list():
    return "list of objects"

@main.route('/api/<dataset>', methods=["GET"])
def get_dataset_info(dataset):
  try:
    info = client.get_metadata(dataset)
  except exceptions.HTTPError:
    return ("Dataset doesn't exist, check dataset id")
  columns = info["columns"]
  response = {}
  for column in columns:
    response[column["name"]] = column["description"]
  count = client.get(dataset, select="COUNT(*) as total")
  try: 
    count = int(count[0]["total"])
  except KeyError:
    # dataset may not have api automation yet
    count = 0
  response["total"] = count
  return jsonify(response)


# @main.route('/api/<dataset>/<column>', methods=["GET"])
# def get_dataset_subset(dataset, column):
#   where = {column: "POOYAN"}    
#   count = client.get(dataset, **where)
#   return jsonify({"total":count})