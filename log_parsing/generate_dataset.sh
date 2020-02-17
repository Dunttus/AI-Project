#!/bin/bash
# Parses metadata away from journalctl json output,
# and formats the data to csv: "message",priority [0-7]
# There might be no priority number!

sudo journalctl -n 5 -o json --output-fields=PRIORITY,MESSAGE |
sed -E 's/"__CURSOR":"[^"]*"//;
	s/"_BOOT_ID":"[^"]*"//;
	s/"__MONOTONIC_TIMESTAMP":"[^"]*"//;
	s/"__REALTIME_TIMESTAMP":"[^"]*"//;
# Beginning curly brackets and any number of commas after
	s/^\{,*//;
# Last curly bracket and any number of commas before
	s/,*}$//;
# Trim separator to only one comma
	s/",*"/","/;
# If the priority is now first, move it to end
	s/^("PRIORITY":"[0-9]?"),(.*)/\2,\1/;
# Remove labels
	s/"PRIORITY":"([0-7]?)"/\1/;
	s/"MESSAGE"://' > testdataset.json
