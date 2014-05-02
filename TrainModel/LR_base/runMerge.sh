#!/bin/bash

root=/home/yipei/Twitter

tool=$root/TrainModel/LR_base/mergetrain.py

userlist=$root/FeatureExtraction/data/trainfile/LR_sub100.list
#user=$root/FeatureExtraction/data/trainfile/LRbase/10350.txt

output=mergetrain.log

$tool $userlist #> $output
