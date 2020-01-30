import pandas as pd 
from sodapy import Socrata

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

  results = client.get(dataset_str, limit=count, **kwargs)
  results_df = pd.DataFrame.from_records(results)