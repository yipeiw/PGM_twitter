#!/bin/bash

root=/home/yipei/Twitter

tool=$root/TrainModel/LR_base/train.py

userlist=$root/FeatureExtraction/data/trainfile/LR_sub100.list
#user=$root/FeatureExtraction/data/trainfile/LRbase/10350.txt

output=train.log

$tool $userlist > $output
