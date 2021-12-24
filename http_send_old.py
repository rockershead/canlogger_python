import json
from logging import error
import os
import os.path
from os import path
import requests
import paho.mqtt.client as mqttClient
from dotenv import load_dotenv
import json
from datetime import datetime
import os
import socket
import shutil
import time
from datetime import datetime

load_dotenv()


delete_status=1
url=os.getenv("http_url")
headers = {'content-type': 'application/json','Authorization':'Bearer '+os.getenv("access_token")}

def send_request(payload):
 error_status=0
 try:
  response = requests.post(url, data=payload, headers=headers)
  print(response.status_code)
  print(response.json())
  if("errors" in response.json() ):
   error_status=1
 except requests.exceptions.RequestException as e:
  print(e)
  error_status=1
 
 return error_status




if(path.exists("/home/pi/buffer")):
 file1 = open("/home/pi/buffer", "r")
 lines = file1.readlines()
 for line in lines:
  error_status=send_request(line.strip())
  if(error_status==1):
   delete_status=0
   break
  time.sleep(3)
 if (delete_status==1):
  print("all old data published")
  os.remove("/home/pi/buffer")
 
  
 
 
 
  						
 
 
