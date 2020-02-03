#!/bin/bash
set -e

display_help() { 
echo ''' 
EJK-script usage:
writelogtodatabase <index_name>

More helpful information coming your way soon(tm).
'''
}

if [[ $# != 1 ]]; then display_help
	echo ERROR: Wrong number of arguments
	exit
fi

check_user() {
	if [ $(id -u) != 0 ]; then
		echo For full logs, run the script as root
	fi
}

generate_json_file() {
	echo Generating JSON file from systemd-journl logs...
	journalctl -o json > $1.json
}

populate_database() {
	while read line; do
		curl -XPOST localhost:9200/$1/_doc/?filter_path=_seq_no \
		-H 'Content-type:application/json' \
		-d "$line"
	done < $1.json
}

generate_json_file $1
populate_database $1
