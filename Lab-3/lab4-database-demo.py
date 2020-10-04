#!/usr/bin/env python3
import sqlite3

#connect to database file
dbconnect = sqlite3.connect("mydatabase2.db");
#row_factory to sqlite3.ROw class
dbconnect.row_factory = sqlite3.Row;
#now we create a cursor to work with db
cursor = dbconnect.cursor();
#execute insetr statement
cursor.execute('''create table if not exists temps(sensorID integer,type text, zone text)''');

#If we want to access colimns by name we need to set
cursor.execute('''insert into temps values (1,"door","kitchen")''');

cursor.execute('''insert into temps values (2,"tempereature","kitchen")''')

cursor.execute('''insert into temps values (3,"door","garage")''')

cursor.execute('''insert into temps values (4,"motion","garage")''')

cursor.execute('''insert into temps values (5,"tempereature","garage")''')

dbconnect.commit();
#execute simple select statement
cursor.execute('SELECT * FROM temps');
#print data
print("Sensors in kitchen:")
print("sensorID \t type")
for row in cursor:
    if row['zone'] == "kitchen":
        print(str(row['sensorID']) + "\t\t" +row['type']);
print("\nDoor sensors are:")
cursor.execute('SELECT * FROM temps');
#print data
for row in cursor:
    if row['type'] == "door":
        print(row['sensorID'],row['type'],row['zone']);
#close the connection
dbconnect.close();
