# Installation Instructions

Run
```bash
docker build -m sysinfo .
```

# Usage

To use the program, run
```bash
docker run --rm sysinfo
```

To ommit the uptime or disk usage
```bash
docker run --rm -e SHOW_UPTIME=false SHOW_DISK=false sysinfo
```
