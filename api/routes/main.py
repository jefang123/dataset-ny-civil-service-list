from flask import Blueprint, jsonify, abort
from requests import exceptions
import basic_client

main = Blueprint('main', __name__)

@main.route("/api", methods=["GET"])
def treasure_list():
  res, status_code = basic_client.get_all_datasets()
  if status_code == 200:
    return jsonify(res)
  elif status_code >= 400:
    abort(status_code)

@main.route('/api/<dataset>', methods=["GET"])

def get_dataset_info(dataset):
  res, status_code = basic_client.get_dataset_info(dataset)
  if status_code == 404:
    abort(404)
  return jsonify(res)

# @main.route('/api/<dataset>/<column>', methods=["GET"])
# def get_dataset_subset(dataset, column):
#   where = {column: "ASDF"}    
#   count = client.get(dataset, **where)
#   return jsonify({"total":count})