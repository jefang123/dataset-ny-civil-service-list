from flask import Blueprint, jsonify, abort, request
from requests import exceptions
import basic_client

main = Blueprint('main', __name__)

@main.route("/api/", methods=["GET"])
# def get_datasets():
#   query_params = request.args
#   res, status_code = basic_client.get_all_datasets(query_params)
#   if status_code == 200:
#     return jsonify(res)
#   elif status_code >= 400:
#     abort(status_code)
def get_civil_dataset():
  res, status_code = basic_client.get_civil_dataset()
  if status_code == 200:
    return jsonify(res)
  elif status_code >= 400:
    abort(status_code)

@main.route('/api/<dataset>/', methods=["GET"])
def get_dataset(dataset):
  query_params = request.args
  res, status_code = basic_client.get_dataset(dataset, query_params)
  if status_code == 200:
    return jsonify(res)
  elif status_code >= 400:
    abort(status_code)

@main.route('/info/<dataset>/', methods=["GET"])
def get_dataset_info(dataset):
  # query_params = request.args
  res, status_code = basic_client.get_dataset_info(dataset)
  if status_code == 200:
    return jsonify(res)
  elif status_code >= 400:
    abort(status_code)

# @main.route('/api/<dataset>/<column>', methods=["GET"])
# def get_dataset_subset(dataset, column):
#   where = {column: "ASDF"}    
#   count = client.get(dataset, **where)
#   return jsonify({"total":count})