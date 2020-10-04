#!/usr/bin/env python3
import sqlite3
from urllib.request import * 
from urllib.parse import * 
import json

# The URL that is formatted: http://api.openweathermap.org/data/2.5/weather?APPID=a808bbf30202728efca23e099a4eecc7&units=imperial&q=ottawa


# As of October 2015, you need an API key.
# I have registered under my Carleton email.
apiKey = "a808bbf30202728efca23e099a4eecc7"

# Query the user for a city
city = input("Enter the name of a city whose weather you want: ")

# Build the URL parameters
params = {"q":city, "units":"imperial", "APPID":apiKey }
arguments = urlencode(params)

# Get the weather information
address = "http://api.openweathermap.org/data/2.5/weather"
url = address + "?" + arguments

print (url)
webData = urlopen(url)
results = webData.read().decode('utf-8')
  # results is a JSON string
webData.close()

print (results)
#Convert the json result to a dictionary
# See http://openweathermap.org/current#current_JSON for the API

data = json.loads(results)

# Print the results

# current = data["main"]
# print("main:", current)
# degreeSym = chr(176)

# print ("Temperature: %d%sF" % (current["temp"], degreeSym ))
# print ("Humidity: %d%%" % current["humidity"])
# print ("Pressure: %d" % current["pressure"] )

# current = data["wind"]
# print ("Wind : %d" % current["speed"])

#connect to database file
dbconnect = sqlite3.connect("mydatabase2.db");
#row_factory to sqlite3.ROw class
dbconnect.row_factory = sqlite3.Row;
#now we create a cursor to work with db
cursor = dbconnect.cursor();
#execute insetr statement
cursor.execute('''create table if not exists windspeed(city text,windspeed Integer)''');

#If we want to access colimns by name we need to set
cursor.execute('''insert into windspeed values (?,?)''',(city, data["wind"]["speed"]));

dbconnect.commit();
#execute simple select statement
cursor.execute('SELECT * FROM windspeed');
#print data
print("city \t windspeed")
for row in cursor:
  print((row['city']) + "\t" +str(row['windspeed']));
#close the connection
dbconnect.close();


