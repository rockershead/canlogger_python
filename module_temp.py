import can
from can.bus import BusState
import time
import cantools


# bus = can.interface.Bus(bustype='ixxat', channel=0, bitrate=250000)
 # bus = can.interface.Bus(bustype='vector', app_name='CANalyzer', channel=0, bitrate=250000)
 # set to read-only, only supported on some interfaces
 #bus.state = BusState.PASSIVE
count=0
new_dict4={}

with can.interface.Bus(bustype="socketcan", channel="can0", bitrate=250000) as bus:
 db = cantools.database.load_file('/home/pi/durapower_jp.dbc') #path of .dbc file
 ##for all bmu
 msg1=can.Message(arbitration_id=0x00004200, data=[0x03],is_remote_frame=False, is_extended_id=True, dlc=8)
 bus.send(msg1)

 for msg in bus:
  count=count+1
  print(msg)
  json_data=db.decode_message(msg.arbitration_id, msg.data)
  for key in json_data.keys():
   new_dict4[key]=json_data[key]
   
  time.sleep(1)
  print(count)
  if(count==10):
    count=0
    break
  
 

 msg2=can.Message(arbitration_id=0x00004201, data=[0x03],is_remote_frame=False, is_extended_id=True, dlc=8)
 bus.send(msg2)

 for msg in bus:
  count=count+1
  print(msg)
  json_data=db.decode_message(msg.arbitration_id, msg.data)
  for key in json_data.keys():
   new_dict4[key]=json_data[key]
   
  time.sleep(1)
  print(count)
  if(count==10):
    count=0
    break

 msg3=can.Message(arbitration_id=0x00004202, data=[0x03],is_remote_frame=False, is_extended_id=True, dlc=8)
 bus.send(msg3)

 for msg in bus:
  count=count+1
  print(msg)
  json_data=db.decode_message(msg.arbitration_id, msg.data)
  for key in json_data.keys():
   new_dict4[key]=json_data[key]
   
  time.sleep(1)
  print(count)
  if(count==10):
    count=0
    break

 msg4=can.Message(arbitration_id=0x00004203, data=[0x03],is_remote_frame=False, is_extended_id=True, dlc=8)
 bus.send(msg4)

 for msg in bus:
  count=count+1
  print(msg)
  json_data=db.decode_message(msg.arbitration_id, msg.data)
  for key in json_data.keys():
   new_dict4[key]=json_data[key]
   
  time.sleep(1)
  print(count)
  if(count==10):
    count=0
    break