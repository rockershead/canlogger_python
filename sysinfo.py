import can
from can.bus import BusState
import time
import cantools

count=0
new_dict1={}
alarm={}

def sys_level_fault(binary_data,rack_no,level):
 sys_level_fault_object={}
 sys_level_fault_object['B'+str(rack_no)+'_SYS_LEVEL_'+str(level)+'_FAULT_CVL']=binary_data[len(binary_data)-1]
 sys_level_fault_object['B'+str(rack_no)+'_SYS_LEVEL_'+str(level)+'_FAULT_CVH']=binary_data[len(binary_data)-2]
 sys_level_fault_object['B'+str(rack_no)+'_SYS_LEVEL_'+str(level)+'_FAULT_BVL']=binary_data[len(binary_data)-3]
 sys_level_fault_object['B'+str(rack_no)+'_SYS_LEVEL_'+str(level)+'_FAULT_BVH']=binary_data[len(binary_data)-4]
 sys_level_fault_object['B'+str(rack_no)+'_SYS_LEVEL_'+str(level)+'_FAULT_CTL']=binary_data[len(binary_data)-5]
 sys_level_fault_object['B'+str(rack_no)+'_SYS_LEVEL_'+str(level)+'_FAULT_CTH']=binary_data[len(binary_data)-6]
 sys_level_fault_object['B'+str(rack_no)+'_SYS_LEVEL_'+str(level)+'_FAULT_DTL']=binary_data[len(binary_data)-7]
 sys_level_fault_object['B'+str(rack_no)+'_SYS_LEVEL_'+str(level)+'_FAULT_DTH']=binary_data[len(binary_data)-8]
 sys_level_fault_object['B'+str(rack_no)+'_SYS_LEVEL_'+str(level)+'_FAULT_COC']=binary_data[len(binary_data)-9]
 sys_level_fault_object['B'+str(rack_no)+'_SYS_LEVEL_'+str(level)+'_FAULT_DOC']=binary_data[len(binary_data)-10]
 sys_level_fault_object['B'+str(rack_no)+'_SYS_LEVEL_'+str(level)+'_FAULT_RES']=binary_data[len(binary_data)-11]
 sys_level_fault_object['B'+str(rack_no)+'_SYS_LEVEL_'+str(level)+'_FAULT_RES1']=binary_data[len(binary_data)-12]
 sys_level_fault_object['B'+str(rack_no)+'_SYS_LEVEL_'+str(level)+'_FAULT_IF']=binary_data[len(binary_data)-13]
 sys_level_fault_object['B'+str(rack_no)+'_SYS_LEVEL_'+str(level)+'_FAULT_SOCTL']=binary_data[len(binary_data)-14]
 sys_level_fault_object['B'+str(rack_no)+'_SYS_LEVEL_'+str(level)+'_FAULT_CVI']=binary_data[len(binary_data)-15]
 sys_level_fault_object['B'+str(rack_no)+'_SYS_LEVEL_'+str(level)+'_FAULT_TSI']=binary_data[len(binary_data)-16]
 
 return sys_level_fault_object
  


def alarm_decode(data,rack_no):
 global alarm
 sys_status_bit={}
 sys_failure_bit={}
 print(data)
 ##first byte##
 first_byte=data[0]+data[1]
 binary_first_byte=bin(int('1'+first_byte, 16))[3:]
 param_name='B'+str(rack_no)+'_SYS_STATUS_BIT'
 sys_status_bit['B'+str(rack_no)+'_SYS_STATUS_BIT_RFC']=int(binary_first_byte[len(binary_first_byte)-4])
 sys_status_bit['B'+str(rack_no)+'_SYS_STATUS_BIT_RE']=int(binary_first_byte[len(binary_first_byte)-5])
 sys_status_bit['B'+str(rack_no)+'_SYS_STATUS_BIT_MR']=int(binary_first_byte[len(binary_first_byte)-6])

 alarm[param_name]=sys_status_bit

 ##second byte###
 second_byte=data[2]+data[3]
 binary_second_byte=bin(int('1'+second_byte, 16))[3:]
 param_name='B'+str(rack_no)+'_SYS_FAILURE_BIT'
 sys_failure_bit['B'+str(rack_no)+'_SYS_FAILURE_BIT_CE']=int(binary_second_byte[len(binary_second_byte)-1])
 sys_failure_bit['B'+str(rack_no)+'_SYS_FAILURE_BIT_TE']=int(binary_second_byte[len(binary_second_byte)-2])
 sys_failure_bit['B'+str(rack_no)+'_SYS_FAILURE_BIT_ICE']=int(binary_second_byte[len(binary_second_byte)-3])
 sys_failure_bit['B'+str(rack_no)+'_SYS_FAILURE_BIT_DCO_ER']=int(binary_second_byte[len(binary_second_byte)-4])
 sys_failure_bit['B'+str(rack_no)+'_SYS_FAILURE_BIT_RPE']=int(binary_second_byte[len(binary_second_byte)-5])
 sys_failure_bit['B'+str(rack_no)+'_SYS_FAILURE_BIT_RE']=int(binary_second_byte[len(binary_second_byte)-6])
 
 
 alarm[param_name]=sys_failure_bit

 ##third and fourth byte.sys level 1 fault#########################################################################
 third_and_fourth_byte=data[4]+data[5]+data[6]+data[7]
 binary_third_and_fourth_byte=bin(int('1'+third_and_fourth_byte, 16))[3:]
 param_name='B'+str(rack_no)+'_SYS_LEVEL_1_FAULT'
 alarm[param_name]=sys_level_fault(binary_third_and_fourth_byte,rack_no,1)

 ##fifth and sixth byte.sys level 2 fault##
 fifth_and_sixth_byte=data[8]+data[9]+data[10]+data[11]
 binary_fifth_and_sixth_byte=bin(int('1'+fifth_and_sixth_byte, 16))[3:]
 param_name='B'+str(rack_no)+'_SYS_LEVEL_2_FAULT'
 alarm[param_name]=sys_level_fault(binary_fifth_and_sixth_byte,rack_no,2)

 ##seventh and eighth byte.sys level 3 fault##
 seventh_and_eighth_byte=data[12]+data[13]+data[14]+data[15]
 binary_seventh_and_eighth_byte=bin(int('1'+seventh_and_eighth_byte, 16))[3:]
 param_name='B'+str(rack_no)+'_SYS_LEVEL_3_FAULT'
 alarm[param_name]=sys_level_fault(binary_seventh_and_eighth_byte,rack_no,3)
 



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
   
   print(count)
   if(count==20):
    
    break
  except:
   ##alarm data processed here
   if(int(msg.arbitration_id)==int(0x00004250) ):
    alarm_decode(msg.data.hex(),1)
   if(int(msg.arbitration_id)==int(0x00004251) ):
    alarm_decode(msg.data.hex(),2)
   if(int(msg.arbitration_id)==int(0x00004252) ):
    alarm_decode(msg.data.hex(),3)
   if(int(msg.arbitration_id)==int(0x00004253) ):
    alarm_decode(msg.data.hex(),4)

   count=count+1
   print(count)
   if(count==20):
    
    break
   pass
  
 