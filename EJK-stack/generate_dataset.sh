#!/bin/bash
# Parses metadata from journalctl json output

sudo journalctl -o json --output-fields=PRIORITY,MESSAGE |
sed -E 's/"__CURSOR":"[^"]*"//;
	s/"_BOOT_ID":"[^"]*"//;
	s/"__MONOTONIC_TIMESTAMP":"[^"]*"//;
	s/"__REALTIME_TIMESTAMP":"[^"]*"//' > testdataset.json
