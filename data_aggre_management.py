import time
from datetime import datetime
from sysinfo import new_dict1,alarm
from batt_info import new_dict2
import json

number_of_racks=4
count=0
computed_data={}
SUM_SOH=0
ACTUAL_CAPACITY_SUMMARY=0
ENERGY_THROUGHPUT_CHARGE_SUMMARY=0
ENERGY_THROUGHPUT_DISCHARGE_SUMMARY=0
TOTAL_ENERGY_SUMMARY=0
CAPACITY_THROUGHPUT_CHARGE_SUMMARY=0
CAPACITY_THROUGHPUT_DISCHARGE_SUMMARY=0

timestamp=datetime.now().isoformat()
combine_dict1={**new_dict1,**new_dict2}

combine_dict1["timestamp"]=timestamp

##do computation with the formulas
for rack_no in range(1,number_of_racks+1):
 computed_data['B'+str(rack_no)+'_ACTUAL_CAPACITY']=(combine_dict1['B'+str(rack_no)+'_BATT_CAPACITY'])*(combine_dict1['B'+str(rack_no)+'_SOH'])

 if(combine_dict1['B'+str(rack_no)+'_SYSCURRENT']>0):
  computed_data['B'+str(rack_no)+'_ENERGY_THROUGHPUT_DISCHARGE']=0
  computed_data['B'+str(rack_no)+'_ENERGY_THROUGHPUT_CHARGE']=(((combine_dict1['B'+str(rack_no)+'_SYSCURRENT'])*(combine_dict1['B'+str(rack_no)+'_SYSVOLTAGE']))/3600)/pow(10,6)
 elif(combine_dict1['B'+str(rack_no)+'_SYSCURRENT']<0):
  computed_data['B'+str(rack_no)+'_ENERGY_THROUGHPUT_CHARGE']=0
  computed_data['B'+str(rack_no)+'_ENERGY_THROUGHPUT_DISCHARGE']=(((combine_dict1['B'+str(rack_no)+'_SYSCURRENT'])*(combine_dict1['B'+str(rack_no)+'_SYSVOLTAGE']))/3600)/pow(10,6)
 else:
  computed_data['B'+str(rack_no)+'_ENERGY_THROUGHPUT_CHARGE']=0
  computed_data['B'+str(rack_no)+'_ENERGY_THROUGHPUT_DISCHARGE']=0

 

 computed_data['B'+str(rack_no)+'_TOTAL_ENERGY']=computed_data['B'+str(rack_no)+'_ENERGY_THROUGHPUT_CHARGE']+computed_data['B'+str(rack_no)+'_ENERGY_THROUGHPUT_DISCHARGE']
 
 if(combine_dict1['B'+str(rack_no)+'_SYSCURRENT']>0):
  computed_data['B'+str(rack_no)+'_CAPACITY_THROUGHPUT_CHARGE']=((combine_dict1['B'+str(rack_no)+'_SYSCURRENT'])/3600)/pow(10,6)
  computed_data['B'+str(rack_no)+'_CAPACITY_THROUGHPUT_DISCHARGE']=0
 elif(combine_dict1['B'+str(rack_no)+'_SYSCURRENT']<0):
  computed_data['B'+str(rack_no)+'_CAPACITY_THROUGHPUT_DISCHARGE']=((combine_dict1['B'+str(rack_no)+'_SYSCURRENT'])/3600)/pow(10,6)
  computed_data['B'+str(rack_no)+'_CAPACITY_THROUGHPUT_CHARGE']=0
 else:
  computed_data['B'+str(rack_no)+'_CAPACITY_THROUGHPUT_DISCHARGE']=0
  computed_data['B'+str(rack_no)+'_CAPACITY_THROUGHPUT_CHARGE']=0

 computed_data['B'+str(rack_no)+'_EQUIVALENT_FULL_CHARGE_CYCLES']=(computed_data['B'+str(rack_no)+'_ENERGY_THROUGHPUT_CHARGE']+computed_data['B'+str(rack_no)+'_ENERGY_THROUGHPUT_DISCHARGE'])/(computed_data['B'+str(rack_no)+'_ACTUAL_CAPACITY'])
 
 ##calculating sums
 SUM_SOH=SUM_SOH+combine_dict1['B'+str(rack_no)+'_SOH']
 ACTUAL_CAPACITY_SUMMARY=ACTUAL_CAPACITY_SUMMARY+computed_data['B'+str(rack_no)+'_ACTUAL_CAPACITY']
 ENERGY_THROUGHPUT_CHARGE_SUMMARY=ENERGY_THROUGHPUT_CHARGE_SUMMARY+computed_data['B'+str(rack_no)+'_ENERGY_THROUGHPUT_CHARGE']
 ENERGY_THROUGHPUT_DISCHARGE_SUMMARY=ENERGY_THROUGHPUT_DISCHARGE_SUMMARY+computed_data['B'+str(rack_no)+'_ENERGY_THROUGHPUT_DISCHARGE']
 TOTAL_ENERGY_SUMMARY=TOTAL_ENERGY_SUMMARY+computed_data['B'+str(rack_no)+'_TOTAL_ENERGY']
 CAPACITY_THROUGHPUT_CHARGE_SUMMARY=CAPACITY_THROUGHPUT_CHARGE_SUMMARY+computed_data['B'+str(rack_no)+'_CAPACITY_THROUGHPUT_CHARGE']
 CAPACITY_THROUGHPUT_DISCHARGE_SUMMARY=CAPACITY_THROUGHPUT_DISCHARGE_SUMMARY+computed_data['B'+str(rack_no)+'_CAPACITY_THROUGHPUT_DISCHARGE']

computed_data['SOH_SUMMARY']=SUM_SOH/number_of_racks
computed_data['ACTUAL_CAPACITY_SUMMARY']=ACTUAL_CAPACITY_SUMMARY
computed_data['ENERGY_THROUGHPUT_CHARGE_SUMMARY']=ENERGY_THROUGHPUT_CHARGE_SUMMARY
computed_data['ENERGY_THROUGHPUT_DISCHARGE_SUMMARY']=ENERGY_THROUGHPUT_DISCHARGE_SUMMARY
computed_data['TOTAL_ENERGY_SUMMARY']=TOTAL_ENERGY_SUMMARY
computed_data['CAPACITY_THROUGHPUT_CHARGE_SUMMARY']=CAPACITY_THROUGHPUT_CHARGE_SUMMARY
computed_data['CAPACITY_THROUGHPUT_DISCHARGE_SUMMARY']=CAPACITY_THROUGHPUT_DISCHARGE_SUMMARY
computed_data['EQUIVALENT_FULL_CHARGE_CYCLES_SUMMARY']=(ENERGY_THROUGHPUT_CHARGE_SUMMARY+ENERGY_THROUGHPUT_DISCHARGE_SUMMARY)/(ACTUAL_CAPACITY_SUMMARY)
computed_data['timestamp']=timestamp

combine_dict_json1=json.dumps(combine_dict1)
computed_data_json=json.dumps(computed_data)
alarm["timestamp"]=timestamp
json_full_alarm={"STATUS":alarm}
json_alarm=json.dumps(json_full_alarm)

print(combine_dict_json1)
