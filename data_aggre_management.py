import time
from datetime import datetime
from sysinfo import new_dict1
from batt_info import new_dict2
import json

count=0
timestamp=datetime.now().isoformat()
combine_dict1={**new_dict1,**new_dict2}

combine_dict1["timestamp"]=timestamp

combine_dict_json1=json.dumps(combine_dict1)
print(combine_dict_json1)
