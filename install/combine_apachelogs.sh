#!/bin/bash
folder=/AI-Project/datasets/training_dataset
cp /accesslog/access.log.* $folder
gunzip $folder/access.log.*
cat $folder/access.log.* > $folder/train_access.log
rm $folder/access.log.*
