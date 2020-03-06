from sodapy import Socrata
from requests import exceptions

_client = None

DOMAINS = {
  "data.cityofnewyork.us":"ny",
}

def setup_client():
  global _client
  if not _client:
    _client = Socrata("data.cityofnewyork.us", None)

def setup_with_appToken(appToken):
  global _client
  _client = Socrata("data.cityofnewyork.us", appToken)

def get_all_datasets(q="", limit=25, offset=0):
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

def get_dataset_info(dataset):
  setup_client()
  try:
    info = _client.get_metadata(dataset)
  except exceptions.HTTPError as e:
    if e.response.status_code == 404:
      return ("Dataset doesn't exist, check dataset id", 404)
    elif e.response.status_code == 500:
      return ("Client is throttled, try query later", 500)
    else:
      return ("Unable to query database, try again later.", 500)
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
  try: 
    count = int(count[0]["total"])
  except KeyError:
    # dataset may not have api automation yet
    count = 0
  response["total"] = count
  return response, 200