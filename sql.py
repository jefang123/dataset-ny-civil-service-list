"""
  Socrata client has a select argument for its get method
  A Valid SQL query can be given as a select argument 

  Example query parameters for vx8i-nprf:

  WHERE exam_no = 'XXXX'
  ORDER BY lastname, firstname ASC/DESC
  ORDER BY Adj.FA ASC/DESC
  ORDER BY exam_no ASC/DESC
  ORDER BY list_no

  FROM is not used explicitly 

"""

class SQLCreate:
  def __init__(self):
    self.s = "*"
    self.w = ""
    self.g = ""
    self.o = ""

  def select(self, select_sql):
    self.s = f"{select_sql} "

  def where(self, where_sql):
    self.w = f"WHERE {where_sql} "
    
  def group(self, group_sql):
    self.g = f"GROUP BY {group_sql} "
  
  def order(self, order_sql):
    self.o = f"ORDER BY {order_sql} "
  
  # def limit(self, limit_sql):
  #   self.l = f"LIMIT {limit_sql} "

  def execute(self):
    return(f"{self.s}{self.w}{self.g}{self.o}")

  
