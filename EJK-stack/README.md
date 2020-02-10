# Elasticsearch - Journalctl - Kibana

This directory contains scripts that manipulate journalctl generated JSON files.

- elasticsearch database population with curl loop
- journalctl simple parser

## TODO:
- _bulk API instead of a slow curl loop
- parse underscores somehow so elasticsearch can use them better
- make simple parser to CSV format
- examine "Unexpected character ('p' (code 112))" Errors
- make journalctl metadata timestamps human readable:
	__MONOTONIC_TIMESTAMP __REALTIME_TIMESTAMP
- format conversion, as everything is {"string":"string"}

### More TODO:
- systemd-journald-remote usage
- test with containers

For details and background, see blog posts:  
https://ailogs.design.blog/2020/02/01/elasticsearch-journalctl-kibana/  
https://ailogs.design.blog/2020/02/10/supervised-learning-model-construction/  
