import socket
import subprocess
import shutil
hostname = socket.gethostname()

hostname = socket.gethostname()
uptime = subprocess.check_output(["uptime","-p"]).decode().strip()
disk = shutil.disk_usage("/")
print(f"Hostname: {hostname}")
print(f"Uptime: {uptime}")
print(f"Disk usage: {disk.used // (1024**3)} GB / {disk.total // (1024**3)} GB")
