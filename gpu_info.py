pip install gputil
import GPUtil
from tabulate import tabulate

try: 
  print("="*40, "GPU Details", "="*40)
  gpus = GPUtil.getGPUs()
  list_gpus = []
  for gpu in gpus:
      # get the GPU id
      gpu_id = gpu.id
      # name of GPU
      gpu_name = gpu.name
      # get % percentage of GPU usage of that GPU
      gpu_load = f"{gpu.load*100}%"
      # get free memory in MB format
      gpu_free_memory = f"{gpu.memoryFree}MB"
      # get used memory
      gpu_used_memory = f"{gpu.memoryUsed}MB"
      # get total memory
      gpu_total_memory = f"{gpu.memoryTotal}MB"
      # get GPU temperature in Celsius
      gpu_temperature = f"{gpu.temperature} °C"
      gpu_uuid = gpu.uuid
      list_gpus.append((
          gpu_id, gpu_name, gpu_load, gpu_free_memory, gpu_used_memory,
          gpu_total_memory, gpu_temperature, gpu_uuid
      ))

  print(tabulate(list_gpus, headers=("id", "name", "load", "free memory", "used memory", "total memory",
                                    "temperature", "uuid")))
  
except: 
  print ("Could not communicate with a GPU. This could be becasue the runtime is not connected to a GPU.")

from psutil import virtual_memory
ram_gb = virtual_memory().total / 1e9
print('Your runtime has {:.1f} gigabytes of available RAM\n'.format(ram_gb))

if ram_gb < 20:
  print('Not using a high-RAM runtime')
else:
  print('Using a high-RAM runtime!')
