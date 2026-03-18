#!/usr/bin/env python3

import glob
import json
import os


report_files = glob.glob("/home/labadmin/reports/python/python_health_report_*.json")

if not report_files:
    print("No JSON health reports found.")
    exit(1)

latest_report = max(report_files, key=os.path.getmtime)

with open(latest_report, "r") as f:
    data = json.load(f)

print("===================================")
print(" Latest JSON Health Report Summary")
print("===================================\n")

print(f"Report file : {latest_report}")
print(f"Hostname    : {data['hostname']}")
print(f"Date        : {data['date']}")
print(f"IP Addresses: {', '.join(data['ip_addresses'])}")
print()

disk = data["disk_usage"]
print("[Disk Usage]")
print(f"Total: {disk['total_gb']} GB")
print(f"Used : {disk['used_gb']} GB")
print(f"Free : {disk['free_gb']} GB")
print()

print("[Service Status]")
for service, status in data["services"].items():
    print(f"{service}: {status}")
print()

print("[Listening Ports]")
for port in data["listening_ports"]:
    print(port)
print()

print("[Warnings]")
warnings = []

if disk["total_gb"] > 0:
    used_percent = (disk["used_gb"] / disk["total_gb"]) * 100
    if used_percent >= 80:
        warnings.append(f"High disk usage detected: {used_percent:.1f}%")

for service, status in data["services"].items():
    if status != "ACTIVE":
        warnings.append(f"Service {service} is not active.")

ports_text = " ".join(data["listening_ports"])
if ":22" not in ports_text:
    warnings.append("Expected SSH port 22 is not listening.")
if ":80" not in ports_text:
    warnings.append("Expected HTTP port 80 is not listening.")

if warnings:
    for warning in warnings:
        print(f"WARNING: {warning}")
    overall_status = "WARNING"
else:
    print("No warnings detected. System looks healthy.")
    overall_status = "HEALTHY"

print()
print(f"OVERALL STATUS: {overall_status}")
print("\nSummary completed.")
