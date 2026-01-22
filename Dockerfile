# 1) Choose a base image that already has Python installed
FROM python:3.12-slim

# Install system utilities (uptime comes from procps)
RUN apt-get update \
    && apt-get install -y --no-install-recommends procps \
    && rm -rf /var/lib/apt/lists/*

# 2) Set a working directory inside the container
WORKDIR /app

# 3) Copy your script into the container image
COPY sysinfo.py /app/sysinfo.py

# 4) By default, run the script
CMD ["python", "/app/sysinfo.py"]
