#!/bin/bash
folderdata=/datasets/training_dataset
folderlog=/var/log/apache2

cd $PWD
cd ..
cp $folderlog/access.log.* $PWD$folderdata
gunzip $PWD$folderdata/access.log.*
cat $PWD$folderdata/access.log.* > $PWD$folderdata/train_access.log
rm $PWD$folderdata/access.log.*
