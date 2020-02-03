# Elasticsearch - Journalctl - Kibana

For details, see blog post:  
https://ailogs.design.blog/2020/02/01/elasticsearch-journalctl-kibana/  

This directory contains scripts that move journalctl generated JSON files
into elasticsearch database.

## TODO:
- _bulk API instead of a slow curl loop
- parse underscores somehow so elasticsearch can use them better
- examine "Unexpected character ('p' (code 112))" Errors
- make journalctl metadata timestamps human readable:
	__MONOTONIC_TIMESTAMP __REALTIME_TIMESTAMP
- format conversion, as everything is {"string":"string"}

### More TODO:
- systemd-journald-remote usage
- test with containers

