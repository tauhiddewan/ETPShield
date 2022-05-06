from myproject import db
from datetime import datetime
class Data(db.Model):
  id = db.Column(db.Integer(), primary_key=True)
  temp = db.Column(db.String())
  time = db.Column(db.DateTime, default=datetime.now())
  
  def __init__(self, temp):
    self.temp = temp
    
  
    