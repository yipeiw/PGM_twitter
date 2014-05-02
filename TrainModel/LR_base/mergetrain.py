#!/usr/bin/env python

from sklearn import linear_model
from sklearn import cross_validation
from sklearn.metrics import classification_report

import sys
import numpy as np
import os.path as path

import Loader

#trainfile='/home/yipei/Twitter/FeatureExtraction/data/trainfile/LRbase/110445334.txt'

trainlist=sys.argv[1]
paramfile = 'mergetrain_param.log'

pos_threshold = 10
effective = 0
f = open(paramfile, 'w')
X=[]
Y=[]
X_test=[]
Y_test=[]
for line in open(trainlist):
    trainfile = line.strip()
    X_list, Y_list, X_test_list, Y_test_list = Loader.LoadData(trainfile, 0.1, pos_threshold, 1)
    if len(Y_list)==0:
        continue
    effective += 1
    X += X_list[0]
    Y += Y_list[0]
    X_test += X_test_list[0]
    Y_test += Y_test_list[0]

    f.write(trainfile+'\n')

logreg = linear_model.LogisticRegression()
logreg.fit(X, Y)

f.write("%s\n" % (",".join([str(item) for item in logreg.coef_])))

Y_predict = logreg.predict(X_test)
target_list = ['not_retweet', 'retweet']
print(classification_report(Y_test, Y_predict, target_names=target_list))
f.close()
print "effective ", effective
