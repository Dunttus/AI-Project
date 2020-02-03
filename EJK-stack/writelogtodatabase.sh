#!/bin/bash
while read line; do
	curl -XPOST localhost:9200/$1/_doc/?filter_path=_seq_no \
	-H 'Content-type:application/json' \
	-d "$line"
done < $2
