from datetime import datetime
from os import environ
from sodapy import Socrata
from requests import exceptions

_client = None
DOMAINS = {
  "data.cityofnewyork.us":"ny", #Add more domains in the future
}
_current_dataset = None
"""
Column Data:
  FieldName : FieldDataType

Possible Data Types: text, number, calender_date
"""
_COLUMNS_TYPE = {}
_COUNT = 0

def setup_client():
  global _client
  if not _client:
    appToken = environ.get("SOCRATA_APPTOKEN", None)
    _client = Socrata("data.cityofnewyork.us", appToken)

def handleHTTPError(e):
  if e.response.status_code == 404:
    return ("Dataset doesn't exist, check dataset id", 404)
  elif e.response.status_code == 500:
    return ("Client is throttled, try query later", 500)
  else:
    return ("Unable to query database, try again later.", 500)

def setup_dataset(dataset):
  global _current_dataset, _COLUMNS_TYPE, _COUNT
  if not _current_dataset or _current_dataset != dataset:
    _current_dataset = dataset
    _COUNT = 0
    try:
      info = _client.get_metadata(dataset)
    except exceptions.HTTPError as e:
      return handleHTTPError(e)
    columns = info["columns"]
    for column in columns:
      _COLUMNS_TYPE[column["fieldName"]] = column["dataTypeName"]
  
  if not _COUNT:
    try:
      count = _client.get(dataset, select="COUNT(*) as total")
    except exceptions.HTTPError as e:
      return handleHTTPError(e)
    try: 
      _COUNT = int(count[0]["total"])
    except KeyError:
      # dataset may not have api automation yet
      _COUNT = -1
  return ("Setup dataset successfully", 200)

def setup(dataset=None):
  setup_client()
  if dataset:
    return setup_dataset(dataset)

def get_all_datasets(query_params):
  l = query_params.get("limit", 25)
  q = query_params.get("q", "")
  o = query_params.get("offset", 0)
  setup()
  data = {}
  domain = DOMAINS.get(_client.domain)
  datasets = _client.datasets(limit=l, q=q, offset=o)
  for dataset in datasets:
    dataset_id = dataset["resource"]["id"] 
    dataset_name = dataset["resource"]["name"]
    data[dataset_id] = dataset_name
    data["domain"] = domain
  return data, 200

def get_dataset(dataset, query_params):
  sort_asc = query_params.get("sort_asc")
  sort_dsc = query_params.get("sort_desc")
  sort = ""

  if sort_asc:
    sort += ",".join(sort_asc) + " ASC"
  if sort_dsc:
    sort += ",".join(sort_dsc) + " DSC"


  msg, status_code = setup(dataset)
  if status_code != 200:
    return (msg, status_code)
  try:
    results = _client.get(dataset, limit=25, sort=sort)
  except exceptions.HTTPError as e:
    return handleHTTPError(e)
  response = {}
  for i, result in enumerate(results):
    for field, value in result.items():
      if _COLUMNS_TYPE[field] == "number":
        result[field] = int(float(value))
      elif _COLUMNS_TYPE[field] == "calendar_date":
        result[field] = datetime.fromisoformat(value).strftime("%m/%d/%y")
    response[i] = result
  # response["total"] = _COUNT
  return response, 200

def get_dataset_info(dataset):
  msg, status_code = setup(dataset)
  if status_code != 200:
    return (msg, status_code)
  try:
    info = _client.get_metadata(dataset)
  except exceptions.HTTPError as e:
    return(handleHTTPError)
  columns = info["columns"]
  response = {}
  response["dataset_name"] = info["name"]
  cols_metadata = {}
  for column in columns:
    meta = {}
    meta["name"] = column.get("name", "")
    meta["description"] = column.get("description", "")
    cols_metadata[column["id"]] = meta
  response["columns"] = cols_metadata
  count = _client.get(dataset, select="COUNT(*) as total")
  response["total"] = _COUNT
  return response, 200