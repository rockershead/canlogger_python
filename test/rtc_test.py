import json
import os
import os.path
from os import path
import requests

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
  if("errors" in response.json() ):
   print("Cant send payload")
   buffer_file = open("/home/pi/buffer", "a+")
   buffer_file.write(payload+"\r\n")
   buffer_file.close()
 except requests.exceptions.RequestException as e:
  print("Cant send payload")
  buffer_file = open("/home/pi/buffer", "a+")
  buffer_file.write(payload+"\r\n")
  buffer_file.close()




json_data={"data":"test","timestamp":timestamp}

send_request(json.dumps(json_data))