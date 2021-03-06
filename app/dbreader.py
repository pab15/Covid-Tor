import sqlite3
from datetime import datetime

class Article:
    def __init__(self, url, site, title, author, preview, date):
        self.url = url
        self.site = site
        self.title = title
        if author == "None":
            self.author = "Unknown"
        else:
            self.author = author
        self.preview = preview
        self.date = datetime.strptime(date, "%B %d, %Y %I:%M")

    def return_dict(self):
        result_dict = {
            "url" : self.url,
            "source" : self.site,
            "title" : self.title,
            "author" : self.author,
            "preview" : self.preview,
            "date" : self.date
        }

class ArticleList:
    def __init__(self):
        self.list = []

    def add_article(self, url, site, title, author, preview, date):
        self.list.append(Article(url, site, title, author, preview, date))

    def sort_articles(self):
        self.list.sort(key=lambda r: r.date)
        self.list.reverse()

class LocationCases:
    def __init__(self, location, date, casecount, deathcount):
        self.location = location
        self.date = datetime.strptime(date, "%B %d, %Y")
        self.casecount = casecount
        self.deathcount = deathcount

class CaseList:
    def __init__(self):
        self.list = []
    
    def add_location(self, location, date, casecount, deathcount):
        self.list.append(LocationCases(location, date, casecount, deathcount)) 

    def sort_cases(self):
        date_dict = {}
        key_array = []
        for x in self.list:
            str_date = x.date.strftime("%d %m, %Y")
            if str_date in date_dict:
                date_dict[str_date].append(x)
            else:
                date_dict[str_date] = [x]
        for key in date_dict:
            key_array.append(key)
            date_dict[key].sort(key=lambda x: x.casecount, reverse = True)
        key_array.sort(key=lambda date: date)
        key_array.reverse()
        new_list = []
        for key in key_array:
            for item in date_dict[key]:
                new_list.append(item)
        self.list = new_list

def create_article_list():
    conn = sqlite3.connect('data.db')
    curs = conn.cursor()
    a = ArticleList()
    curs.execute('''SELECT url, site, title, author, preview, date from news''')
    for article in curs:
        a.add_article(article[0], article[1], article[2], article[3], article[4], article[5])
    a.sort_articles()
    conn.commit()
    conn.close()
    return a.list

def create_country_list():
    conn = sqlite3.connect('data.db')
    curs = conn.cursor()
    c = CaseList()
    curs.execute('''SELECT country, date, casescount, deathcount from countrycounts''')
    for location in curs:
        c.add_location(location[0], location[1], location[2], location[3])
    c.sort_cases()
    conn.commit()
    conn.close()
    return c.list

def create_state_list():
    conn = sqlite3.connect('data.db')
    curs = conn.cursor()
    c = CaseList()
    curs.execute('''SELECT state, date, casescount, deathcount from statecounts''')
    for location in curs:
        c.add_location(location[0], location[1], location[2], location[3])
    c.sort_cases()
    conn.commit()
    conn.close()
    return c.list

create_country_list()