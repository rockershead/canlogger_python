import can
from can.bus import BusState
import time
import cantools
import time



with can.interface.Bus(bustype="socketcan", channel="can0", bitrate=250000) as bus:
 db = cantools.database.load_file('/home/pi/durapower_jp.dbc')
 msg=can.Message(arbitration_id=0x00004200, data=[0x02],is_remote_frame=False, is_extended_id=True, dlc=8)
 bus.send(msg)
 #message = bus.recv()
 #print(message)
 for msg in bus:
  print(msg)
  json_data=db.decode_message(msg.arbitration_id, msg.data)
  print(json_data)
  time.sleep(1)
