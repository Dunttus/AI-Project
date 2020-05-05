#!/bin/bash
# Parses metadata away from journalctl json output,
# and formats the data to csv: "message",priority [0-7]
# There might be no priority number!

SYSTEMD_VERSION=$(systemd --version | grep systemd | sed 's/systemd //')
echo "systemd v.: $SYSTEMD_VERSION"

if [[ $SYSTEMD_VERSION -ne 237 ]]; then
	echo "Systemd -version has to be 237. Aborting..."
	break
fi
# This is 237 (Ubuntu 18.04)
sudo journalctl -n 5 -o json --output-fields=PRIORITY,MESSAGE |
sed -E 's/"__CURSOR" : "[^"]*"//;
	s/"_BOOT_ID" : "[^"]*"//;
	s/"__MONOTONIC_TIMESTAMP" : "[^"]*"//;
	s/"__REALTIME_TIMESTAMP" : "[^"]*"//;
# Beginning curly brackets and any number of commas after
	s/^\{,*//;
# Last curly bracket and any number of commas before
	s/,*}$//;
# If the priority is now first, move it to end
	s/^("PRIORITY" : "[0-9]?"),(.*)/\2,\1/;
# Remove labels
	s/"PRIORITY" : "([0-7]?)"/\1/;
	s/"MESSAGE" ://;
# Remove additional commas
	s/[ ,]*//' > testdataset
