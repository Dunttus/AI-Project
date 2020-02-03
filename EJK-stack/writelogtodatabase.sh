#!/bin/bash
set -e

display_help() { 
echo ''' 
EJK-script usage:
Helpful information coming your way soon(tm).
'''
}

if [[ -z "$1" ]]; then display_help
	echo ERROR: No arguments specified 
	exit
fi

check_user() {
	if [ $(id -u) != 0 ]; then
		echo For full logs, run the script as root
	fi
}

while read line; do
	curl -XPOST localhost:9200/$1/_doc/?filter_path=_seq_no \
	-H 'Content-type:application/json' \
	-d "$line"
done < $2
