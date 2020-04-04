import re
import ssl
import urllib
import sqlite3
from datetime import datetime
from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error

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

            
        

def build_db():
    conn = sqlite3.connect('data.db')
    curs = conn.cursor()
    curs.execute('''CREATE TABLE IF NOT EXISTS news
                    (id INTEGER PRIMARY KEY, url STRING, site STRING, title STRING, author STRING, preview STRING, date STRING)''')
    curs.execute('''CREATE TABLE IF NOT EXISTS countrycounts
                    (id INTEGER PRIMARY KEY, country STRING, casescount INTEGER, deathcount INTEGER, date STRING)''')
    conn.commit()
    conn.close()

def refresh_db():
    grab_ny_news()
    print('fetching articles...')
    #watch --interval=3600 command

if __name__ == '__main__':
    grab_ny_news()
    build_db()