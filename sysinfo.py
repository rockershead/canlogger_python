import can
from can.bus import BusState
import time
import cantools


# bus = can.interface.Bus(bustype='ixxat', channel=0, bitrate=250000)
 # bus = can.interface.Bus(bustype='vector', app_name='CANalyzer', channel=0, bitrate=250000)
 # set to read-only, only supported on some interfaces
 #bus.state = BusState.PASSIVE
count=0
new_dict1={}

with can.interface.Bus(bustype="socketcan", channel="can0", bitrate=250000) as bus:
 db = cantools.database.load_file('/home/pi/durapower_jp.dbc') #path of .dbc file
 ##for all bmu
 msg1=can.Message(arbitration_id=0x00004200, data=[0x00],is_remote_frame=False, is_extended_id=True, dlc=8)
 bus.send(msg1)

 for msg in bus:
  
  try:
   
   print(msg)
   json_data=db.decode_message(msg.arbitration_id, msg.data)
   for key in json_data.keys():
    new_dict1[key]=json_data[key]
   
   
   count=count+1
   #time.sleep(1)
   print(count)
   if(count==20):
    break
  except:
   count=count+1
   print(count)
   if(count==20):
    break
   pass
  # time.sleep(1)
 