import re
import ssl
import urllib
import sqlite3
from datetime import datetime
from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error

class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

def grab_ny_news():
    conn = sqlite3.connect('data.db')
    curs = conn.cursor()
    result = []
    url = 'https://www.nytimes.com/news-event/coronavirus'
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    data = soup.find_all('li', attrs={"class" : "css-ye6x8s"})
    for item in data:
        source = 'NY Times'
        title_data = item.find_all('h2')
        link_data = item.find_all('a', href=True)
        author_block = item.find_all('span', attrs={"class" : "css-1n7hynb"})
        preview_block = item.find_all('p', attrs={"class" : "css-1echdzn e1xfvim31"})
        title = title_data[0].string
        url = "http://www.nytimes.com" + link_data[0]['href']
        try:
            author = author_block[0].string
        except:
            author = 'Unknown'
        preview = preview_block[0].string
        date = datetime.now().strftime("%B %d, %Y %I:%M")
        # date = datetime.strptime(date, "%B %d, %Y %I:%M")
        curs.execute('SELECT url FROM "news" WHERE url=?', (url,))
        check_url = curs.fetchone()
        if check_url:
            pass
        else:
            curs.execute("INSERT INTO news(url, site, title, author, preview, date) VALUES('{}', '{}', '{}','{}','{}', '{}')".format(url, source, title, author, preview, date))
    conn.commit()
    conn.close()

def grab_counts():
    conn = sqlite3.connect('data.db')
    curs = conn.cursor()
    result = []
    url = 'https://www.worldometers.info/coronavirus/'
    opener = AppURLopener()
    response = opener.open(url)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    data = soup.find_all('tr')
    count = 0
    end = False
    for dt in data:
        if end == True:
            break
        else:
            dta = dt.find_all('td')
            col_count = 0
            done = False
            for d in dta:
                if d.string == 'Total:':
                    end = False
                    break
                else:
                    if col_count == 0:
                        location = d.string
                        print(location)
                    if col_count == 1:
                        if d.string == "None" or d.string == "" or d.string == " ":
                            total_cases = 0
                        else:
                            total_cases = int(d.string.replace(",", ""))
                            print(total_cases)
                    if col_count == 3:
                        if d.string == None or d.string == "" or d.string == " ":
                            total_deaths = 0
                        else:
                            total_deaths = int(d.string.replace(",", ""))
                        print(total_deaths)
                        done = True
                    if done == True:
                        date = datetime.now().strftime("%B %d, %Y")
                        curs.execute('SELECT country, date FROM "countrycounts" WHERE country=? AND date=?', (location, date))
                        check_country = curs.fetchone()
                        if check_country:
                            pass
                        else:
                            curs.execute("INSERT INTO countrycounts(country, casescount, deathcount, date) VALUES('{}', '{}', '{}','{}')".format(location, total_cases, total_deaths, date))
                        done = False    
                    col_count += 1
    conn.commit()
    conn.close()

def grab_state_counts():
    conn = sqlite3.connect('data.db')
    curs = conn.cursor()
    result = []
    url = 'https://www.worldometers.info/coronavirus/country/us/'
    opener = AppURLopener()
    response = opener.open(url)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    data = soup.find_all('tr')
    count = 0
    end = False
    for dt in data:
        if end == True:
            break
        else:
            dta = dt.find_all('td')
            col_count = 0
            done = False
            for d in dta:
                if d.string == 'Total:':
                    end = True
                    break
                else:
                    if col_count == 0:
                        location = d.string.rstrip(" ").lstrip(" ").replace("\n", "")
                        print(location)
                    if col_count == 1:
                        if d.string == None or d.string == "" or d.string == " " or d.string == "\n":
                            total_cases = 0
                        else:
                            total_cases = int(d.string.replace(",", ""))
                            print(total_cases)
                    if col_count == 3:
                        if d.string == None or d.string == "" or d.string == " " or d.string == "\n" or d.string == "\xa0":
                            total_deaths = 0
                        else:
                            total_deaths = int(d.string.replace(",", ""))
                        print(total_deaths)
                        done = True
                    if done == True:
                        date = datetime.now().strftime("%B %d, %Y")
                        curs.execute('SELECT state, date FROM "statecounts" WHERE state=? AND date=?', (location, date))
                        check_state = curs.fetchone()
                        if check_state:
                            pass
                        else:
                            curs.execute("INSERT INTO statecounts(state, casescount, deathcount, date) VALUES('{}', '{}', '{}','{}')".format(location, total_cases, total_deaths, date))
                        done = False    
                    col_count += 1
    conn.commit()
    conn.close()        

def build_db():
    conn = sqlite3.connect('data.db')
    curs = conn.cursor()
    curs.execute('''CREATE TABLE IF NOT EXISTS news
                    (id INTEGER PRIMARY KEY, url STRING, site STRING, title STRING, author STRING, preview STRING, date STRING)''')
    curs.execute('''CREATE TABLE IF NOT EXISTS countrycounts
                    (id INTEGER PRIMARY KEY, country STRING, casescount INTEGER, deathcount INTEGER, date STRING)''')
    curs.execute('''CREATE TABLE IF NOT EXISTS statecounts
                    (id INTEGER PRIMARY KEY, state STRING, casescount INTEGER, deathcount INTEGER, date STRING)''')
    conn.commit()
    conn.close()

def refresh_db():
    grab_ny_news()
    print('fetching articles...')
    #watch --interval=3600 command
    grab_counts()
    print('grabbing counts...')
    grab_state_counts()
    print('grabbing counts...')


if __name__ == '__main__':
    build_db()
    refresh_db()
    