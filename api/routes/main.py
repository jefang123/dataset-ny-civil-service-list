from flask import Blueprint, jsonify
from requests import exceptions
import basic_client

main = Blueprint('main', __name__)

@main.route("/api")
def treasure_list():
    return "list of objects"

@main.route('/api/<dataset>', methods=["GET"])

def get_dataset_info(dataset):
  res, status_code = basic_client.get_dataset_info(dataset)
  if status_code == 404:
    abort(404)
  return jsonify(res)

# @main.route('/api/<dataset>/<column>', methods=["GET"])
# def get_dataset_subset(dataset, column):
#   where = {column: "POOYAN"}    
#   count = client.get(dataset, **where)
#   return jsonify({"total":count})