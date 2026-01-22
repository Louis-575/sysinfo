import os
import socket
import subprocess
import shutil

hostname = socket.gethostname()
print(f"Hostname: {hostname}")

# Optional, uses environement variable
if os.getenv("SHOW_UPTIME", "true").lower() == "true":
    uptime = subprocess.check_output(["uptime", "-p"]).decode().strip()
    print(f"Uptime: {uptime}")


# Optional, uses environement variable
if os.getenv("SHOW_DISK", "true").lower() == "true":
    disk = shutil.disk_usage("/")
    print(f"Disk usage: {disk.used // (1024**3)} GB / {disk.total // (1024**3)} GB")
