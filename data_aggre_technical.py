import time
from datetime import datetime
from cell_voltage import new_dict3
from module_temp import new_dict4
import json

count=0
timestamp=datetime.now().isoformat()
combine_dict2={**new_dict3,**new_dict4}

combine_dict2["timestamp"]=timestamp

combine_dict_json2=json.dumps(combine_dict2)
print(combine_dict_json2)
