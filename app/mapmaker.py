import os
import numpy
import sqlite3
from datetime import datetime
import matplotlib.pyplot as plt
from geopy.geocoders import Nominatim
from mpl_toolkits.basemap import Basemap

def country_map():
  map = Basemap(projection='mill', 
                lat_0=0, lon_0=0)

  conn = sqlite3.connect('data.db')
  curs = conn.cursor()
  date = datetime.now().strftime("%B %d, %Y")
  curs.execute('''SELECT country, casescount, latitudes, longitudes from countrycounts WHERE date=?''', (date,))
  lons = []
  lats = []
  size = []
  for location in curs:
    if location[2] != None and location[3] != None and location[0] != "World":
      lons.append(location[3])
      lats.append(location[2])
      if location[1] > 100000:
        size.append(location[1] / 100)
      elif location[1] > 10000:
        size.append(location[1] / 100)
      elif location[1] > 1000:
        size.append(location[1] / 100)
      elif location[1] > 100:
        size.append(location[1] / 10)
      elif location[1] >= 10:
        size.append(location[1] / 2)
      elif location[1] < 10:
        size.append(location[1] / 1.5)
    else:
      print(location[0])
  conn.close()
  x, y = map(lons, lats)
  s = size
  print(len(s))
  print(len(x))
  print(len(y))
  map.scatter(x, y, s=s, marker='o',color='r', zorder=2)
  map.drawmapboundary(fill_color='aqua', zorder=0)
  map.fillcontinents(color='coral',lake_color='aqua', zorder=1)
  map.drawcoastlines()
  static_path = os.getcwd()
  print(static_path)
  plt.title("Corona Virus Cases World Wide")
  plt.savefig(static_path + r"\app\static\countrymap.png")


def state_map():
  map = Basemap(llcrnrlon=-119,llcrnrlat=22,urcrnrlon=-64,urcrnrlat=49,
        projection='lcc',lat_1=32,lat_2=45,lon_0=-95)

  conn = sqlite3.connect('data.db')
  curs = conn.cursor()
  date = datetime.now().strftime("%B %d, %Y")
  curs.execute('''SELECT state, casescount, latitudes, longitudes from statecounts WHERE date=?''', (date,))
  lons = []
  lats = []
  size = []
  for location in curs:
    if location[2] != None and location[3] != None and location[0] != "USA Total" and location[0] != "Wuhan Repatriated" and location[0] != "Diamond Princess Cruise":
      lons.append(location[3])
      lats.append(location[2])
      if location[1] > 100000:
        size.append(location[1] / 50)
      elif location[1] > 10000:
        size.append(location[1] / 50)
      elif location[1] > 1000:
        size.append(location[1] / 10)
      elif location[1] > 100:
        size.append(location[1] / 5)
      elif location[1] >= 10:
        size.append(location[1] / 2)
      elif location[1] < 10:
        size.append(location[1] / 1.5)
    else:
      print(location[0])
  conn.close()
  x, y = map(lons, lats)
  s = size
  print(len(s))
  print(len(x))
  print(len(y))
  map.scatter(x, y, s=s, marker='o',color='r', zorder=2)
  map.drawcoastlines()
  map.drawmapboundary(fill_color='aqua', zorder=0)
  map.fillcontinents(color='coral', lake_color='aqua', zorder=1)
  static_path = os.getcwd()
  print(static_path)
  plt.title("Corona Virus Cases In USA")
  plt.savefig(static_path + r"\app\static\statemap.png")

country_map()
state_map()