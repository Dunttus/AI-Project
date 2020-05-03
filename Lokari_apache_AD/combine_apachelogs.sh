#!/bin/bash
folder=/AI-Project/Lokari_apache_AD/training_dataset
cp /accesslog/access.log.* $folder
gunzip $folder/access.log.*
cat $folder/access.log.* > $folder/access.log
rm $folder/access.log.*
