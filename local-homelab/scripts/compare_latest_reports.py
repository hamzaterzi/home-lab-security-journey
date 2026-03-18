#!/usr/bin/env python3

import glob
import json
import os


report_files = sorted(
    glob.glob("/home/labadmin/reports/python/python_health_report_*.json"),
    key=os.path.getmtime
)

if len(report_files) < 2:
    print("Not enough JSON reports to compare.")
    exit(1)

old_report = report_files[-2]
new_report = report_files[-1]

with open(old_report, "r") as f:
    old_data = json.load(f)

with open(new_report, "r") as f:
    new_data = json.load(f)

print("===================================")
print(" JSON Report Comparison")
print("===================================\n")

print(f"Older report : {old_report}")
print(f"Newer report : {new_report}\n")

print("[1] Disk Usage Comparison")
old_disk = old_data["disk_usage"]
new_disk = new_data["disk_usage"]

print(f"Old used space: {old_disk['used_gb']} GB")
print(f"New used space: {new_disk['used_gb']} GB")
print(f"Difference    : {new_disk['used_gb'] - old_disk['used_gb']} GB\n")

print("[2] Service Status Changes")
service_changes = []

all_services = set(old_data["services"].keys()) | set(new_data["services"].keys())
for service in sorted(all_services):
    old_status = old_data["services"].get(service, "MISSING")
    new_status = new_data["services"].get(service, "MISSING")
    if old_status != new_status:
        service_changes.append(f"{service}: {old_status} -> {new_status}")

if service_changes:
    for change in service_changes:
        print(change)
else:
    print("No service status changes detected.")
print()

print("[3] Listening Port Changes")
old_ports = set(old_data["listening_ports"])
new_ports = set(new_data["listening_ports"])

added_ports = new_ports - old_ports
removed_ports = old_ports - new_ports

if added_ports:
    print("Added ports:")
    for port in added_ports:
        print(port)

if removed_ports:
    print("Removed ports:")
    for port in removed_ports:
        print(port)

if not added_ports and not removed_ports:
    print("No listening port changes detected.")

print("\nComparison completed.")
