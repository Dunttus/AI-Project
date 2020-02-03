#!/bin/bash
set -e

display_help() { 
echo ''' 
EJK-script usage:
Helpful information coming your way soon(tm).
'''
}

if [[ $# != 2 ]]; then display_help
	echo ERROR: Not enough arguments
	exit
fi

check_user() {
	if [ $(id -u) != 0 ]; then
		echo For full logs, run the script as root
	fi
}

populate_database {
	while read line; do
		curl -XPOST localhost:9200/$1/_doc/?filter_path=_seq_no \
		-H 'Content-type:application/json' \
		-d "$line"
	done < $2
}
