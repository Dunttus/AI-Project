# Elasticsearch - Journalctl - Kibana

This directory contains scripts that manipulate journalctl generated JSON files. Big files need lots of memory, but the speedup with bulk API is considerable.

- elasticsearch database population with bulk API  
  Configurations in /etc/elasticsearch/
  * elastisearch.yml:
    * http.max_content_length: 1000mb
  * jvm.options:
    * Xms8g
    * Xmx8g
- elasticsearch database population with curl loop
- journalctl simple sed-based parser to csv format

## TODO:
- don't redirect curl output to /dev/null on bulk_writer to see if there were errors
- parse underscores for elasticsearch import
- make journalctl metadata timestamps human readable:
	__MONOTONIC_TIMESTAMP __REALTIME_TIMESTAMP
- format conversion, as everything is {"string":"string"}

### More TODO:
- systemd-journald-remote usage
- test with containers

For details and background, see blog posts:  
https://ailogs.design.blog/2020/02/01/elasticsearch-journalctl-kibana/  
https://ailogs.design.blog/2020/02/10/supervised-learning-model-construction/  
https://ailogs.design.blog/2020/02/24/classifying-logs-gathering-data/  
