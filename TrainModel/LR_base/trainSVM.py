#!/usr/bin/env python

from sklearn import linear_model
from sklearn import cross_validation
from sklearn.metrics import classification_report

import random
import numpy as np


def LoadData(trainfile):
    feature_pool = []
    label = []
    feature_test = []
    label_test = []
    for line in open(trainfile):
        linelist = line.strip().split(',')
        lb = int(linelist[0])
        
        if random.uniform(0, 1)<0.1:
            label_test.append(int(linelist[0]))
            feature_test.append([int(item) for item in linelist[1:len(linelist)] ])
            continue

        #if lb<1:
         #   if random.uniform(0, 1) < 0.98:
          #      continue

        label.append(int(linelist[0]))
        feature_pool.append([int(item) for item in linelist[1:len(linelist)] ])

    return feature_pool, label, feature_test, label_test


trainfile='/home/yipei/Twitter/FeatureExtraction/data/trainfile/LRbase/110445334.txt'

X, Y, X_test, Y_test = LoadData(trainfile)
print "num samples: ", len(Y)

from sklearn import svm
clf = svm.OneClassSVM(nu=0.1, kernel='linear', gamma=0.1)
clf.fit(X, Y)
 
print "parameter, ", clf.coef_
print "\ntest\n"

#accuracy = cross_validation.cross_val_score(clf, X_test, np.array(Y_test), cv=10)
#print accuracy
#print np.mean(accuracy)

Y_predict = clf.predict(X_test)
target_list = ['not_retweet', 'retweet']
print classification_report(Y_test, Y_predict)
