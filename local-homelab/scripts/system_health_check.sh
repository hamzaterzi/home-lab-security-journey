#!/bin/bash

echo "=============================="
echo " System Health Check Report"
echo "=============================="
echo

echo "[1] Host Information"
echo "Hostname: $(hostname)"
echo "Current User: $(whoami)"
echo "Date: $(date)"
echo

echo "[2] IP Addresses"
hostname -I
echo

echo "[3] Disk Usage"
df -h /
echo

echo "[4] Service Status"
for service in ssh nginx fail2ban; do
    if systemctl is-active --quiet "$service"; then
        echo "$service: ACTIVE"
    else
        echo "$service: INACTIVE"
    fi
done
echo

echo "[5] Listening Ports"
ss -tuln | grep -E '(:22|:80)'
echo

echo "[6] Firewall Status"
ufw status verbose
echo

echo "[7] Recent SSH Log Entries"
tail -n 5 /var/log/auth.log
echo

echo "[8] Recent Nginx Access Log Entries"
tail -n 5 /var/log/nginx/access.log
echo

echo "Health check completed."
