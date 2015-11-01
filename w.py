#!/usr/bin/python

import json
import urllib2
import xml.etree.ElementTree as ET
import time

while 1==1 :
    # query Taipei weather from openweather
    url='http://api.openweathermap.org/data/2.5/weather?id=1668341&appid=0c793813238d1dcb4c829d4eac4bfeb3'
    r = urllib2.urlopen(url)
    data = json.load(r)
    print "OpenWeather"
    print data["main"]["temp"]
    print data["main"]["temp_min"]
    print data["main"]["temp_max"]

    time.sleep(5)


# query Taipei weather from cwb.gov.tw
#url2='http://opendata.cwb.gov.tw/opendataapi?dataid=F-C0032-001&authorizationkey=CWB-0748F0D7-6B87-4E15-9905-DF410EBAB4C7'
#r2 = urllib2.urlopen(url)
#xml_str = urllib2.urlopen(url2).read()
#root = ET.fromstring(xml_str)
#print root["location"]
