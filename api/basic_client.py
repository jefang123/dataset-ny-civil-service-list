# import pandas as pd 
from sodapy import Socrata

def client():
  return Socrata("data.cityofnewyork.us", None)
  

# metadata = client.get_metadata("vx8i-nprf")

# count = client.get("vx8i-nprf", select="COUNT(*) as total")
# try 
#   count = int(count[0]["total"])
# except Exception 
#   print("Error in query, setting limit to default")
#   count = 25

# results = client.get("vx8i-nprf", limit = 10)
# full = client.get("vx8i-nprf", limit = count)
# results_df = pd.DataFrame.from_records(results)