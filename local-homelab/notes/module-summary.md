# Local Home Lab Module Summary

## Environment
- Hypervisor: VirtualBox
- VM 1: Ubuntu Server
- VM 2: Kali Linux
- VM 3: Windows Server
- Internal Network: Host-only
- Internet Access: NAT

## Module 1 – Initial Setup
- Imported Kali Linux into VirtualBox
- Installed Ubuntu Server
- Configured NAT networking for internet access
- Added Host-only networking for internal lab communication
- Established SSH connectivity from Kali to Ubuntu

## Module 2 – User and Firewall Configuration
- Created labadmin user
- Added labadmin to sudo group
- Enabled UFW firewall
- Allowed OpenSSH only
- Disabled root SSH login

## Module 3 – SSH Key Authentication
- Generated ED25519 key pair on Kali
- Copied public key to Ubuntu
- Verified key-based SSH login
- Disabled password authentication

## Module 4 – Web Server Deployment
- Installed Nginx on Ubuntu
- Allowed HTTP in UFW
- Verified port 80 from Kali
- Tested page delivery with curl
- Published a custom Nginx test page

## Module 5 – Log Analysis
- Reviewed SSH service logs with journalctl
- Reviewed /var/log/auth.log
- Reviewed Nginx access and error logs
- Observed successful SSH and HTTP events in logs

## Module 6 – Nmap Service Discovery
- Ran Nmap service/version detection
- Identified OpenSSH and Nginx on Ubuntu
- Performed a full TCP port scan
- Confirmed only ports 22 and 80 were open
- Observed Nmap scan activity in Nginx access logs

## Module 7 – Fail2ban Protection
- Installed Fail2ban
- Enabled the sshd jail
- Configured retry, findtime, and bantime settings
- Observed failed SSH attempts in logs

## Module 8 – Bash Automation
- Created system_health_check.sh
- Reported host, user, date, IP addresses, disk usage, service status, and listening ports
- Made the script executable and validated successful execution

## Module 9 – Enhanced Reporting
- Extended the Bash script with firewall status
- Added recent SSH log entries
- Added recent Nginx access log entries
- Exported the report to health_report.txt

## Module 10 – Scheduled Reporting with Cron
- Created a timestamp-based Bash wrapper script for system health reporting
- Generated dated health report files automatically
- Configured root crontab to execute the reporting workflow every 5 minutes
- Verified successful scheduled report creation on Ubuntu Server

## Module 11 – Python Health Check
- Created a Python-based system health check script
- Collected hostname, timestamp, IP addresses, and disk usage
- Checked service status for SSH, Nginx, and Fail2ban
- Displayed listening ports for key services
- Validated successful execution on Ubuntu Server

## Module 12 – Python JSON Reporting
- Extended the Python health check script to export structured JSON output
- Captured host metadata, IP addresses, disk usage, service states, and listening ports
- Generated timestamped JSON reports for machine-readable diagnostics

## Module 13 – JSON Report Reader
- Created a Python script to locate the latest generated JSON health report
- Parsed structured system data from the report file
- Displayed a summarized view of host, disk, service, and port information
- Validated a multi-step automation flow where one script generates data and another consumes it

## Module 14 – Health Warning Logic
- Enhanced the JSON report reader with basic health evaluation logic
- Added checks for disk usage thresholds
- Added checks for inactive services
- Added checks for expected listening ports
- Confirmed healthy state reporting when no issues were detected

## Module 15 – Warning Logic Validation
- Simulated a service outage by stopping Nginx
- Generated a new JSON health report during the outage
- Confirmed that the report reader raised warnings for inactive service state and missing expected port
- Restarted Nginx and verified that warnings disappeared after service recovery

## Module 16 – Overall Health Status
- Enhanced the JSON report reader with an overall system state label
- Reported HEALTHY when no issues were detected
- Reported WARNING when service, port, or disk checks failed
- Improved readability of automated monitoring output

## Module 17 – JSON Report Comparison
- Created a Python script to compare the two most recent JSON health reports
- Compared disk usage values between reports
- Detected service state changes between report snapshots
- Detected listening port changes between report snapshots
- Verified stable system state by confirming no differences across recent reports

## Module 18 – Report and Script Organization
- Organized the lab into dedicated directories for scripts and generated reports
- Separated Bash text reports and Python JSON reports into different folders
- Updated all script paths to use the new project structure
- Verified that reading, comparison, and scheduled reporting continued to work after reorganization

## Module 19 – Windows Server Lab Integration
- Installed Windows Server 2022 Standard Evaluation (Desktop Experience) in VirtualBox
- Added Windows Server to the same host-only network as Ubuntu and Kali
- Assigned a static internal IP address to Windows Server
- Verified internal network communication with Ubuntu and Kali

## Module 20 – Windows Server Network Integration
- Confirmed bidirectional network communication inside the lab
- Enabled ICMP echo request rules in Windows Defender Firewall
- Verified successful ping communication from Ubuntu and Kali to Windows Server

## Module 21 – Windows Firewall Overview
- Reviewed Windows Defender Firewall profile settings on Windows Server
- Confirmed that Domain, Private, and Public profiles were enabled
- Verified default policy as BlockInbound and AllowOutbound across all profiles
- Observed the configured firewall log path and noted that connection logging was disabled by default

## Module 22 – RDP Availability Check
- Verified active listening ports on Windows Server with netstat
- Confirmed that RDP was not initially enabled because port 3389 was not listening
- Identified baseline Windows services such as RPC, SMB, and WinRM as active listeners

## Module 23 – RDP Enablement
- Enabled Remote Desktop on Windows Server
- Verified that port 3389 was listening after RDP activation
- Confirmed that Windows Server was ready for remote desktop access over the internal lab network

## Module 24 – RDP Validation
- Tested Remote Desktop access from the host machine to the Windows Server VM
- Authenticated successfully with the local Administrator account
- Confirmed practical remote administration over the internal lab network

## Module 25 – Windows Event Viewer Basics
- Reviewed Windows Security logs in Event Viewer
- Observed successful and failed audit events
- Identified important security event IDs such as 4624, 4625, and 4672
- Recognized the relationship between successful logons, failed logons, and privileged sessions

## Module 26 – Failed Logon Event Validation
- Triggered and identified failed authentication attempts in Windows Security logs
- Verified that Event ID 4625 corresponded to failed logon activity
- Practiced event-based validation of authentication failures on Windows Server

## Module 27 – Windows Service Exposure Validation
- Scanned Windows Server from the Kali VM using Nmap
- Confirmed that RDP (3389) and WinRM (5985) were externally reachable
- Observed that ports 135, 139, and 445 were filtered despite appearing as listening locally
- Compared inside-view service visibility with externally exposed network surface

## Module 28 – WinRM Exposure Awareness
- Verified that WinRM was listening on port 5985 on Windows Server
- Confirmed external visibility of WinRM from the Kali VM
- Recognized WinRM as an additional remote management surface alongside RDP
- Related Windows management exposure to security monitoring and attack surface concepts
