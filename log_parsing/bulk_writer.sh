#!/bin/bash
set -e

# ElasticSearch bulk API

# Log JSON's can be created with journalctl:
# sudo journalctl -o json > bulktest.json

# Rewrite the JSON file to conform bulk API format:
sed 'i\{"index":{}}' bulktest.json > bulktest2.json

# Curl the file into database
curl 	-s -o /dev/null -H "Content-Type: application/x-ndjson" \
	-XPOST localhost:9200/hugebulktest/_bulk?pretty=true \
	--data-binary "@bulktest2.json"

