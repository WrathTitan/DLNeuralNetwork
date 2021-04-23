from flask import Flask, render_template, redirect
import requests
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)
app.config['SQLITE_DATABASE_CONFIG']='sqlite3:///test.db'
db=SQLAlchemy(app)
db.create_all()

@app.route('/')
def home():
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)