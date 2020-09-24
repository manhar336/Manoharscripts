# /usr/bin/python
#purpose:script used to recover group servers automatically after 30 mins in MCT
#Date: 24-09-2020
import requests
import json

url = 'https://mctapi.webex.com/mpi/maintain/updateserver/0'
file = open('jsondata', 'rb')
data = file.read()
data = json.loads(data)    #loads used to load json into object
data = json.dumps(data)    #dumps load json into dictionary
header = {"content-type": "application/json"}
print data
file.close()
r = requests.post(url, data=c,headers=header)
print r.text
print r.status_code
if (r.status_code == 200):
    print ("MCT disabled and recover automatically after 30 mins")
else:
    print ("MCT disable failed ,Please check ")
