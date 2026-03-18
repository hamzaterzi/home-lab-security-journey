#!/usr/bin/env python3

import json
import socket
import shutil
import subprocess
from datetime import datetime


def run_command(command: str) -> str:
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout.strip()


def check_service(service_name: str) -> str:
    result = subprocess.run(
        f"systemctl is-active {service_name}",
        shell=True,
        capture_output=True,
        text=True
    )
    return result.stdout.strip().upper()


timestamp = datetime.now()
timestamp_str = timestamp.strftime("%Y-%m-%d_%H-%M-%S")

report = {
    "hostname": socket.gethostname(),
    "date": str(timestamp),
    "ip_addresses": run_command("hostname -I").split(),
    "disk_usage": {},
    "services": {},
    "listening_ports": run_command("ss -tuln | grep -E '(:22|:80)'").splitlines()
}

total, used, free = shutil.disk_usage("/")
report["disk_usage"] = {
    "total_gb": total // (1024**3),
    "used_gb": used // (1024**3),
    "free_gb": free // (1024**3)
}

for service in ["ssh", "nginx", "fail2ban"]:
    report["services"][service] = check_service(service)

output_file = f"/home/labadmin/reports/python/python_health_report_{timestamp_str}.json"

with open(output_file, "w") as f:
    json.dump(report, f, indent=4)

print("JSON health report saved to:")
print(output_file)
