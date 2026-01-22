import socket
import subprocess
hostname = socket.gethostname()

hostname = socket.gethostname()
uptime = subprocess.check_output(["uptime","-p"]).decode().strip()
print(f"Hostname: {hostname}")
print(f"Uptime: {uptime}")
