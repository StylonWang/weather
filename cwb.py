#!/usr/bin/python

import json
import urllib2
import xml.etree.ElementTree as ET
import time

while 1==1 :

    #query Taipei weather from cwb.gov.tw
    url2='http://opendata.cwb.gov.tw/opendataapi?dataid=F-C0032-001&authorizationkey=CWB-0748F0D7-6B87-4E15-9905-DF410EBAB4C7'
    r2 = urllib2.urlopen(url2)
    xml_str = urllib2.urlopen(url2).read()
    root = ET.fromstring(xml_str)
    print xml_str
    print root[8][0][1].text
    time.sleep(5)


