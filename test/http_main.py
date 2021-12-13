import json
import os
import os.path
from os import path
import requests
import can
from can.bus import BusState
import time
import cantools
# bus = can.interface.Bus(bustype='ixxat', channel=0, bitrate=250000)
 # bus = can.interface.Bus(bustype='vector', app_name='CANalyzer', channel=0, bitrate=250000)
 # set to read-only, only supported on some interfaces
 #bus.state = BusState.PASSIVE
import paho.mqtt.client as mqttClient
from dotenv import load_dotenv
import json
from datetime import datetime
import os
import socket
import shutil
import time
import json
from datetime import datetime


load_dotenv()




broker_address=os.getenv("broker_address")
#port=int(os.getenv("port"))
#topic=os.getenv("topic")
#username=os.getenv("username")
#access_token=os.getenv("access_token")


def send_request(payload):
 try:
  response = requests.api.post(url, data=payload, headers=headers)
  print(response.status_code)
  print(response.json())
 except requests.exceptions.RequestException as e:
  print(e)





with can.interface.Bus(bustype="socketcan", channel="can0", bitrate=250000) as bus:
 db = cantools.database.load_file('/home/pi/test.dbc') #path of .dbc file
 #message = bus.recv()
 for msg in bus:
  new_dict={}
  try:
   
   print(msg)
   timestamp=msg.timestamp
   json_data=db.decode_message(msg.arbitration_id, msg.data)
   
   json_data["timestamp"]=datetime.fromtimestamp(timestamp).isoformat()
   print (json_data)
   send_request(json.dumps(json_data))
  						
 
 

   time.sleep(3)
  except:
   pass
   time.sleep(3) 
 



 
