import os
import sqlite3
import datetime
from app import app
from app.dbreader import *
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/news')
def news():
    article_list = create_article_list()
    return render_template('news.html', article_list=article_list)

@app.route('/counts')
def counts():
    return render_template('counts.html')

@app.route('/symptoms')
def symptoms():
    return render_template('symptom.html')
