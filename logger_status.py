import os
import psutil





tempC = os.popen("vcgencmd measure_temp").readline()
tempC = float(tempC[5:9])



# Get cpu statistics
cpu = str(psutil.cpu_percent()) + '%'

# Calculate memory information
memory = psutil.virtual_memory()
# Convert Bytes to MB (Bytes -> KB -> MB)
ram_available = round(memory.available/1024.0/1024.0/1024,1)

ram_total = round(memory.total/1024.0/1024.0/1024,1)

ram_used=ram_total-ram_available





# Calculate disk information
disk = psutil.disk_usage('/')
# Convert Bytes to GB (Bytes -> KB -> MB -> GB)
storage_free = round(disk.free/1024.0/1024.0/1024.0,1)

storage_total = round(disk.total/1024.0/1024.0/1024.0,1)
storage_used=storage_total-storage_free
storage_used="{:.1f}".format(storage_used)


device_status={}
device_status['JP_STR1_CPU']=cpu
device_status['JP_STR1_RAM_USED']=ram_used
device_status['JP_STR1_RAM_TOTAL']=ram_total
device_status['JP_STR1_RAM_REM']=ram_available
device_status['JP_STR1_CPU_TEMP']=tempC
device_status['JP_STR1_STO_USED']=storage_used
device_status['JP_STR1_STO_TOTAL']=storage_total
device_status['JP_STR1_STO_REM']=storage_free
#print(device_status)