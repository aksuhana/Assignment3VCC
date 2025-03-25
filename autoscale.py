import psutil
import subprocess
import time


CPU_THRESHOLD_UP = 75
CPU_THRESHOLD_DOWN = 50
MEM_THRESHOLD_UP = 75
MEM_THRESHOLD_DOWN = 50
ZONE = "us-central1-a"
GROUP = "my-group"


def get_cpu_mem():
   cpu = psutil.cpu_percent(interval=2)
   mem = psutil.virtual_memory().percent
   print(f"CPU: {cpu}%, Memory: {mem}%")
   return cpu, mem


def get_current_group_size():
   result = subprocess.run([
       "gcloud", "compute", "instance-groups", "managed", "list-instances", GROUP,
       "--zone", ZONE, "--format=value(name)"
   ], capture_output=True, text=True)


   instances = result.stdout.strip().split('\n')
   return len([i for i in instances if i.strip() != ""])


def scale_group(new_size):
   print(f"Scaling instance group to size: {new_size}")
   subprocess.run([
       "gcloud", "compute", "instance-groups", "managed", "resize",
       GROUP, f"--size={new_size}", "--zone", ZONE
   ])


while True:
   cpu, mem = get_cpu_mem()
   current_size = get_current_group_size()
   print(f"Current group size: {current_size}")


   if cpu > CPU_THRESHOLD_UP or mem > MEM_THRESHOLD_UP:
       if current_size < 2:
           scale_group(current_size + 1)
       else:
           print("Already scaled up.")
   elif cpu < CPU_THRESHOLD_DOWN and mem < MEM_THRESHOLD_DOWN:
       if current_size > 1:
           scale_group(current_size - 1)
       else:
           print("Already at minimum size.")
   else:
       print("Usage in balanced range, no scaling.")


   print("-" * 50)
   time.sleep(20)
