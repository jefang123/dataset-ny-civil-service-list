import pandas as pd 
from sodapy import Socrata
from sql import SQLCreate

def soql_query(query_dict):
  query = SQLCreate()
  methods = {
    "select": query.select,
    "where": query.where,
    "group": query.group,
    "order": query.order,
  }
  for i, k in query_dict.items():
    methods[i] = k 
  return query.execute()

def data_query(dataset_host, dataset_str, full=False, **kwargs):
  client = Socrata(dataset_host, None)
  count = limit
  if full:
    metadata = client.get_metadata(dataset_str)
    count_res = client.get(dataset_str, select="COUNT(*) as total")
    try:
      count = int(count_res[0]["total"])
    except Exception:
      print("Error in total count query, setting limit to default")

  soql = soql_query(kwargs)
  results = client.get(dataset_str, select=soql, limit=count)
  results_df = pd.DataFrame.from_records(results)