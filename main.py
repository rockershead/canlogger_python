from data_aggre_management import combine_dict_json1
from data_aggre_technical import combine_dict_json2
import json
import os
import os.path
from os import path

import paho.mqtt.client as mqttClient
from dotenv import load_dotenv
import json
from datetime import datetime
import os
import socket
import shutil
import time




load_dotenv()




broker_address=os.getenv("broker_address")
port=int(os.getenv("port"))
topic=os.getenv("topic")
username=os.getenv("username")
access_token=os.getenv("access_token")




def on_publish(client,userdata,result):             #create function for callback
 print("data published \n")
 
def error_str(rc):
 return '{}: {}'.format(rc, mqtt.error_string(rc))
 
def on_connect(client, userdata, flags, rc):
 global rc1
 rc1=rc
 print('connected:rc=', error_str(rc))



mqttc = mqttClient.Client(clean_session=True)
mqttc.username_pw_set(username=username,password=access_token)
#mqttc.username_pw_set(access_token)
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish

 #try:
mqttc.connect(broker_address, port)
   #mqttc.loop_start()
 
 
mqttc.publish(topic,combine_dict_json1,qos=0)
 
print("management data published")

mqttc.publish(topic,combine_dict_json2,qos=0)

print("technical data published")
  						
 
 
#except:
 #print("connection lost.buffering......")

 
 


