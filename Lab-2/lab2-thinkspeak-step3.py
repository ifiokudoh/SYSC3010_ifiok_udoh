import httplib
import urllib
import time
import requests
import json
key = "OEGCYO9F8FJCZGO6"  # Put your API Key here
def thermometer():
    #Calculate CPU temperature of Raspberry Pi in Degrees C
    temp = int(open('/sys/class/thermal/thermal_zone0/temp').read()) / 1e3 # Get Raspberry Pi CPU temp
    params = urllib.urlencode({'field1': temp, 'key':key }) 
    headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
    conn = httplib.HTTPConnection("api.thingspeak.com:80")
    try:
        conn.request("POST", "/update", params, headers)
        response = conn.getresponse()
        print temp
        print response.status, response.reason
        data = response.read()
        conn.close()
    except:
        print "connection failed"
    
def read_data_thingspeak():
    NEW_URL='https://api.thingspeak.com/channels/1161330/feeds.json?api_key=5H3MLOB7Q9F0RZGH&results=2'

    get_data=requests.get(NEW_URL).json()
    print(get_data)
    channel_id=get_data['channel']['id']

    feild_1=get_data['feeds']
    #print(feild_1)

    t=[]
    for x in feild_1:
        #print(x['field1'])
        t.append(x['field1'])

if __name__ == '__main__':
    # while True:
        # thermometer()
    read_data_thingspeak()

       