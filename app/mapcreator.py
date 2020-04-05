import numpy
import sqlite3
from datetime import datetime
import matplotlib.pyplot as plt
from geopy.geocoders import Nominatim
from mpl_toolkits.basemap import Basemap

# fig = plt.figure(figsize=(18,18))
# m=Basemap(projection='cea')
# m.drawcoastlines()
# m.fillcontinents()
# m.drawmapboundary()

# geolocator = Nominatim(user_agent="Mozilla/5.0")

# map = Basemap(projection = 'mill', llcrnrlat = -90, llcrnrlon = -180, urcrnrlat = 90, urcrnrlon = 180, resolution = 'c')

# map.drawcoastlines()
# map.drawcountries(linewidth = 1)
# map.fillcontinents(color = "coral", lake_color = "aqua")
# map.drawparallels(numpy.arange(-90.,120.,30.))
# map.drawmeridians(numpy.arange(0.,420.,60.))
# map.drawmapboundary(fill_color='aqua')

import numpy as np
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from datetime import datetime
# miller projection
# map = Basemap(projection='mill',lon_0=180)
# plot coastlines, draw label meridians and parallels.
# map.drawcoastlines()
# map.drawparallels(np.arange(-90,90,30),labels=[1,0,0,0])
# map.drawmeridians(np.arange(map.lonmin,map.lonmax+30,60),labels=[0,0,0,1])
# fill continents 'coral' (with zorder=0), color wet areas 'aqua'
# map.drawmapboundary(fill_color='aqua')
# map.fillcontinents(color='coral',lake_color='aqua')
# shade the night areas, with alpha transparency so the
# map shows through. Use current time in UTC.
# date = datetime.utcnow()
# map.plot(10, 10, 'ro', markersize=15)
# plt.title('Day/Night Map for %s (UTC)' % date.strftime("%d %b %Y %H:%M:%S"))
# plt.savefig('new_map')
# conn = sqlite3.connect('data.db')
# curs = conn.cursor()
# date = datetime.now().strftime("%B %d, %Y")
# curs.execute('''SELECT country, date, casescount, deathcount from countrycounts WHERE date=?''', (date,))
# for location in curs:
#   country = geolocator.geocode(location[0])
#   print(country[0])
#   map.plot(country.latitude, country.longitude, 'ro', markersize=5)
# country = geolocator.geocode("UAE")
# xpt, ypt = country.latitude, country.longitude

# conn.close()
fig, ax = plt.subplots(figsize=(15,15))


m1 = Basemap(projection='merc',
             llcrnrlat=8.3,
             urcrnrlat=53.9,
             llcrnrlon=94.0,
             urcrnrlon=147.6,
             lat_ts=0,
             resolution='c')

m1.fillcontinents(color='#191919',lake_color='#000000') # dark grey land, black lakes
m1.drawmapboundary(fill_color='#000000')                # black background
m1.drawcountries(linewidth=0.1, color="w")              # thin white line for country borders
m1.drawstates(linewidth=0.1, color="w")


# Plot the data
mxy = m1([30, 20, -30, 90], [30, 20, -30, 90])
m1.scatter(mxy[0], mxy[1], s=300,c=20, lw=0, alpha=1, zorder=5,cmap='Reds')
ax.annotate("blablabla", (121.597366,25.105497),color='green')

#colorbar
plt.colorbar(label=r'24H Trading-Volume in MillionK$')
plt.clim(1, 21)
plt.title("Cryptocurrency capital movement - Asia")
