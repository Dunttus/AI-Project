#!/bin/bash
# Parses metadata from journalctl json output

sudo journalctl -o json --output-fields=PRIORITY,MESSAGE |
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
# Parses priority to a mere number
	s/"PRIORITY":"([0-7]?)"/\1/;
# Remove more
	s/"MESSAGE"://' > testdataset.json
	
# TODO: the order varies, make it constant (priority,"message")	

