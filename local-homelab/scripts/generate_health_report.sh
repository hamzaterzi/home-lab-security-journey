#!/bin/bash

TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
OUTPUT="/home/labadmin/reports/bash/health_report_${TIMESTAMP}.txt"

/home/labadmin/scripts/system_health_check.sh > "$OUTPUT"
chown labadmin:labadmin "$OUTPUT"

echo "Health report saved to: $OUTPUT"
