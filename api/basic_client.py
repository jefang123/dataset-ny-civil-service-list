from sodapy import Socrata
from requests import exceptions

_client = None
DOMAINS = {
  "data.cityofnewyork.us":"ny",
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
    _client = Socrata("data.cityofnewyork.us", None)

def setup_with_appToken(appToken):
  global _client
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

def get_all_datasets(query_params):
  l = query_params.get("limit", 25)
  q = query_params.get("q", "")
  offset = query_params.get("offset", 0)
  setup_client()
  data = {}
  domain = DOMAINS.get(_client.domain)
  datasets = _client.datasets(limit=limit, q=q, offset=offset)
  for dataset in datasets:
    dataset_id = dataset["resource"]["id"] 
    dataset_name = dataset["resource"]["name"]
    data[dataset_id] = dataset_name
    data["domain"] = domain
  return data, 200

def get_dataset(dataset):
  setup_client()
  msg, status_code = setup_dataset(dataset)
  if status_code != 200:
    return (msg, status_code)
  try:
    results = _client.get(dataset)
  except exceptions.HTTPError as e:
    return handleHTTPError(e)
  response = {}
  for i, result in enumerate(results):
    for field, value in result.items():
      if _COLUMNS_TYPE[field] == "number":
        value = int(value)
      elif _COLUMNS_TYPE[field] == "calender_date":
        pass
    response[i] = result
  if _COUNT > 0:
    response["total"] = _COUNT
  return response, 200

def get_dataset_info(dataset):
  setup_client()
  msg, status_code = setup_dataset(dataset)
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
    meta["name"] = column["name"]
    meta["description"] = column["description"]
    cols_metadata[column["id"]] = meta
  response["columns"] = cols_metadata
  count = _client.get(dataset, select="COUNT(*) as total")
  if _COUNT > 0:
    response["total"] = _COUNT
  return response, 200