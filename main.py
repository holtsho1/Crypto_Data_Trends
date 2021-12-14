from HTMLParser import *
import time
from datetime import datetime
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from datetime import date
import requests
import lxml.html
import os
from CMCAPI_Data_Pull import *
request=HTMLParser1()
old_data=CMCAPI_DataExtract()
new_data=old_data
print("running")
time.sleep(1)

while True:


        # create a new parse
        # request = HTMLParser1()
        # print(request)
        # wait for 10 seconds
        time.sleep(10)

        # create a new parse
        newRequest = HTMLParser1()
        print(newRequest)
        #check if new hash is same as the previous hash
        if not request==newRequest:
                print("New coin added")  #notify
                #write CMC api pull trigger
                new_data=CMCAPI_DataExtract()
                CMCAPI_DataManipulate(new_data,old_data)
        # wait for 10 seconds
        old_data=new_data
        request=newRequest
        time.sleep(10)
        continue
