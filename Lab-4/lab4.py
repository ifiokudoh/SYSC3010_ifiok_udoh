#Lab 4 programming task to write data to thinkspeak channel
#Author Ifiok Udoh 101052143
#
import httplib
import urllib

key = "AT68QYQ94MQEWXL3"  # L4 key


'''
This function writes the required data to the appropraite fields for Lab4
'''
def writeThinkSpeak():
    params = urllib.urlencode({'field1': 'L3-T-3', 'field2': 'ifiokudoh@cmail.carleton.ca', 'field3': 'd', 'key':key }) 
    headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
    conn = httplib.HTTPConnection("api.thingspeak.com:80")
    try:
        conn.request("POST", "/update", params, headers)
        response = conn.getresponse()
        print response.status, response.reason
        data = response.read()
        conn.close()
    except:
        print "connection failed"
    
def main():
    writeThinkSpeak()

if __name__ == '__main__':
   main()
