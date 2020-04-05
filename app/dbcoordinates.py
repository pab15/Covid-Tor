import sqlite3
from geopy.geocoders import Nominatim

def build_country_coordinates():
    geolocator = Nominatim(user_agent="Mozilla/5.0")
    conn = sqlite3.connect('data.db')
    curs = conn.cursor()
    data = curs.execute('''SELECT * FROM countrycounts''')
    data = data.fetchall()
    for location in data:
        print(location)
        if location[1] != "World":
            country = geolocator.geocode(location[1])
            sql_update_query = """UPDATE countrycounts SET latitudes={} WHERE country='{}'""".format(country.latitude, location[1])
            print(sql_update_query)
            curs.execute(sql_update_query)
            sql_update_query = """UPDATE countrycounts SET longitudes={} WHERE country='{}'""".format(country.longitude, location[1])
            curs.execute(sql_update_query)
            conn.commit()
    #   lons.append(country.longitude)
    #   lats.append(country.latitude)
    conn.close()

def build_state_coordinates():
    geolocator = Nominatim(user_agent="Mozilla/5.0")
    conn = sqlite3.connect('data.db')
    curs = conn.cursor()
    data = curs.execute('''SELECT * FROM statecounts''')
    data = data.fetchall()
    for location in data:
        print(location)
        if location[1] != "USA Total" and location[1] != "Wuhan Repatriated" and location[1] != "Diamond Princess Cruise":
            state = geolocator.geocode(location[1])
            sql_update_query = """UPDATE statecounts SET latitudes={} WHERE state='{}'""".format(state.latitude, location[1])
            print(sql_update_query)
            curs.execute(sql_update_query)
            sql_update_query = """UPDATE statecounts SET longitudes={} WHERE state='{}'""".format(state.longitude, location[1])
            curs.execute(sql_update_query)
            conn.commit()
    #   lons.append(country.longitude)
    #   lats.append(country.latitude)
    conn.close()

if __name__ == "__main__":
    build_state_coordinates()