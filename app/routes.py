import os
import sqlite3
from app.dbmodels import News
from app import app, db
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/counts')
def counts():
    return render_template('counts.html')
