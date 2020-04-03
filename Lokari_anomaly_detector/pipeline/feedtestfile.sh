#!/bin/bash

# Test the realtime_log_reading.py code
# Send lines with timestamps to testfile and see if python code produces it

for i in {1..1000}; do
	echo "$i $(date -Ins)" >> testfile
done
