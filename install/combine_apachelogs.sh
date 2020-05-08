#!/bin/bash
localdir=$(pwd)
folderdata=/datasets/training_dataset
folderlog=/var/log/apache2

cp $folderlog/access.log.* $localdir$folderdata
gunzip $localdir$folderdata/access.log.*
cat $localdir$folderdata/access.log.* > $localdir$folderdata/train_access.log
rm $localdir$folderdata/access.log.*