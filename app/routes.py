import os
import sqlite3
import datetime
from app import app
from app.dbreader import *
from flask import render_template, request, url_for, flash

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/news')
def news():
    article_list = create_article_list()
    return render_template('news.html', article_list=article_list)

@app.route('/counts', methods=['POST', 'GET'])
def counts():
    data = {}
    case_data = create_country_list()
    case_data_us = create_state_list()
    if request.method == 'POST':
        conn = sqlite3.connect('data.db')
        curs = conn.cursor()
        if request.form.get('USA') == 'USA':
            location = request.form['location']
            date = datetime.now().strftime("%B %d, %Y")
            curs.execute('SELECT state FROM "statecounts" WHERE state=? AND date=?', (location, date))
            check_state = curs.fetchone()
            if check_state:
                data['country'] = location
                data['date'] = date
                curs.execute('SELECT casescount FROM "statecounts" WHERE state=? AND date=?', (location, date))
                cases = curs.fetchone()
                data['cases'] = str(cases[0])
                curs.execute('SELECT deathcount FROM "statecounts" WHERE state=? AND date=?', (location, date))
                deaths = curs.fetchone()
                data['deaths'] = str(deaths[0])
                return render_template('statecounts.html', data=data)
            else:
                flash('State not found in database!')
                return render_template('counts.html', case_data=case_data, case_data_us=case_data_us)
        else:
            location = request.form['location']
            date = datetime.now().strftime("%B %d, %Y")
            curs.execute('SELECT country FROM "countrycounts" WHERE country=? AND date=?', (location, date))
            check_country = curs.fetchone()
            if check_country:
                data['country'] = location
                data['date'] = date
                curs.execute('SELECT casescount FROM "countrycounts" WHERE country=? AND date=?', (location, date))
                cases = curs.fetchone()
                data['cases'] = str(cases[0])
                curs.execute('SELECT deathcount FROM "countrycounts" WHERE country=? AND date=?', (location, date))
                deaths = curs.fetchone()
                data['deaths'] = str(deaths[0])
                return render_template('countrycounts.html', data=data)
            else:
                flash('Country not found in database!')
                return render_template('counts.html', case_data=case_data, case_data_us=case_data_us)
        conn.close()
    else:
        return render_template('counts.html', case_data=case_data, case_data_us=case_data_us)

@app.route('/symptoms')
def symptoms():
    return render_template('symptom.html')

@app.route('/favicon.ico')
def faviconico():
    return ""
