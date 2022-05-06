from myproject import app, db
from myproject.models import Data
from flask import render_template, redirect, flash, url_for
import os
@app.route('/')
@app.route('/index')
def index():
  return render_template('index.htm')


@app.route('/etp/<sensordata>')
def etp (sensordata):
    now_temp = sensordata
    db.session.add(Data(now_temp))
    db.session.commit()
    return f'Success'
  
@app.route('/database')
def database():
  db = Data.query.all()
  return render_template('database.htm', db=db)
if __name__=='__main__':
  os.system('flask db migrate')
  os.system('flask db upgrade')
  app.run(debug=True)