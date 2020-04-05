import numpy
import sqlite3
from datetime import datetime
import matplotlib.pyplot as plt
from geopy.geocoders import Nominatim
from mpl_toolkits.basemap import Basemap

geolocator = Nominatim(user_agent="Mozilla/5.0")

map = Basemap(projection='mill', 
              lat_0=0, lon_0=0)

map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='coral',lake_color='aqua')
map.drawcoastlines()
conn = sqlite3.connect('data.db')
curs = conn.cursor()
date = datetime.now().strftime("%B %d, %Y")
curs.execute('''SELECT country, date, casescount, deathcount from countrycounts WHERE date=?''', (date,))
lons = []
lats = []
for location in curs:
  country = geolocator.geocode(location[0])
  print(country[0])
  lons.append(country.longitude)
  lats.append(country.latitude)

x, y = map(lons, lats)
map.scatter(x, y, marker='D',color='m')

plt.show()