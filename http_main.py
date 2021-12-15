from data_aggre_management import combine_dict_json1,json_alarm
#from data_aggre_technical import combine_dict_json2
from cell_voltage import new_dict3
from module_temp import new_dict4
import json
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


timestamp=datetime.now().isoformat()

url=os.getenv("http_url")
headers = {'content-type': 'application/json','Authorization':'Bearer '+os.getenv("access_token")}

def send_request(payload):
 try:
  response = requests.post(url, data=payload, headers=headers)
  print(response.status_code)
  print(response.json())
 except requests.exceptions.RequestException as e:
  print(e)



 






 
send_request(combine_dict_json1)

 
print("management data published")
time.sleep(5)
#mqttc.publish(topic,combine_dict_json2,qos=0)

#print("technical data published")
new_dict4["timestamp"]=timestamp
print(json.dumps(new_dict4))
send_request(json.dumps(new_dict4))
print("module temp sent")
time.sleep(5)
new_dict3["timestamp"]=timestamp
##voltage info
print(json.dumps(new_dict3))
send_request(json.dumps(new_dict3))
print("voltage info sent")

time.sleep(5)
print(json_alarm)
send_request(json_alarm)
print("alarm info sent")
  						
 
 


 
 

